# Adaptative-Clustering
# Details of Datasets
1 ReLink dataset :"Wu, Rongxin, et al. "Relink: recovering links between bugs and changes." Proceedings of the 19th ACM SIGSOFT symposium and the 13th European conference on Foundations of software engineering. 2011".


2 AEEEM dataset :"D’Ambros, Marco, Michele Lanza, and Romain Robbes. "Evaluating defect prediction approaches: a benchmark and an extensive comparison." Empirical Software Engineering 17 (2012): 531-577".


3 JIRA dataset :"Yatish, Suraj, et al. "Mining software defects: Should we consider affected releases?." 2019 IEEE/ACM 41st international conference on software engineering (ICSE). IEEE, 2019".

4 T. Menzies, R. Krishna, and D. Pryor, “The promise repository of empirical software engineering data (2015),” URL http://promisedata.googlecode. com, 2015.

5 L.-q. Chen, C. Wang, and S.-l. Song, “Software defect prediction based on nested-stacking and heterogeneous feature selection,” Complex & Intelligent Systems, vol. 8, no. 4, pp. 3333–3348, 2022.


# Metrics Details of ReLink Dataset
| **Abbreviation**      | **Description**                                                |
| --------------------- | -------------------------------------------------------------- |
| AvgCyclomatic         | Average Cyclomatic Complexity                                  |
| AvgCyclomaticModified | Average Modified Cyclomatic Complexity                         |
| AvgCyclomaticStrict   | Average Strict Cyclomatic Complexity                           |
| AvgEssential          | Average Essential Complexity                                   |
| AvgLine               | Average Lines                                                  |
| AvgLineBlank          | Average Blank Lines                                            |
| AvgLineCode           | Average Code Lines                                             |
| AvgLineComment        | Average Comment Lines                                          |
| CountLine             | Number of Lines                                                |
| CountLineBlank        | Number of Blank Lines                                          |
| CountLineCode         | Number of Code Lines                                           |
| CountLineCodeDecl     | Number of Declarative Code Lines                               |
| CountLineCodeExe      | Number of Executable Code Lines                                |
| CountLineComment      | Number of Comment Lines                                        |
| CountSemicolon        | Number of Semicolons                                           |
| CountStmt             | Number of Statements                                           |
| CountStmtDecl         | Number of Declarative Statements                               |
| CountStmtExe          | Number of Executive Statements                                 |
| MaxCyclomatic         | Maximum Cyclomatic Complexity of all nested functions          |
| MaxCyclomaticModified | Maximum Modified Cyclomatic Complexity of all nested functions |
| MaxCyclomaticStrict   | Maximum Strict Cyclomatic Complexity of all nested functions   |
| RatioCommentToCode    | Ratio of Comment Lines to Code Lines                           |
| SumCyclomatic         | Sum of Cyclomatic Complexity of all nested functions           |
| SumCyclomaticModified | Sum of Modified Cyclomatic Complexity of all nested functions  |
| SumCyclomaticStrict   | Sum of Strict Cyclomatic Complexity of all nested functions    |
| SumEssential          | Sum of Essential Complexity of all nested functions            |

