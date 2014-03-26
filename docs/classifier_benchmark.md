Classifying 0 th split of fair apps with unfair app
-------------------------------------------------------------------------------


Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=distance)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.50      0.67      0.57         3
       True       0.50      0.33      0.40         3

avg / total       0.50      0.50      0.49         6



Confusion matrix:
[[2 1]
 [2 1]]


Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=uniform)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.50      0.67      0.57         3
       True       0.50      0.33      0.40         3

avg / total       0.50      0.50      0.49         6



Confusion matrix:
[[2 1]
 [2 1]]


Classifier: 
 GaussianNB()
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.60      1.00      0.75         3
       True       1.00      0.33      0.50         3

avg / total       0.80      0.67      0.62         6



Confusion matrix:
[[3 0]
 [2 1]]


Classifier: 
 DecisionTreeClassifier(compute_importances=None, criterion=gini,
            max_depth=None, max_features=None, min_density=None,
            min_samples_leaf=1, min_samples_split=2, random_state=None,
            splitter=best)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.75      1.00      0.86         3
       True       1.00      0.67      0.80         3

avg / total       0.88      0.83      0.83         6



Confusion matrix:
[[3 0]
 [1 2]]


Classifier: 
 SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, degree=3, gamma=0.0,
  kernel=rbf, max_iter=-1, probability=False, random_state=None,
  shrinking=True, tol=0.001, verbose=False)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.60      1.00      0.75         3
       True       1.00      0.33      0.50         3

avg / total       0.80      0.67      0.62         6



Confusion matrix:
[[3 0]
 [2 1]]


Classifier: 
 NuSVC(cache_size=200, coef0=0.0, degree=3, gamma=0.0, kernel=rbf, max_iter=-1,
   nu=0.5, probability=False, random_state=None, shrinking=True, tol=0.001,
   verbose=False)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       1.00      0.33      0.50         3
       True       0.60      1.00      0.75         3

avg / total       0.80      0.67      0.62         6



Confusion matrix:
[[1 2]
 [0 3]]


Classifier: 
 AdaBoostClassifier(algorithm=SAMME,
          base_estimator=DecisionTreeClassifier(compute_importances=None, criterion=gini, max_depth=1,
            max_features=None, min_density=None, min_samples_leaf=1,
            min_samples_split=2, random_state=None, splitter=best),
          base_estimator__compute_importances=None,
          base_estimator__criterion=gini, base_estimator__max_depth=1,
          base_estimator__max_features=None,
          base_estimator__min_density=None,
          base_estimator__min_samples_leaf=1,
          base_estimator__min_samples_split=2,
          base_estimator__random_state=None, base_estimator__splitter=best,
          learning_rate=1.0, n_estimators=200, random_state=None)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.33      0.33      0.33         3
       True       0.33      0.33      0.33         3

avg / total       0.33      0.33      0.33         6



Confusion matrix:
[[1 2]
 [2 1]]



Classifying 1 th split of fair apps with unfair app
-------------------------------------------------------------------------------


Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=distance)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.75      1.00      0.86         3
       True       1.00      0.67      0.80         3

avg / total       0.88      0.83      0.83         6



Confusion matrix:
[[3 0]
 [1 2]]


Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=uniform)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.60      1.00      0.75         3
       True       1.00      0.33      0.50         3

avg / total       0.80      0.67      0.62         6



Confusion matrix:
[[3 0]
 [2 1]]


Classifier: 
 GaussianNB()
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.50      0.67      0.57         3
       True       0.50      0.33      0.40         3

avg / total       0.50      0.50      0.49         6



Confusion matrix:
[[2 1]
 [2 1]]


Classifier: 
 DecisionTreeClassifier(compute_importances=None, criterion=gini,
            max_depth=None, max_features=None, min_density=None,
            min_samples_leaf=1, min_samples_split=2, random_state=None,
            splitter=best)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.60      1.00      0.75         3
       True       1.00      0.33      0.50         3

avg / total       0.80      0.67      0.62         6



Confusion matrix:
[[3 0]
 [2 1]]


Classifier: 
 SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, degree=3, gamma=0.0,
  kernel=rbf, max_iter=-1, probability=False, random_state=None,
  shrinking=True, tol=0.001, verbose=False)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.50      0.33      0.40         3
       True       0.50      0.67      0.57         3

avg / total       0.50      0.50      0.49         6



Confusion matrix:
[[1 2]
 [1 2]]


Classifier: 
 NuSVC(cache_size=200, coef0=0.0, degree=3, gamma=0.0, kernel=rbf, max_iter=-1,
   nu=0.5, probability=False, random_state=None, shrinking=True, tol=0.001,
   verbose=False)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.60      1.00      0.75         3
       True       1.00      0.33      0.50         3

