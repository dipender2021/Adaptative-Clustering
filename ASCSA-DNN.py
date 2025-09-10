import numpy as np
import pandas as pd
import torch
import torch.nn as nn
from torch.utils.data import TensorDataset, DataLoader
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score

def set_seed():
    import random
    random.seed(s); np.random.seed(s)
    torch.manual_seed(s); torch.cuda.manual_seed_all(s)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False

def to_loader():
    X = torch.tensor(X, dtype=torch.float32)
    if y is None:
        ds = TensorDataset(X)
    else:
        y = torch.tensor(y, dtype=torch.float32)
        ds = TensorDataset(X, y)
    return DataLoader(ds, batch_size=bs, shuffle=shuffle)

def adaptive_partition(X):
    n = X.shape[0]
    dummy = np.arange(n) % 2
    labels = np.zeros(n, dtype=int)
    labels[:] = dummy
    return labels

def structural_score(X_block, X_target):
    xb_mean = np.mean(X_block, axis=0, keepdims=True)
    xt_mean = np.mean(X_target, axis=0, keepdims=True)
    diff = np.linalg.norm(xb_mean - xt_mean)
    return float(diff)

def domain_align_loss(Fs, Ft):
    if Fs.size(0) == 0 or Ft.size(0) == 0:
        return torch.tensor(0.0, device=Fs.device)
    mean_s = Fs.mean(0)
    mean_t = Ft.mean(0)
    dist = torch.norm(mean_s - mean_t, p=2)
    return dist

class DNN(nn.Module):
    def __init__(self, d_in):
        super().__init__()
        self.f = nn.Sequential(
            nn.Linear(d_in, d_in), nn.ReLU()
        )
        self.clf = nn.Linear(d_in, 1)
    def forward(self, x):
        z = self.f(x)
        logit = self.clf(z).squeeze(-1)
        return logit, z

def train_model(model, src_loader, tgt_loader=None):
    model.to(device)
    opt = torch.optim.Adam(model.parameters(), lr=lr)
    bce = nn.BCEWithLogitsLoss()
    for _ in range(epochs):
        model.train()
        it = zip(src_loader, tgt_loader) if tgt_loader is not None else ((b, (None,)) for b in src_loader)
        for src_batch, tgt_batch in it:
            xs, ys = src_batch
            xt = tgt_batch[0] if tgt_loader is not None else None
            xs, ys = xs.to(device), ys.to(device)
            opt.zero_grad()
            log_s, z_s = model(xs)
            loss = bce(log_s, ys)
            if xt is not None:
                xt = xt.to(device)
                _, z_t = model(xt)
                loss = loss + lam * domain_align_loss(z_s, z_t)
            loss.backward()
            opt.step()
    return model

def evaluate(model, X):
    model.eval()
    xb = torch.tensor(X, dtype=torch.float32, device=device)
    logit, _ = model(xb)
    prob = torch.sigmoid(logit).cpu().numpy()
    metrics = {}
    if y is not None:
        y = np.asarray(y).astype(int)
        pred = (prob >= 0.5).astype(int)
        metrics = dict(
            precision=precision_score(y, pred, zero_division=0),
            recall=recall_score(y, pred, zero_division=0),
            f1=f1_score(y, pred, zero_division=0),
            auc=roc_auc_score(y, prob) if len(np.unique(y)) == 2 else float("nan"),
        )
    return prob, metrics

def run_pipeline(source_list, target_tuple):
    scaler = MinMaxScaler()
    X_tgt, y_tgt = target_tuple
    X_tgt = scaler.fit_transform(X_tgt)
    candidates = []
    for Xs, ys in source_list:
        Xs = scaler.fit_transform(Xs)
        lbl = adaptive_partition(Xs)
        for c in np.unique(lbl):
            m = lbl == c
            Xb, yb = Xs[m], ys[m]
            s = structural_score(Xb, X_tgt)
            candidates.append((s, Xb, yb))
    candidates.sort(key=lambda t: t[0])
    X_tr = np.vstack([c[1] for c in candidates[:top_k]]) if candidates else np.empty((0, X_tgt.shape[1]))
    y_tr = np.hstack([c[2] for c in candidates[:top_k]]) if candidates else np.empty((0,))
    if X_tr.size == 0:
        return np.zeros(len(X_tgt)), {}
    model = DNN(d_in=X_tr.shape[1])
    src_loader = to_loader(X_tr, y_tr, shuffle=True)
    tgt_loader = to_loader(X_tgt, None, shuffle=True)
    model = train_model(model, src_loader, tgt_loader, lam=lam, device=device)
    probs, metrics = evaluate(model, X_tgt, y=y_tgt, device=device)
    return probs, metrics