# Metrics Details of AEEEM Dataset
| **Abbreviation**                   | **Description**                                                                    |
| ---------------------------------- | ---------------------------------------------------------------------------------- |
| ck\_oo\_wmc                        | Weighted method count                                                              |
| ck\_oo\_dit                        | Depth of inheritance tree                                                          |
| ck\_oo\_rfc                        | Response for class                                                                 |
| ck\_oo\_noc                        | Number of children                                                                 |
| ck\_oo\_cbo                        | Coupling between objects                                                           |
| ck\_oo\_lcom                       | Lack of cohesion in methods                                                        |
| ck\_oo\_fanin                      | Number of other classes that reference the class                                   |
| ck\_oo\_fanout                     | Number of other classes referenced by the class                                    |
| ck\_oo\_noa                        | Number of attributes                                                               |
| ck\_oo\_nopa                       | Number of public attributes                                                        |
| ck\_oo\_nopra                      | Number of private attributes                                                       |
| ck\_oo\_noai                       | Number of attributes inherited                                                     |
| ck\_oo\_loc                        | Number of lines of code                                                            |
| ck\_oo\_nom                        | Number of methods                                                                  |
| ck\_oo\_nopm                       | Number of public methods                                                           |
| ck\_oo\_noprm                      | Number of private methods                                                          |
| ck\_oo\_nomt                       | Number of methods inherited                                                        |
| WCHU\_wmc                          | Weighted churn of weighted method count                                            |
| WCHU\_dit                          | Weighted churn of depth of inheritance tree                                        |
| WCHU\_rfc                          | Weighted churn of response for class                                               |
| WCHU\_noc                          | Weighted churn of number of children                                               |
| WCHU\_cbo                          | Weighted churn of coupling between objects                                         |
| WCHU\_lcom                         | Weighted churn of lack of cohesion in methods                                      |
| WCHU\_fanin                        | Weighted churn of number of other classes that reference the class                 |
| WCHU\_fanout                       | Weighted churn of number of other classes referenced by the class                  |
| WCHU\_noa                          | Weighted churn of number of attributes                                             |
| WCHU\_nopa                         | Weighted churn of number of public attributes                                      |
| WCHU\_nopra                        | Weighted churn of number of private attributes                                     |
| WCHU\_noai                         | Weighted churn of number of attributes inherited                                   |
| WCHU\_loc                          | Weighted churn of number of lines of code                                          |
| WCHU\_nom                          | Weighted churn of number of methods                                                |
| WCHU\_nopm                         | Weighted churn of number of public methods                                         |
| WCHU\_noprm                        | Weighted churn of number of private methods                                        |
| WCHU\_nomt                         | Weighted churn of number of methods inherited                                      |
| LDHH\_wmc                          | Linear decayed history entropy of weighted method count                            |
| LDHH\_dit                          | Linear decayed history entropy of depth of inheritance tree                        |
| LDHH\_rfc                          | Linear decayed history entropy of response for class                               |
| LDHH\_noc                          | Linear decayed history entropy of number of children                               |
| LDHH\_cbo                          | Linear decayed history entropy of coupling between objects                         |
| LDHH\_lcom                         | Linear decayed history entropy of lack of cohesion in methods                      |
| LDHH\_fanin                        | Linear decayed history entropy of number of other classes that reference the class |
| LDHH\_fanout                       | Linear decayed history entropy of number of other classes referenced by the class  |
| LDHH\_noa                          | Linear decayed history entropy of number of attributes                             |
| LDHH\_nopa                         | Linear decayed history entropy of number of public attributes                      |
| LDHH\_nopra                        | Linear decayed history entropy of number of private attributes                     |
| LDHH\_noai                         | Linear decayed history entropy of number of attributes inherited                   |
| LDHH\_loc                          | Linear decayed history entropy of number of lines of code                          |
| LDHH\_nom                          | Linear decayed history entropy of number of methods                                |
| LDHH\_nopm                         | Linear decayed history entropy of number of public methods                         |
| LDHH\_noprm                        | Linear decayed history entropy of number of private methods                        |
| LDHH\_nomt                         | Linear decayed history entropy of number of methods inherited                      |
| CvsEntropy                         | Entropy of CVS change log                                                          |
| CvsWEntropy                        | Weighted Entropy of CVS change log                                                 |
| CvsLogEntropy                      | Logarithmic Entropy of CVS change log                                              |
| CvsExpEntropy                      | Exponential Entropy of CVS change log                                              |
| CvsLinEntropy                      | Linear Entropy of CVS change log                                                   |
| numberOfNonTrivialBugsFoundUntil   | Number of non-trivial bugs found until the corresponding fix                       |
| numberOfCriticalBugsFoundUntil     | Number of critical bugs found until the corresponding fix                          |
| numberOfHighPriorityBugsFoundUntil | Number of high priority bugs found until the corresponding fix                     |
| numberOfMajorBugsFoundUntil        | Number of major bugs found until the corresponding fix                             |
| numberOfBugsFoundUntil             | Number of bugs found until the corresponding fix                                   |