avg / total       0.80      0.67      0.62         6



Confusion matrix:
[[3 0]
 [2 1]]


Classifier: 
 AdaBoostClassifier(algorithm=SAMME,
          base_estimator=DecisionTreeClassifier(compute_importances=None, criterion=gini, max_depth=1,
            max_features=None, min_density=None, min_samples_leaf=1,
            min_samples_split=2, random_state=None, splitter=best),
          base_estimator__compute_importances=None,
          base_estimator__criterion=gini, base_estimator__max_depth=1,
          base_estimator__max_features=None,
          base_estimator__min_density=None,
          base_estimator__min_samples_leaf=1,
          base_estimator__min_samples_split=2,
          base_estimator__random_state=None, base_estimator__splitter=best,
          learning_rate=1.0, n_estimators=200, random_state=None)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.25      0.33      0.29         3
       True       0.00      0.00      0.00         3

avg / total       0.12      0.17      0.14         6



Confusion matrix:
[[1 2]
 [3 0]]



Classifying 2 th split of fair apps with unfair app
-------------------------------------------------------------------------------


Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=distance)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.67      1.00      0.80         2
       True       1.00      0.75      0.86         4

avg / total       0.89      0.83      0.84         6



Confusion matrix:
[[2 0]
 [1 3]]


Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=uniform)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.67      1.00      0.80         2
       True       1.00      0.75      0.86         4

avg / total       0.89      0.83      0.84         6



Confusion matrix:
[[2 0]
 [1 3]]


Classifier: 
 GaussianNB()
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.50      1.00      0.67         2
       True       1.00      0.50      0.67         4

avg / total       0.83      0.67      0.67         6



Confusion matrix:
[[2 0]
 [2 2]]


Classifier: 
 DecisionTreeClassifier(compute_importances=None, criterion=gini,
            max_depth=None, max_features=None, min_density=None,
            min_samples_leaf=1, min_samples_split=2, random_state=None,
            splitter=best)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.00      0.00      0.00         2
       True       0.60      0.75      0.67         4

avg / total       0.40      0.50      0.44         6



Confusion matrix:
[[0 2]
 [1 3]]


Classifier: 
 SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, degree=3, gamma=0.0,
  kernel=rbf, max_iter=-1, probability=False, random_state=None,
  shrinking=True, tol=0.001, verbose=False)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.33      1.00      0.50         2
       True       0.00      0.00      0.00         4

avg / total       0.11      0.33      0.17         6



Confusion matrix:
[[2 0]
 [4 0]]


Classifier: 
 NuSVC(cache_size=200, coef0=0.0, degree=3, gamma=0.0, kernel=rbf, max_iter=-1,
   nu=0.5, probability=False, random_state=None, shrinking=True, tol=0.001,
   verbose=False)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       1.00      0.50      0.67         2
       True       0.80      1.00      0.89         4

avg / total       0.87      0.83      0.81         6



Confusion matrix:
[[1 1]
 [0 4]]


Classifier: 
 AdaBoostClassifier(algorithm=SAMME,
          base_estimator=DecisionTreeClassifier(compute_importances=None, criterion=gini, max_depth=1,
            max_features=None, min_density=None, min_samples_leaf=1,
            min_samples_split=2, random_state=None, splitter=best),
          base_estimator__compute_importances=None,
          base_estimator__criterion=gini, base_estimator__max_depth=1,
          base_estimator__max_features=None,
          base_estimator__min_density=None,
          base_estimator__min_samples_leaf=1,
          base_estimator__min_samples_split=2,
          base_estimator__random_state=None, base_estimator__splitter=best,
          learning_rate=1.0, n_estimators=200, random_state=None)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.00      0.00      0.00         2
       True       0.60      0.75      0.67         4

avg / total       0.40      0.50      0.44         6



Confusion matrix:
[[0 2]
 [1 3]]



Classifying 3 th split of fair apps with unfair app
-------------------------------------------------------------------------------


Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=distance)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.20      0.50      0.29         2
       True       0.00      0.00      0.00         4

avg / total       0.07      0.17      0.10         6



Confusion matrix:
[[1 1]
 [4 0]]


Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=uniform)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.20      0.50      0.29         2
       True       0.00      0.00      0.00         4

avg / total       0.07      0.17      0.10         6



Confusion matrix:
[[1 1]
 [4 0]]


Classifier: 
 GaussianNB()
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.40      1.00      0.57         2
       True       1.00      0.25      0.40         4

avg / total       0.80      0.50      0.46         6