# Metrics Details of JIRA Dataset
| **Abbreviation**          | **Description**                                                            |
| ------------------------- | -------------------------------------------------------------------------- |
| AvgCyclomatic             | Average cyclomatic complexity for all nested functions or methods          |
| SumCyclomatic             | Sum of cyclomatic complexity of all nested functions or methods            |
| AvgCyclomaticModified     | Average modified cyclomatic complexity for all nested functions or methods |
| SumCyclomaticModified     | Sum of modified cyclomatic complexity of all nested functions              |
| AvgCyclomaticStrict       | Average strict cyclomatic complexity for all nested functions or methods   |
| SumCyclomaticStrict       | Sum of strict cyclomatic complexity of all nested functions or methods     |
| AvgEssential              | Average essential complexity for all nested functions or methods           |
| SumEssential              | Sum of essential complexity of all nested functions or methods             |
| AvgLine                   | Average number of lines for all nested functions or methods                |
| AvgLineBlank              | Average number of blank lines for all nested functions or methods          |
| AvgLineCode               | Average number of lines containing source code for all nested functions    |
| AvgLineComment            | Average number of comment lines for all nested functions or methods        |
| CountClassBase            | Number of immediate base classes                                           |
| CountClassCoupled         | Number of other classes coupled to                                         |
| CountClassDerived         | Number of immediate subclasses                                             |
| MaxInheritanceTree        | Maximum depth of class in inheritance tree                                 |
| PercentLackOfCohesion     | 100% minus the average cohesion for package entities                       |
| CountDeclClass            | Number of classes                                                          |
| CountDeclClassMethod      | Number of class methods                                                    |
| CountDeclClassVariable    | Number of class variables                                                  |
| CountDeclFunction         | Number of functions                                                        |
| CountDeclInstanceMethod   | Number of instance methods                                                 |
| CountDeclInstanceVariable | Number of instance variables                                               |
| CountDeclMethod           | Number of local (non-inherited) methods                                    |
| CountDeclMethodDefault    | Number of local default methods                                            |
| CountDeclMethodPrivate    | Number of local (non-inherited) private methods                            |
| CountDeclMethodProtected  | Number of local protected methods                                          |
| CountDeclMethodPublic     | Number of local (non-inherited) public methods                             |
| CountLine                 | Number of physical lines                                                   |
| CountLineBlank            | Number of blank lines                                                      |
| CountLineCode             | Number of lines containing source code                                     |
| CountLineCodeDecl         | Number of lines containing declarative source code                         |
| CountLineCodeExe          | Number of lines containing executable source code                          |
| CountLineComment          | Number of lines containing comment                                         |
| CountSemicolon            | Number of semicolons                                                       |
| CountStmt                 | Number of statements                                                       |
| CountStmtDecl             | Number of declarative statements                                           |
| CountStmtExe              | Number of executable statements                                            |
| MaxCyclomatic             | Maximum cyclomatic complexity of all nested functions or methods           |
| MaxCyclomaticModified     | Maximum modified cyclomatic complexity of nested functions or methods      |
| MaxCyclomaticStrict       | Maximum strict cyclomatic complexity of nested functions or methods        |
| RatioCommentToCode        | Ratio of comment lines to code lines                                       |
| CountInput\_Min           | Min number of calling subprograms plus global variables read               |
| CountInput\_Mean          | Mean number of calling subprograms plus global variables read              |
| CountInput\_Max           | Max number of calling subprograms plus global variables read               |
| CountOutput\_Min          | Min number of called subprograms plus global variables set                 |
| CountOutput\_Mean         | Mean number of called subprograms plus global variables set                |
| CountOutput\_Max          | Max number of called subprograms plus global variables set                 |
| CountPath\_Min            | Min number of unique paths through a body of code                          |
| CountPath\_Mean           | Mean number of unique paths through a body of code                         |
| CountPath\_Max            | Max number of unique paths through a body of code                          |
| MaxNesting\_Min           | Min of maximum nesting level of control constructs in the function         |
| MaxNesting\_Mean          | Mean of maximum nesting level of control constructs in the function        |
| MaxNesting\_Max           | Max of maximum nesting level of control constructs in the function         |
| COMM                      | Number of Git commits                                                      |
| ADDED\_LINES              | Normalized number of lines added to the module                             |
| DEL\_LINES                | Normalized number of lines deleted from the module                         |
| ADEV                      | Number of active developers                                                |
| DDEV                      | Number of distinct developers                                              |
| MINOR\_COMMIT             | Developers contributing <5% of total code changes                          |
| MINOR\_LINE               | Developers contributing <5% of total LOC                                   |
| MAJOR\_COMMIT             | Developers contributing >5% of total code changes                          |
| MAJOR\_LINES              | Developers contributing >5% of total LOC                                   |
| OWN\_COMMIT               | Proportion of code changes by top contributor                              |
| OWN\_LINE                 | Proportion of lines of code by top contributor                             |

# Metrics Details of PROMISE Dataset
| **Abbreviation** | **Description** |
|------------------|-----------------|
| WMC              | Weighted Methods per Class |
| DIT              | Depth of Inheritance Tree |
| NOC              | Number of Children |
| CBO              | Coupling Between Object Classes |
| RFC              | Response for a Class |
| LCOM             | Lack of Cohesion in Methods |
| CA               | Afferent Couplings |
| CE               | Efferent Couplings |
| NPM              | Number of Public Methods |
| LCOM3            | Lack of Cohesion in Methods (variant of LCOM) |
| LOC              | Lines of Code |
| DAM              | Data Access Metric |
| MOA              | Measure of Aggregation |
| MFA              | Measure of Functional Abstraction |
| CAM              | Cohesion Among Methods of a Class |
| IC               | Inheritance Coupling |
| CBM              | Coupling Between Methods |
| AMC              | Average Method Complexity |
| CC               | McCabe’s Cyclomatic Complexity |
| MAX_CC           | Maximum Value of CC Among Methods in the Class |
| AVG_CC           | Average (Arithmetic Mean) CC of Methods in the Class |

# Metrics Details of Kamei Dataset
| **Abbreviation** | **Description** |
|----------|----------------|
| NS     | Number of modified subsystems. |
| ND     | Number of modified directories. |
| NF     | Number of modified files. |
| Entropy | Distribution of modified code across each file, measuring the spread of changes. |
| LA     | Lines of code added during the change. |
| LD     | Lines of code deleted during the change. |
| LT     | Lines of code in a file before the change. |
| FIX    | Binary indicator of whether the change is a defect fix (`1`) or not (`0`). |
| NDEV   | Number of distinct developers who previously modified the affected files. |
| PD     | Average time interval between the current and previous changes to the files. |
| NPT    | Number of unique previous changes to the files. |
| EXP    | Developer’s overall experience, typically measured by number of prior commits. |
| REXP   | Developer’s recent experience, often computed with time-decay weighting. |
| SEXP   | Developer’s experience within the specific subsystem of the modified files. |

# Number of Clusters for each target Project using adaptive spectral clustering

| Target Project        | Number of Clusters |
|-----------------------|--------------------|
| Apache                | 5 |
| Safe                  | 3 |
| Zxing                 | 4 |
| Equinox               | 5 |
| Jdt                   | 4 |
| Lucene                | 5 |
| Mylyn                 | 2 |
| Pde                   | 5 |
| Activemq-5.2.0        | 5 |
| Derby-10.2.1.6        | 5 |
| Groovy-1_5_7          | 5 |
| Hbase-0.94.0          | 3 |
| Hive-0.9.0            | 3 |
| Jruby-1.1             | 5 |
| Wicket-1.3.0beta-1    | 2 |
| Ant-1.3               | 4 |
| Ivy-2.0               | 4 |
| Jedit-4.1             | 4 |
| Log4j-1.0             | 3 |
| Synapse-1.2           | 4 |
| Tomcat                | 5 |
| Xalan-2.4             | 4 |
| Bugzilla              | 4 |
| Columba               | 3 |
| Postgres              | 5 |