Confusion matrix:
[[2 0]
 [3 1]]


Classifier: 
 DecisionTreeClassifier(compute_importances=None, criterion=gini,
            max_depth=None, max_features=None, min_density=None,
            min_samples_leaf=1, min_samples_split=2, random_state=None,
            splitter=best)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.00      0.00      0.00         2
       True       0.50      0.50      0.50         4

avg / total       0.33      0.33      0.33         6



Confusion matrix:
[[0 2]
 [2 2]]


Classifier: 
 SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, degree=3, gamma=0.0,
  kernel=rbf, max_iter=-1, probability=False, random_state=None,
  shrinking=True, tol=0.001, verbose=False)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.33      1.00      0.50         2
       True       0.00      0.00      0.00         4

avg / total       0.11      0.33      0.17         6



Confusion matrix:
[[2 0]
 [4 0]]


Classifier: 
 NuSVC(cache_size=200, coef0=0.0, degree=3, gamma=0.0, kernel=rbf, max_iter=-1,
   nu=0.5, probability=False, random_state=None, shrinking=True, tol=0.001,
   verbose=False)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.33      1.00      0.50         2
       True       0.00      0.00      0.00         4

avg / total       0.11      0.33      0.17         6



Confusion matrix:
[[2 0]
 [4 0]]


Classifier: 
 AdaBoostClassifier(algorithm=SAMME,
          base_estimator=DecisionTreeClassifier(compute_importances=None, criterion=gini, max_depth=1,
            max_features=None, min_density=None, min_samples_leaf=1,
            min_samples_split=2, random_state=None, splitter=best),
          base_estimator__compute_importances=None,
          base_estimator__criterion=gini, base_estimator__max_depth=1,
          base_estimator__max_features=None,
          base_estimator__min_density=None,
          base_estimator__min_samples_leaf=1,
          base_estimator__min_samples_split=2,
          base_estimator__random_state=None, base_estimator__splitter=best,
          learning_rate=1.0, n_estimators=200, random_state=None)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.00      0.00      0.00         2
       True       0.50      0.50      0.50         4

avg / total       0.33      0.33      0.33         6



Confusion matrix:
[[0 2]
 [2 2]]



Classifying 4 th split of fair apps with unfair app
-------------------------------------------------------------------------------


Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=distance)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.60      1.00      0.75         3
       True       1.00      0.33      0.50         3

avg / total       0.80      0.67      0.62         6



Confusion matrix:
[[3 0]
 [2 1]]


Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=uniform)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.75      1.00      0.86         3
       True       1.00      0.67      0.80         3

avg / total       0.88      0.83      0.83         6



Confusion matrix:
[[3 0]
 [1 2]]


Classifier: 
 GaussianNB()
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.60      1.00      0.75         3
       True       1.00      0.33      0.50         3

avg / total       0.80      0.67      0.62         6



Confusion matrix:
[[3 0]
 [2 1]]


Classifier: 
 DecisionTreeClassifier(compute_importances=None, criterion=gini,
            max_depth=None, max_features=None, min_density=None,
            min_samples_leaf=1, min_samples_split=2, random_state=None,
            splitter=best)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.50      0.67      0.57         3
       True       0.50      0.33      0.40         3

avg / total       0.50      0.50      0.49         6



Confusion matrix:
[[2 1]
 [2 1]]


Classifier: 
 SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, degree=3, gamma=0.0,
  kernel=rbf, max_iter=-1, probability=False, random_state=None,
  shrinking=True, tol=0.001, verbose=False)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.75      1.00      0.86         3
       True       1.00      0.67      0.80         3

avg / total       0.88      0.83      0.83         6



Confusion matrix:
[[3 0]
 [1 2]]


Classifier: 
 NuSVC(cache_size=200, coef0=0.0, degree=3, gamma=0.0, kernel=rbf, max_iter=-1,
   nu=0.5, probability=False, random_state=None, shrinking=True, tol=0.001,
   verbose=False)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.60      1.00      0.75         3
       True       1.00      0.33      0.50         3

avg / total       0.80      0.67      0.62         6



Confusion matrix:
[[3 0]
 [2 1]]


Classifier: 
 AdaBoostClassifier(algorithm=SAMME,
          base_estimator=DecisionTreeClassifier(compute_importances=None, criterion=gini, max_depth=1,
            max_features=None, min_density=None, min_samples_leaf=1,
            min_samples_split=2, random_state=None, splitter=best),
          base_estimator__compute_importances=None,
          base_estimator__criterion=gini, base_estimator__max_depth=1,
          base_estimator__max_features=None,
          base_estimator__min_density=None,
          base_estimator__min_samples_leaf=1,
          base_estimator__min_samples_split=2,
          base_estimator__random_state=None, base_estimator__splitter=best,
          learning_rate=1.0, n_estimators=200, random_state=None)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.60      1.00      0.75         3
       True       1.00      0.33      0.50         3