# Performance of the traditional full-project approach (FPA) with different classifiers in terms of AUC and MCC.
| Target        | **AUC — FPA-DNN** |   FPA-LR |   FPA-RF | FPA-SVM | FPA-KNN |   FPA-NB | **MCC — FPA-DNN** |   FPA-LR |   FPA-RF | FPA-SVM |  FPA-KNN |   FPA-NB |
| ------------- | ----------------: | -------: | -------: | ------: | ------: | -------: | ----------------: | -------: | -------: | ------: | -------: | -------: |
| Apache        |          **0.73** |     0.67 |     0.60 |    0.69 |    0.64 |     0.61 |          **0.42** |     0.36 |     0.14 |    0.32 |     0.28 |     0.24 |
| Safe          |          **0.74** |     0.73 |     0.71 |    0.71 |    0.66 |     0.65 |              0.27 | **0.38** |     0.35 |    0.27 |     0.28 |     0.34 |
| Zxing         |          **0.62** |     0.60 |     0.58 |    0.58 |    0.53 |     0.58 |          **0.22** |     0.11 |     0.14 |    0.15 |     0.10 |     0.20 |
| Equinox       |              0.67 | **0.72** |     0.70 |    0.63 |    0.58 | **0.72** |          **0.37** |     0.33 |     0.30 |    0.31 |     0.22 |     0.31 |
| Jdt           |          **0.77** |     0.74 |     0.70 |    0.69 |    0.59 |     0.69 |          **0.46** |     0.41 |     0.29 |    0.39 |     0.17 |     0.39 |
| Lucene        |          **0.75** |     0.69 |     0.69 |    0.68 |    0.62 |     0.70 |              0.26 |     0.21 |     0.23 |    0.23 |     0.16 | **0.32** |
| Mylyn         |          **0.76** |     0.71 |     0.72 |    0.69 |    0.51 |     0.71 |          **0.51** |     0.25 |     0.26 |    0.29 |     0.13 |     0.38 |
| Pde           |          **0.73** |     0.71 |     0.68 |    0.69 |    0.65 |     0.69 |              0.26 |     0.30 |     0.28 |    0.28 |     0.17 | **0.33** |
| Activemq-5..  |          **0.80** |     0.78 |     0.78 |    0.73 |    0.69 |     0.75 |              0.32 |     0.34 | **0.38** |    0.28 |     0.26 | **0.38** |
| Derby-10..    |          **0.81** |     0.77 |     0.73 |    0.76 |    0.66 |     0.72 |          **0.53** |     0.42 |     0.29 |    0.39 |     0.32 |     0.31 |
| Groovy-1\_5.. |              0.76 |     0.72 | **0.78** |    0.71 |    0.76 |     0.72 |          **0.27** |     0.18 |     0.25 |    0.17 |     0.22 | **0.27** |
| Hbase-0.94..  |          **0.78** |     0.75 |     0.76 |    0.72 |    0.70 |     0.70 |              0.25 |     0.29 | **0.34** |    0.31 |     0.30 |     0.26 |
| Hive-0.9..    |              0.66 |     0.67 |     0.67 |    0.57 |    0.58 | **0.68** |          **0.31** |     0.27 |     0.27 |    0.22 |     0.20 |     0.25 |
| Jruby-1.1     |          **0.85** |     0.82 |     0.80 |    0.76 |    0.79 |     0.79 |          **0.36** |     0.32 |     0.29 |    0.30 | **0.36** |     0.30 |
| Wicket-1.3..  |          **0.85** |     0.83 |     0.81 |    0.66 |    0.64 |     0.74 |              0.25 |     0.26 |     0.13 |    0.10 |     0.08 | **0.28** |
| Ant-1.3       |          **0.81** |     0.74 |     0.77 |    0.66 |    0.65 |     0.70 |              0.27 |     0.27 | **0.36** |    0.23 |     0.18 |     0.27 |
| Ivy-2.0       |          **0.77** |     0.73 |     0.72 |    0.69 |    0.65 |     0.71 |          **0.33** |     0.25 |     0.30 |    0.24 |     0.18 |     0.28 |
| Jedit-4.1     |          **0.78** |     0.75 |     0.62 |    0.69 |    0.66 |     0.72 |          **0.49** |     0.40 |     0.26 |    0.26 |     0.29 |     0.33 |
| Log4j-1.0     |          **0.78** |     0.71 |     0.70 |    0.67 |    0.60 |     0.74 |              0.35 |     0.23 |     0.32 |    0.30 |     0.22 | **0.38** |
| Synapse-1.2   |          **0.72** |     0.70 |     0.63 |    0.59 |    0.58 |     0.67 |          **0.31** |     0.29 |     0.21 |    0.17 |     0.21 |     0.30 |
| Tomcat        |          **0.74** |     0.72 |     0.73 |    0.70 |    0.64 |     0.73 |          **0.27** |     0.24 |     0.20 |    0.21 |     0.17 |     0.25 |
| Xalan-2.4     |              0.66 |     0.64 | **0.68** |    0.63 |    0.62 |     0.67 |              0.17 |     0.18 |     0.19 |    0.14 |     0.20 | **0.24** |
| Bugzilla      |              0.62 |     0.60 | **0.66** |    0.61 |    0.55 |     0.56 |              0.23 |     0.21 | **0.24** |    0.20 |     0.16 |     0.21 |
| Columba       |          **0.67** |     0.63 |     0.64 |    0.63 |    0.58 |     0.41 |          **0.30** |     0.23 |     0.23 |    0.24 |     0.18 |    -0.02 |
| Postgres      |              0.65 |     0.62 | **0.66** |    0.63 |    0.60 |     0.64 |              0.23 |     0.26 |     0.24 |    0.25 |     0.19 | **0.29** |
| **Average**   |          **0.74** |     0.71 |     0.70 |    0.67 |    0.63 |     0.68 |          **0.32** |     0.28 |     0.26 |    0.25 |     0.21 |     0.28 |

# Performance of the proposed ASCSA approach with different classifiers in terms of AUC and MCC.

| Target        | **AUC — ASCSA-DNN** | ASCSA-LR | ASCSA-RF | ASCSA-SVM | ASCSA-KNN | ASCSA-NB | **MCC — ASCSA-DNN** | ASCSA-LR | ASCSA-RF | ASCSA-SVM | ASCSA-KNN | ASCSA-NB |
| ------------- | ------------------: | -------: | -------: | --------: | --------: | -------: | ------------------: | -------: | -------: | --------: | --------: | -------: |
| Apache        |            **0.78** |     0.72 |     0.70 |      0.73 |      0.71 |     0.70 |            **0.44** |     0.42 |     0.33 |      0.36 |      0.32 |     0.36 |
| Safe          |            **0.82** |     0.73 |     0.74 |      0.70 |      0.72 |     0.75 |            **0.36** |     0.33 |     0.31 |      0.24 |      0.32 |     0.34 |
| Zxing         |            **0.66** |     0.62 |     0.61 |      0.64 |      0.58 |     0.60 |            **0.24** |     0.14 |     0.18 |      0.17 |      0.12 |     0.16 |
| Equinox       |            **0.76** |     0.74 |     0.72 |      0.70 |      0.64 |     0.75 |            **0.42** |     0.36 |     0.31 |      0.37 |      0.40 |     0.34 |
| Jdt           |            **0.84** |     0.77 |     0.73 |      0.75 |      0.66 |     0.74 |            **0.50** |     0.47 |     0.37 |      0.44 |      0.29 |     0.45 |
| Lucene        |            **0.77** |     0.72 |     0.70 |      0.72 |      0.67 |     0.75 |            **0.32** |     0.25 |     0.27 |      0.24 |      0.16 |     0.30 |
| Mylyn         |            **0.83** |     0.73 |     0.78 |      0.75 |      0.54 |     0.76 |            **0.54** |     0.30 |     0.45 |      0.40 |      0.13 |     0.50 |
| Pde           |            **0.79** |     0.75 |     0.70 |      0.73 |      0.69 |     0.76 |                0.32 | **0.33** | **0.33** |      0.30 |      0.21 |     0.32 |
| Activemq-5..  |            **0.88** |     0.87 |     0.83 |      0.80 |      0.74 |     0.81 |            **0.51** |     0.41 |     0.46 |      0.38 |      0.29 |     0.43 |
| Derby-10..    |            **0.85** |     0.79 |     0.69 |      0.80 |      0.71 |     0.76 |            **0.54** |     0.49 |     0.30 |      0.45 |      0.35 |     0.38 |
| Groovy-1\_5.. |            **0.82** |     0.76 |     0.80 |      0.74 |      0.78 |     0.79 |            **0.28** |     0.24 |     0.19 |      0.17 |      0.19 |     0.26 |
| Hbase-0.94..  |            **0.84** |     0.78 |     0.76 |      0.76 |      0.74 |     0.78 |            **0.37** |     0.35 |     0.36 |      0.34 |      0.29 |     0.32 |
| Hive-0.9..    |                0.69 | **0.70** |     0.68 |      0.63 |      0.53 |     0.66 |            **0.33** |     0.27 |     0.30 |      0.27 |      0.04 |     0.28 |
| Jruby-1.1     |            **0.92** |     0.86 |     0.83 |      0.77 |      0.81 |     0.84 |                0.38 |     0.36 |     0.32 |      0.31 |      0.33 | **0.40** |
| Wicket-1.3..  |            **0.90** |     0.88 |     0.85 |      0.72 |      0.70 |     0.80 |                0.22 |     0.27 |     0.16 |      0.13 |      0.09 | **0.28** |
| Ant-1.3       |            **0.85** |     0.81 |     0.75 |      0.73 |      0.71 |     0.78 |                0.29 |     0.30 | **0.32** |      0.27 |      0.22 |     0.28 |
| Ivy-2.0       |            **0.82** |     0.81 |     0.76 |      0.75 |      0.67 |     0.77 |            **0.37** |     0.33 |     0.34 |      0.35 |      0.13 |     0.32 |
| Jedit-4.1     |            **0.82** |     0.78 |     0.73 |      0.71 |      0.71 |     0.76 |            **0.50** |     0.44 |     0.35 |      0.30 |      0.35 |     0.41 |
| Log4j-1.0     |            **0.85** |     0.77 |     0.70 |      0.68 |      0.65 |     0.80 |            **0.42** |     0.37 |     0.23 |      0.26 |      0.32 |     0.40 |
| Synapse-1.2   |            **0.77** |     0.73 |     0.66 |      0.60 |      0.60 |     0.75 |            **0.34** |     0.31 |     0.22 |      0.23 |      0.17 |     0.29 |
| Tomcat        |            **0.80** |     0.76 |     0.78 |      0.75 |      0.74 |     0.75 |            **0.29** |     0.20 |     0.28 |      0.26 |      0.25 |     0.26 |
| Xalan-2.4     |                0.68 |     0.66 |     0.66 |      0.62 |      0.65 | **0.70** |            **0.20** |     0.18 |     0.19 |      0.17 |      0.15 |     0.19 |
| Bugzilla      |                0.69 | **0.70** | **0.70** |      0.66 |      0.60 |     0.63 |            **0.28** |     0.23 |     0.26 |      0.25 |      0.20 |     0.23 |
| Columba       |            **0.74** |     0.67 |     0.69 |      0.68 |      0.63 |     0.46 |            **0.35** |     0.28 |     0.29 |      0.29 |      0.19 |     0.05 |
| Postgres      |            **0.72** |     0.66 |     0.69 |      0.68 |      0.64 |     0.70 |            **0.32** |     0.27 |     0.27 |      0.30 |      0.22 |     0.30 |
| **Average**   |            **0.80** |     0.75 |     0.73 |      0.71 |      0.67 |     0.73 |            **0.37** |     0.32 |     0.30 |      0.29 |      0.23 |     0.31 |