avg / total       0.80      0.67      0.62         6



Confusion matrix:
[[3 0]
 [2 1]]



Classifying 5 th split of fair apps with unfair app
-------------------------------------------------------------------------------


Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=distance)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       1.00      1.00      1.00         3
       True       1.00      1.00      1.00         3

avg / total       1.00      1.00      1.00         6



Confusion matrix:
[[3 0]
 [0 3]]


Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=uniform)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       1.00      1.00      1.00         3
       True       1.00      1.00      1.00         3

avg / total       1.00      1.00      1.00         6



Confusion matrix:
[[3 0]
 [0 3]]


Classifier: 
 GaussianNB()
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.50      0.67      0.57         3
       True       0.50      0.33      0.40         3

avg / total       0.50      0.50      0.49         6



Confusion matrix:
[[2 1]
 [2 1]]


Classifier: 
 DecisionTreeClassifier(compute_importances=None, criterion=gini,
            max_depth=None, max_features=None, min_density=None,
            min_samples_leaf=1, min_samples_split=2, random_state=None,
            splitter=best)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.00      0.00      0.00         3
       True       0.40      0.67      0.50         3

avg / total       0.20      0.33      0.25         6



Confusion matrix:
[[0 3]
 [1 2]]


Classifier: 
 SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, degree=3, gamma=0.0,
  kernel=rbf, max_iter=-1, probability=False, random_state=None,
  shrinking=True, tol=0.001, verbose=False)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       1.00      1.00      1.00         3
       True       1.00      1.00      1.00         3

avg / total       1.00      1.00      1.00         6



Confusion matrix:
[[3 0]
 [0 3]]


Classifier: 
 NuSVC(cache_size=200, coef0=0.0, degree=3, gamma=0.0, kernel=rbf, max_iter=-1,
   nu=0.5, probability=False, random_state=None, shrinking=True, tol=0.001,
   verbose=False)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.75      1.00      0.86         3
       True       1.00      0.67      0.80         3

avg / total       0.88      0.83      0.83         6



Confusion matrix:
[[3 0]
 [1 2]]


Classifier: 
 AdaBoostClassifier(algorithm=SAMME,
          base_estimator=DecisionTreeClassifier(compute_importances=None, criterion=gini, max_depth=1,
            max_features=None, min_density=None, min_samples_leaf=1,
            min_samples_split=2, random_state=None, splitter=best),
          base_estimator__compute_importances=None,
          base_estimator__criterion=gini, base_estimator__max_depth=1,
          base_estimator__max_features=None,
          base_estimator__min_density=None,
          base_estimator__min_samples_leaf=1,
          base_estimator__min_samples_split=2,
          base_estimator__random_state=None, base_estimator__splitter=best,
          learning_rate=1.0, n_estimators=200, random_state=None)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       1.00      0.67      0.80         3
       True       0.75      1.00      0.86         3

avg / total       0.88      0.83      0.83         6



Confusion matrix:
[[2 1]
 [0 3]]



Classifying 6 th split of fair apps with unfair app
-------------------------------------------------------------------------------


Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=distance)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.75      1.00      0.86         3
       True       1.00      0.67      0.80         3

avg / total       0.88      0.83      0.83         6



Confusion matrix:
[[3 0]
 [1 2]]


Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=uniform)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.75      1.00      0.86         3
       True       1.00      0.67      0.80         3

avg / total       0.88      0.83      0.83         6



Confusion matrix:
[[3 0]
 [1 2]]


Classifier: 
 GaussianNB()
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.67      0.67      0.67         3
       True       0.67      0.67      0.67         3

avg / total       0.67      0.67      0.67         6



Confusion matrix:
[[2 1]
 [1 2]]


Classifier: 
 DecisionTreeClassifier(compute_importances=None, criterion=gini,
            max_depth=None, max_features=None, min_density=None,
            min_samples_leaf=1, min_samples_split=2, random_state=None,
            splitter=best)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.67      0.67      0.67         3
       True       0.67      0.67      0.67         3

avg / total       0.67      0.67      0.67         6



Confusion matrix:
[[2 1]
 [1 2]]


Classifier: 
 SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, degree=3, gamma=0.0,
  kernel=rbf, max_iter=-1, probability=False, random_state=None,
  shrinking=True, tol=0.001, verbose=False)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.50      0.67      0.57         3
       True       0.50      0.33      0.40         3