## Performance Comparison of ASCSA with Domain-Adaptation Methods (AUC)


| Target | ASCSA | TCA+ | CORAL | DeepCORAL | DANN | JMMD |
|---|---:|---:|---:|---:|---:|---:|
| Apache | 0.78 | 0.73 | 0.68 | 0.76 | 0.76 | 0.68 |
| Safe | 0.82 | 0.76 | 0.77 | 0.79 | 0.77 | 0.78 |
| Zxing | 0.66 | 0.63 | 0.62 | 0.63 | 0.62 | 0.62 |
| Equinox | 0.76 | 0.75 | 0.78 | 0.67 | 0.74 | 0.62 |
| Jdt | 0.84 | 0.79 | 0.78 | 0.80 | 0.77 | 0.76 |
| Lucene | 0.77 | 0.73 | 0.76 | 0.73 | 0.77 | 0.77 |
| Mylyn | 0.83 | 0.78 | 0.72 | 0.78 | 0.77 | 0.75 |
| Pde | 0.79 | 0.81 | 0.77 | 0.77 | 0.75 | 0.75 |
| Activemq-5.2.0 | 0.88 | 0.85 | 0.87 | 0.86 | 0.84 | 0.79 |
| Derby-10.2.1.6 | 0.85 | 0.78 | 0.83 | 0.85 | 0.83 | 0.79 |
| Groovy-1_5_7 | 0.82 | 0.80 | 0.81 | 0.82 | 0.84 | 0.81 |
| Hbase-0.94.0 | 0.84 | 0.79 | 0.80 | 0.82 | 0.82 | 0.82 |
| Hive-0.9.0 | 0.69 | 0.74 | 0.71 | 0.59 | 0.71 | 0.71 |
| Jruby-1.1 | 0.92 | 0.87 | 0.89 | 0.87 | 0.87 | 0.89 |
| Wicket-1.3.0beta-1 | 0.90 | 0.82 | 0.83 | 0.81 | 0.82 | 0.83 |
| Ant-1.3 | 0.85 | 0.81 | 0.81 | 0.83 | 0.84 | 0.84 |
| Ivy-2.0 | 0.82 | 0.78 | 0.78 | 0.79 | 0.78 | 0.77 |
| Jedit-4.1 | 0.82 | 0.82 | 0.81 | 0.81 | 0.80 | 0.81 |
| Log4j-1.0 | 0.85 | 0.77 | 0.79 | 0.81 | 0.79 | 0.82 |
| Synapse-1.2 | 0.77 | 0.72 | 0.74 | 0.75 | 0.72 | 0.70 |
| Tomcat | 0.80 | 0.75 | 0.76 | 0.77 | 0.73 | 0.74 |
| Xalan-2.4 | 0.68 | 0.63 | 0.65 | 0.68 | 0.68 | 0.66 |
| Bugzilla | 0.69 | 0.52 | 0.68 | 0.63 | 0.64 | 0.63 |
| Columba | 0.74 | 0.59 | 0.66 | 0.70 | 0.70 | 0.71 |
| Postgres | 0.72 | 0.67 | 0.69 | 0.70 | 0.68 | 0.67 |
| **Average** | **0.80** | 0.75 | 0.76 | 0.76 | 0.76 | 0.75 |


### Sensitivity Analysis for Number of Selected Clusters (K)

| K     | Average AUC | Std. AUC | Average MCC | Std. MCC |
|------:|------------:|---------:|------------:|---------:|
| 1     | 0.76        | 0.04     | 0.32        | 0.05     |
| 2     | 0.78        | 0.03     | 0.34        | 0.04     |
| 3     | 0.79        | 0.03     | 0.35        | 0.04     |
| 4     | 0.80        | 0.02     | 0.36        | 0.03     |
| **5** | **0.80**    | **0.02** | **0.37**    | **0.03** |
| 6     | 0.79        | 0.02     | 0.36        | 0.03     |
| 7     | 0.78        | 0.03     | 0.35        | 0.04     |
| 8     | 0.77        | 0.03     | 0.34        | 0.04     |
| 9     | 0.76        | 0.04     | 0.33        | 0.05     |
| 10    | 0.75        | 0.04     | 0.32        | 0.05     |


### Sensitivity Analysis for MMD Weight (λ)

| λ     | Average AUC | Std. AUC | Average MCC | Std. MCC |
|------:|------------:|---------:|------------:|---------:|
| 0.00  | 0.77        | 0.04     | 0.35        | 0.05     |
| 0.25  | 0.79        | 0.03     | 0.36        | 0.04     |
| **0.50** | **0.80** | **0.02** | **0.37**    | **0.03** |
| 0.75  | 0.79        | 0.03     | 0.36        | 0.04     |
| 1.00  | 0.78        | 0.04     | 0.35        | 0.05     |