avg / total       0.50      0.50      0.49         6



Confusion matrix:
[[2 1]
 [2 1]]


Classifier: 
 NuSVC(cache_size=200, coef0=0.0, degree=3, gamma=0.0, kernel=rbf, max_iter=-1,
   nu=0.5, probability=False, random_state=None, shrinking=True, tol=0.001,
   verbose=False)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.67      0.67      0.67         3
       True       0.67      0.67      0.67         3

avg / total       0.67      0.67      0.67         6



Confusion matrix:
[[2 1]
 [1 2]]


Classifier: 
 AdaBoostClassifier(algorithm=SAMME,
          base_estimator=DecisionTreeClassifier(compute_importances=None, criterion=gini, max_depth=1,
            max_features=None, min_density=None, min_samples_leaf=1,
            min_samples_split=2, random_state=None, splitter=best),
          base_estimator__compute_importances=None,
          base_estimator__criterion=gini, base_estimator__max_depth=1,
          base_estimator__max_features=None,
          base_estimator__min_density=None,
          base_estimator__min_samples_leaf=1,
          base_estimator__min_samples_split=2,
          base_estimator__random_state=None, base_estimator__splitter=best,
          learning_rate=1.0, n_estimators=200, random_state=None)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.33      0.33      0.33         3
       True       0.33      0.33      0.33         3

avg / total       0.33      0.33      0.33         6



Confusion matrix:
[[1 2]
 [2 1]]



Classifying 7 th split of fair apps with unfair app
-------------------------------------------------------------------------------


Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=distance)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.40      0.67      0.50         3
       True       0.00      0.00      0.00         3

avg / total       0.20      0.33      0.25         6



Confusion matrix:
[[2 1]
 [3 0]]


Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=uniform)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.50      1.00      0.67         3
       True       0.00      0.00      0.00         3

avg / total       0.25      0.50      0.33         6



Confusion matrix:
[[3 0]
 [3 0]]


Classifier: 
 GaussianNB()
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.50      1.00      0.67         3
       True       0.00      0.00      0.00         3

avg / total       0.25      0.50      0.33         6



Confusion matrix:
[[3 0]
 [3 0]]


Classifier: 
 DecisionTreeClassifier(compute_importances=None, criterion=gini,
            max_depth=None, max_features=None, min_density=None,
            min_samples_leaf=1, min_samples_split=2, random_state=None,
            splitter=best)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       1.00      1.00      1.00         3
       True       1.00      1.00      1.00         3

avg / total       1.00      1.00      1.00         6



Confusion matrix:
[[3 0]
 [0 3]]


Classifier: 
 SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, degree=3, gamma=0.0,
  kernel=rbf, max_iter=-1, probability=False, random_state=None,
  shrinking=True, tol=0.001, verbose=False)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.50      1.00      0.67         3
       True       0.00      0.00      0.00         3

avg / total       0.25      0.50      0.33         6



Confusion matrix:
[[3 0]
 [3 0]]


Classifier: 
 NuSVC(cache_size=200, coef0=0.0, degree=3, gamma=0.0, kernel=rbf, max_iter=-1,
   nu=0.5, probability=False, random_state=None, shrinking=True, tol=0.001,
   verbose=False)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.40      0.67      0.50         3
       True       0.00      0.00      0.00         3

avg / total       0.20      0.33      0.25         6



Confusion matrix:
[[2 1]
 [3 0]]


Classifier: 
 AdaBoostClassifier(algorithm=SAMME,
          base_estimator=DecisionTreeClassifier(compute_importances=None, criterion=gini, max_depth=1,
            max_features=None, min_density=None, min_samples_leaf=1,
            min_samples_split=2, random_state=None, splitter=best),
          base_estimator__compute_importances=None,
          base_estimator__criterion=gini, base_estimator__max_depth=1,
          base_estimator__max_features=None,
          base_estimator__min_density=None,
          base_estimator__min_samples_leaf=1,
          base_estimator__min_samples_split=2,
          base_estimator__random_state=None, base_estimator__splitter=best,
          learning_rate=1.0, n_estimators=200, random_state=None)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.75      1.00      0.86         3
       True       1.00      0.67      0.80         3

avg / total       0.88      0.83      0.83         6



Confusion matrix:
[[3 0]
 [1 2]]



Classifying 8 th split of fair apps with unfair app
-------------------------------------------------------------------------------


Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=distance)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.50      0.67      0.57         3
       True       0.50      0.33      0.40         3

avg / total       0.50      0.50      0.49         6



Confusion matrix:
[[2 1]
 [2 1]]


Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=uniform)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.60      1.00      0.75         3
       True       1.00      0.33      0.50         3

avg / total       0.80      0.67      0.62         6



Confusion matrix:
[[3 0]
 [2 1]]


Classifier: 
 GaussianNB()
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.60      1.00      0.75         3
       True       1.00      0.33      0.50         3

avg / total       0.80      0.67      0.62         6



Confusion matrix:
[[3 0]
 [2 1]]


Classifier: 
 DecisionTreeClassifier(compute_importances=None, criterion=gini,
            max_depth=None, max_features=None, min_density=None,
            min_samples_leaf=1, min_samples_split=2, random_state=None,
            splitter=best)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.75      1.00      0.86         3
       True       1.00      0.67      0.80         3

avg / total       0.88      0.83      0.83         6



Confusion matrix:
[[3 0]
 [1 2]]


Classifier: 
 SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, degree=3, gamma=0.0,
  kernel=rbf, max_iter=-1, probability=False, random_state=None,
  shrinking=True, tol=0.001, verbose=False)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.50      1.00      0.67         3
       True       0.00      0.00      0.00         3

avg / total       0.25      0.50      0.33         6



Confusion matrix:
[[3 0]
 [3 0]]


Classifier: 
 NuSVC(cache_size=200, coef0=0.0, degree=3, gamma=0.0, kernel=rbf, max_iter=-1,
   nu=0.5, probability=False, random_state=None, shrinking=True, tol=0.001,
   verbose=False)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.33      0.33      0.33         3
       True       0.33      0.33      0.33         3

avg / total       0.33      0.33      0.33         6



Confusion matrix:
[[1 2]
 [2 1]]


Classifier: 
 AdaBoostClassifier(algorithm=SAMME,
          base_estimator=DecisionTreeClassifier(compute_importances=None, criterion=gini, max_depth=1,
            max_features=None, min_density=None, min_samples_leaf=1,
            min_samples_split=2, random_state=None, splitter=best),
          base_estimator__compute_importances=None,
          base_estimator__criterion=gini, base_estimator__max_depth=1,
          base_estimator__max_features=None,
          base_estimator__min_density=None,
          base_estimator__min_samples_leaf=1,
          base_estimator__min_samples_split=2,
          base_estimator__random_state=None, base_estimator__splitter=best,
          learning_rate=1.0, n_estimators=200, random_state=None)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.50      0.67      0.57         3
       True       0.50      0.33      0.40         3

avg / total       0.50      0.50      0.49         6



Confusion matrix:
[[2 1]
 [2 1]]



Classifying 9 th split of fair apps with unfair app
-------------------------------------------------------------------------------


Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=distance)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.40      1.00      0.57         2
       True       1.00      0.25      0.40         4

avg / total       0.80      0.50      0.46         6



Confusion matrix:
[[2 0]
 [3 1]]


Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=uniform)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.33      1.00      0.50         2
       True       0.00      0.00      0.00         4

avg / total       0.11      0.33      0.17         6



Confusion matrix:
[[2 0]
 [4 0]]


Classifier: 
 GaussianNB()
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.40      1.00      0.57         2
       True       1.00      0.25      0.40         4

avg / total       0.80      0.50      0.46         6



Confusion matrix:
[[2 0]
 [3 1]]


Classifier: 
 DecisionTreeClassifier(compute_importances=None, criterion=gini,
            max_depth=None, max_features=None, min_density=None,
            min_samples_leaf=1, min_samples_split=2, random_state=None,
            splitter=best)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.40      1.00      0.57         2
       True       1.00      0.25      0.40         4

avg / total       0.80      0.50      0.46         6



Confusion matrix:
[[2 0]
 [3 1]]


Classifier: 
 SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, degree=3, gamma=0.0,
  kernel=rbf, max_iter=-1, probability=False, random_state=None,
  shrinking=True, tol=0.001, verbose=False)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.33      1.00      0.50         2
       True       0.00      0.00      0.00         4

avg / total       0.11      0.33      0.17         6



Confusion matrix:
[[2 0]
 [4 0]]


Classifier: 
 NuSVC(cache_size=200, coef0=0.0, degree=3, gamma=0.0, kernel=rbf, max_iter=-1,
   nu=0.5, probability=False, random_state=None, shrinking=True, tol=0.001,
   verbose=False)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.50      1.00      0.67         2
       True       1.00      0.50      0.67         4

avg / total       0.83      0.67      0.67         6



Confusion matrix:
[[2 0]
 [2 2]]


Classifier: 
 AdaBoostClassifier(algorithm=SAMME,
          base_estimator=DecisionTreeClassifier(compute_importances=None, criterion=gini, max_depth=1,
            max_features=None, min_density=None, min_samples_leaf=1,
            min_samples_split=2, random_state=None, splitter=best),
          base_estimator__compute_importances=None,
          base_estimator__criterion=gini, base_estimator__max_depth=1,
          base_estimator__max_features=None,
          base_estimator__min_density=None,
          base_estimator__min_samples_leaf=1,
          base_estimator__min_samples_split=2,
          base_estimator__random_state=None, base_estimator__splitter=best,
          learning_rate=1.0, n_estimators=200, random_state=None)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.40      1.00      0.57         2
       True       1.00      0.25      0.40         4

avg / total       0.80      0.50      0.46         6



Confusion matrix:
[[2 0]
 [3 1]]



Classifying 10 th split of fair apps with unfair app
-------------------------------------------------------------------------------


Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=distance)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.20      1.00      0.33         1
       True       1.00      0.20      0.33         5

avg / total       0.87      0.33      0.33         6



Confusion matrix:
[[1 0]
 [4 1]]


Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=uniform)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.20      1.00      0.33         1
       True       1.00      0.20      0.33         5

avg / total       0.87      0.33      0.33         6



Confusion matrix:
[[1 0]
 [4 1]]


Classifier: 
 GaussianNB()
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.20      1.00      0.33         1
       True       1.00      0.20      0.33         5

avg / total       0.87      0.33      0.33         6



Confusion matrix:
[[1 0]
 [4 1]]


Classifier: 
 DecisionTreeClassifier(compute_importances=None, criterion=gini,
            max_depth=None, max_features=None, min_density=None,
            min_samples_leaf=1, min_samples_split=2, random_state=None,
            splitter=best)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.50      1.00      0.67         1
       True       1.00      0.80      0.89         5

avg / total       0.92      0.83      0.85         6



Confusion matrix:
[[1 0]
 [1 4]]


Classifier: 
 SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, degree=3, gamma=0.0,
  kernel=rbf, max_iter=-1, probability=False, random_state=None,
  shrinking=True, tol=0.001, verbose=False)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.17      1.00      0.29         1
       True       0.00      0.00      0.00         5

avg / total       0.03      0.17      0.05         6



Confusion matrix:
[[1 0]
 [5 0]]


Classifier: 
 NuSVC(cache_size=200, coef0=0.0, degree=3, gamma=0.0, kernel=rbf, max_iter=-1,
   nu=0.5, probability=False, random_state=None, shrinking=True, tol=0.001,
   verbose=False)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.00      0.00      0.00         1
       True       0.75      0.60      0.67         5

avg / total       0.62      0.50      0.56         6



Confusion matrix:
[[0 1]
 [2 3]]


Classifier: 
 AdaBoostClassifier(algorithm=SAMME,
          base_estimator=DecisionTreeClassifier(compute_importances=None, criterion=gini, max_depth=1,
            max_features=None, min_density=None, min_samples_leaf=1,
            min_samples_split=2, random_state=None, splitter=best),
          base_estimator__compute_importances=None,
          base_estimator__criterion=gini, base_estimator__max_depth=1,
          base_estimator__max_features=None,
          base_estimator__min_density=None,
          base_estimator__min_samples_leaf=1,
          base_estimator__min_samples_split=2,
          base_estimator__random_state=None, base_estimator__splitter=best,
          learning_rate=1.0, n_estimators=200, random_state=None)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.00      0.00      0.00         1
       True       0.80      0.80      0.80         5

avg / total       0.67      0.67      0.67         6



Confusion matrix:
[[0 1]
 [1 4]]



Classifying 11 th split of fair apps with unfair app
-------------------------------------------------------------------------------


Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=distance)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.60      1.00      0.75         3
       True       1.00      0.33      0.50         3

avg / total       0.80      0.67      0.62         6



Confusion matrix:
[[3 0]
 [2 1]]


Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=uniform)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.75      1.00      0.86         3
       True       1.00      0.67      0.80         3

avg / total       0.88      0.83      0.83         6



Confusion matrix:
[[3 0]
 [1 2]]


Classifier: 
 GaussianNB()
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.60      1.00      0.75         3
       True       1.00      0.33      0.50         3

avg / total       0.80      0.67      0.62         6



Confusion matrix:
[[3 0]
 [2 1]]


Classifier: 
 DecisionTreeClassifier(compute_importances=None, criterion=gini,
            max_depth=None, max_features=None, min_density=None,
            min_samples_leaf=1, min_samples_split=2, random_state=None,
            splitter=best)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.50      0.67      0.57         3
       True       0.50      0.33      0.40         3

avg / total       0.50      0.50      0.49         6



Confusion matrix:
[[2 1]
 [2 1]]


Classifier: 
 SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, degree=3, gamma=0.0,
  kernel=rbf, max_iter=-1, probability=False, random_state=None,
  shrinking=True, tol=0.001, verbose=False)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.60      1.00      0.75         3
       True       1.00      0.33      0.50         3

avg / total       0.80      0.67      0.62         6



Confusion matrix:
[[3 0]
 [2 1]]


Classifier: 
 NuSVC(cache_size=200, coef0=0.0, degree=3, gamma=0.0, kernel=rbf, max_iter=-1,
   nu=0.5, probability=False, random_state=None, shrinking=True, tol=0.001,
   verbose=False)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.60      1.00      0.75         3
       True       1.00      0.33      0.50         3

avg / total       0.80      0.67      0.62         6



Confusion matrix:
[[3 0]
 [2 1]]


Classifier: 
 AdaBoostClassifier(algorithm=SAMME,
          base_estimator=DecisionTreeClassifier(compute_importances=None, criterion=gini, max_depth=1,
            max_features=None, min_density=None, min_samples_leaf=1,
            min_samples_split=2, random_state=None, splitter=best),
          base_estimator__compute_importances=None,
          base_estimator__criterion=gini, base_estimator__max_depth=1,
          base_estimator__max_features=None,
          base_estimator__min_density=None,
          base_estimator__min_samples_leaf=1,
          base_estimator__min_samples_split=2,
          base_estimator__random_state=None, base_estimator__splitter=best,
          learning_rate=1.0, n_estimators=200, random_state=None)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.33      0.33      0.33         3
       True       0.33      0.33      0.33         3

avg / total       0.33      0.33      0.33         6



Confusion matrix:
[[1 2]
 [2 1]]



Classifying 12 th split of fair apps with unfair app
-------------------------------------------------------------------------------


Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=distance)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.50      0.33      0.40         3
       True       0.50      0.67      0.57         3

avg / total       0.50      0.50      0.49         6



Confusion matrix:
[[1 2]
 [1 2]]


Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=uniform)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.33      0.33      0.33         3
       True       0.33      0.33      0.33         3

avg / total       0.33      0.33      0.33         6



Confusion matrix:
[[1 2]
 [2 1]]


Classifier: 
 GaussianNB()
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.75      1.00      0.86         3
       True       1.00      0.67      0.80         3

avg / total       0.88      0.83      0.83         6



Confusion matrix:
[[3 0]
 [1 2]]


Classifier: 
 DecisionTreeClassifier(compute_importances=None, criterion=gini,
            max_depth=None, max_features=None, min_density=None,
            min_samples_leaf=1, min_samples_split=2, random_state=None,
            splitter=best)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.60      1.00      0.75         3
       True       1.00      0.33      0.50         3

avg / total       0.80      0.67      0.62         6



Confusion matrix:
[[3 0]
 [2 1]]


Classifier: 
 SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, degree=3, gamma=0.0,
  kernel=rbf, max_iter=-1, probability=False, random_state=None,
  shrinking=True, tol=0.001, verbose=False)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.67      0.67      0.67         3
       True       0.67      0.67      0.67         3

avg / total       0.67      0.67      0.67         6



Confusion matrix:
[[2 1]
 [1 2]]


Classifier: 
 NuSVC(cache_size=200, coef0=0.0, degree=3, gamma=0.0, kernel=rbf, max_iter=-1,
   nu=0.5, probability=False, random_state=None, shrinking=True, tol=0.001,
   verbose=False)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       1.00      0.33      0.50         3
       True       0.60      1.00      0.75         3

avg / total       0.80      0.67      0.62         6



Confusion matrix:
[[1 2]
 [0 3]]


Classifier: 
 AdaBoostClassifier(algorithm=SAMME,
          base_estimator=DecisionTreeClassifier(compute_importances=None, criterion=gini, max_depth=1,
            max_features=None, min_density=None, min_samples_leaf=1,
            min_samples_split=2, random_state=None, splitter=best),
          base_estimator__compute_importances=None,
          base_estimator__criterion=gini, base_estimator__max_depth=1,
          base_estimator__max_features=None,
          base_estimator__min_density=None,
          base_estimator__min_samples_leaf=1,
          base_estimator__min_samples_split=2,
          base_estimator__random_state=None, base_estimator__splitter=best,
          learning_rate=1.0, n_estimators=200, random_state=None)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       1.00      0.67      0.80         3
       True       0.75      1.00      0.86         3

avg / total       0.88      0.83      0.83         6



Confusion matrix:
[[2 1]
 [0 3]]



