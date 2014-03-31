Classifying 0 th split of fair apps with unfair app
-------------------------------------------------------------------------------


Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=distance)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.50      0.67      0.57         3
       True       0.83      0.71      0.77         7

avg / total       0.73      0.70      0.71        10



Confusion matrix:
[[2 1]
 [2 5]]


Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=uniform)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.50      0.67      0.57         3
       True       0.83      0.71      0.77         7

avg / total       0.73      0.70      0.71        10



Confusion matrix:
[[2 1]
 [2 5]]


Classifier: 
 GaussianNB()
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.60      1.00      0.75         3
       True       1.00      0.71      0.83         7

avg / total       0.88      0.80      0.81        10



Confusion matrix:
[[3 0]
 [2 5]]


Classifier: 
 DecisionTreeClassifier(compute_importances=None, criterion=gini,
            max_depth=None, max_features=None, min_density=None,
            min_samples_leaf=1, min_samples_split=2, random_state=None,
            splitter=best)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.40      0.67      0.50         3
       True       0.80      0.57      0.67         7

avg / total       0.68      0.60      0.62        10



Confusion matrix:
[[2 1]
 [3 4]]


Classifier: 
 SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, degree=3, gamma=0.0,
  kernel=rbf, max_iter=-1, probability=False, random_state=None,
  shrinking=True, tol=0.001, verbose=False)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.30      1.00      0.46         3
       True       0.00      0.00      0.00         7

avg / total       0.09      0.30      0.14        10



Confusion matrix:
[[3 0]
 [7 0]]


Classifier: 
 NuSVC(cache_size=200, coef0=0.0, degree=3, gamma=0.0, kernel=rbf, max_iter=-1,
   nu=0.5, probability=False, random_state=None, shrinking=True, tol=0.001,
   verbose=False)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.50      0.67      0.57         3
       True       0.83      0.71      0.77         7

avg / total       0.73      0.70      0.71        10



Confusion matrix:
[[2 1]
 [2 5]]


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

      False       0.43      1.00      0.60         3
       True       1.00      0.43      0.60         7

avg / total       0.83      0.60      0.60        10



Confusion matrix:
[[3 0]
 [4 3]]



Classifying 1 th split of fair apps with unfair app
-------------------------------------------------------------------------------


Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=distance)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.83      0.83      0.83         6
       True       0.75      0.75      0.75         4

avg / total       0.80      0.80      0.80        10



Confusion matrix:
[[5 1]
 [1 3]]


Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=uniform)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.83      0.83      0.83         6
       True       0.75      0.75      0.75         4

avg / total       0.80      0.80      0.80        10



Confusion matrix:
[[5 1]
 [1 3]]


Classifier: 
 GaussianNB()
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.75      1.00      0.86         6
       True       1.00      0.50      0.67         4

avg / total       0.85      0.80      0.78        10



Confusion matrix:
[[6 0]
 [2 2]]


Classifier: 
 DecisionTreeClassifier(compute_importances=None, criterion=gini,
            max_depth=None, max_features=None, min_density=None,
            min_samples_leaf=1, min_samples_split=2, random_state=None,
            splitter=best)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.75      0.50      0.60         6
       True       0.50      0.75      0.60         4

avg / total       0.65      0.60      0.60        10



Confusion matrix:
[[3 3]
 [1 3]]


Classifier: 
 SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, degree=3, gamma=0.0,
  kernel=rbf, max_iter=-1, probability=False, random_state=None,
  shrinking=True, tol=0.001, verbose=False)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.00      0.00      0.00         6
       True       0.40      1.00      0.57         4

avg / total       0.16      0.40      0.23        10



Confusion matrix:
[[0 6]
 [0 4]]


Classifier: 
 NuSVC(cache_size=200, coef0=0.0, degree=3, gamma=0.0, kernel=rbf, max_iter=-1,
   nu=0.5, probability=False, random_state=None, shrinking=True, tol=0.001,
   verbose=False)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.83      0.83      0.83         6
       True       0.75      0.75      0.75         4

avg / total       0.80      0.80      0.80        10



Confusion matrix:
[[5 1]
 [1 3]]


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

      False       0.50      0.67      0.57         6
       True       0.00      0.00      0.00         4

avg / total       0.30      0.40      0.34        10



Confusion matrix:
[[4 2]
 [4 0]]



Classifying 2 th split of fair apps with unfair app
-------------------------------------------------------------------------------


Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=distance)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.57      0.80      0.67         5
       True       0.67      0.40      0.50         5

avg / total       0.62      0.60      0.58        10



Confusion matrix:
[[4 1]
 [3 2]]


Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=uniform)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.57      0.80      0.67         5
       True       0.67      0.40      0.50         5

avg / total       0.62      0.60      0.58        10



Confusion matrix:
[[4 1]
 [3 2]]


Classifier: 
 GaussianNB()
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.50      1.00      0.67         5
       True       0.00      0.00      0.00         5

avg / total       0.25      0.50      0.33        10



Confusion matrix:
[[5 0]
 [5 0]]


Classifier: 
 DecisionTreeClassifier(compute_importances=None, criterion=gini,
            max_depth=None, max_features=None, min_density=None,
            min_samples_leaf=1, min_samples_split=2, random_state=None,
            splitter=best)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.75      0.60      0.67         5
       True       0.67      0.80      0.73         5

avg / total       0.71      0.70      0.70        10



Confusion matrix:
[[3 2]
 [1 4]]


Classifier: 
 SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, degree=3, gamma=0.0,
  kernel=rbf, max_iter=-1, probability=False, random_state=None,
  shrinking=True, tol=0.001, verbose=False)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.67      0.40      0.50         5
       True       0.57      0.80      0.67         5

avg / total       0.62      0.60      0.58        10



Confusion matrix:
[[2 3]
 [1 4]]


Classifier: 
 NuSVC(cache_size=200, coef0=0.0, degree=3, gamma=0.0, kernel=rbf, max_iter=-1,
   nu=0.5, probability=False, random_state=None, shrinking=True, tol=0.001,
   verbose=False)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.67      0.80      0.73         5
       True       0.75      0.60      0.67         5

avg / total       0.71      0.70      0.70        10



Confusion matrix:
[[4 1]
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

      False       0.67      0.40      0.50         5
       True       0.57      0.80      0.67         5

avg / total       0.62      0.60      0.58        10



Confusion matrix:
[[2 3]
 [1 4]]



Classifying 3 th split of fair apps with unfair app
-------------------------------------------------------------------------------


Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=distance)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.60      0.60      0.60         5
       True       0.60      0.60      0.60         5

avg / total       0.60      0.60      0.60        10



Confusion matrix:
[[3 2]
 [2 3]]


Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=uniform)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.67      0.80      0.73         5
       True       0.75      0.60      0.67         5

avg / total       0.71      0.70      0.70        10



Confusion matrix:
[[4 1]
 [2 3]]


Classifier: 
 GaussianNB()
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.56      1.00      0.71         5
       True       1.00      0.20      0.33         5

avg / total       0.78      0.60      0.52        10



Confusion matrix:
[[5 0]
 [4 1]]


Classifier: 
 DecisionTreeClassifier(compute_importances=None, criterion=gini,
            max_depth=None, max_features=None, min_density=None,
            min_samples_leaf=1, min_samples_split=2, random_state=None,
            splitter=best)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.50      0.60      0.55         5
       True       0.50      0.40      0.44         5

avg / total       0.50      0.50      0.49        10



Confusion matrix:
[[3 2]
 [3 2]]


Classifier: 
 SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, degree=3, gamma=0.0,
  kernel=rbf, max_iter=-1, probability=False, random_state=None,
  shrinking=True, tol=0.001, verbose=False)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.50      0.60      0.55         5
       True       0.50      0.40      0.44         5

avg / total       0.50      0.50      0.49        10



Confusion matrix:
[[3 2]
 [3 2]]


Classifier: 
 NuSVC(cache_size=200, coef0=0.0, degree=3, gamma=0.0, kernel=rbf, max_iter=-1,
   nu=0.5, probability=False, random_state=None, shrinking=True, tol=0.001,
   verbose=False)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.67      0.80      0.73         5
       True       0.75      0.60      0.67         5

avg / total       0.71      0.70      0.70        10



Confusion matrix:
[[4 1]
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

      False       0.50      0.40      0.44         5
       True       0.50      0.60      0.55         5

avg / total       0.50      0.50      0.49        10



Confusion matrix:
[[2 3]
 [2 3]]



Classifying 4 th split of fair apps with unfair app
-------------------------------------------------------------------------------


Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=distance)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.38      1.00      0.55         3
       True       1.00      0.29      0.44         7

avg / total       0.81      0.50      0.47        10



Confusion matrix:
[[3 0]
 [5 2]]


Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=uniform)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.43      1.00      0.60         3
       True       1.00      0.43      0.60         7

avg / total       0.83      0.60      0.60        10



Confusion matrix:
[[3 0]
 [4 3]]


Classifier: 
 GaussianNB()
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.43      1.00      0.60         3
       True       1.00      0.43      0.60         7

avg / total       0.83      0.60      0.60        10



Confusion matrix:
[[3 0]
 [4 3]]


Classifier: 
 DecisionTreeClassifier(compute_importances=None, criterion=gini,
            max_depth=None, max_features=None, min_density=None,
            min_samples_leaf=1, min_samples_split=2, random_state=None,
            splitter=best)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.40      0.67      0.50         3
       True       0.80      0.57      0.67         7

avg / total       0.68      0.60      0.62        10



Confusion matrix:
[[2 1]
 [3 4]]


Classifier: 
 SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, degree=3, gamma=0.0,
  kernel=rbf, max_iter=-1, probability=False, random_state=None,
  shrinking=True, tol=0.001, verbose=False)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.30      1.00      0.46         3
       True       0.00      0.00      0.00         7

avg / total       0.09      0.30      0.14        10



Confusion matrix:
[[3 0]
 [7 0]]


Classifier: 
 NuSVC(cache_size=200, coef0=0.0, degree=3, gamma=0.0, kernel=rbf, max_iter=-1,
   nu=0.5, probability=False, random_state=None, shrinking=True, tol=0.001,
   verbose=False)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.43      1.00      0.60         3
       True       1.00      0.43      0.60         7

avg / total       0.83      0.60      0.60        10



Confusion matrix:
[[3 0]
 [4 3]]


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

      False       0.38      1.00      0.55         3
       True       1.00      0.29      0.44         7

avg / total       0.81      0.50      0.47        10



Confusion matrix:
[[3 0]
 [5 2]]



Classifying 5 th split of fair apps with unfair app
-------------------------------------------------------------------------------


Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=distance)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.83      0.71      0.77         7
       True       0.50      0.67      0.57         3

avg / total       0.73      0.70      0.71        10



Confusion matrix:
[[5 2]
 [1 2]]


Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=uniform)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.86      0.86      0.86         7
       True       0.67      0.67      0.67         3

avg / total       0.80      0.80      0.80        10



Confusion matrix:
[[6 1]
 [1 2]]


Classifier: 
 GaussianNB()
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.75      0.86      0.80         7
       True       0.50      0.33      0.40         3

avg / total       0.68      0.70      0.68        10



Confusion matrix:
[[6 1]
 [2 1]]


Classifier: 
 DecisionTreeClassifier(compute_importances=None, criterion=gini,
            max_depth=None, max_features=None, min_density=None,
            min_samples_leaf=1, min_samples_split=2, random_state=None,
            splitter=best)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       1.00      0.29      0.44         7
       True       0.38      1.00      0.55         3

avg / total       0.81      0.50      0.47        10



Confusion matrix:
[[2 5]
 [0 3]]


Classifier: 
 SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, degree=3, gamma=0.0,
  kernel=rbf, max_iter=-1, probability=False, random_state=None,
  shrinking=True, tol=0.001, verbose=False)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.00      0.00      0.00         7
       True       0.30      1.00      0.46         3

avg / total       0.09      0.30      0.14        10



Confusion matrix:
[[0 7]
 [0 3]]


Classifier: 
 NuSVC(cache_size=200, coef0=0.0, degree=3, gamma=0.0, kernel=rbf, max_iter=-1,
   nu=0.5, probability=False, random_state=None, shrinking=True, tol=0.001,
   verbose=False)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.75      0.43      0.55         7
       True       0.33      0.67      0.44         3

avg / total       0.62      0.50      0.52        10



Confusion matrix:
[[3 4]
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

      False       1.00      0.43      0.60         7
       True       0.43      1.00      0.60         3

avg / total       0.83      0.60      0.60        10



Confusion matrix:
[[3 4]
 [0 3]]



Classifying 6 th split of fair apps with unfair app
-------------------------------------------------------------------------------


Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=distance)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.57      1.00      0.73         4
       True       1.00      0.50      0.67         6

avg / total       0.83      0.70      0.69        10



Confusion matrix:
[[4 0]
 [3 3]]


Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=uniform)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.57      1.00      0.73         4
       True       1.00      0.50      0.67         6

avg / total       0.83      0.70      0.69        10



Confusion matrix:
[[4 0]
 [3 3]]


Classifier: 
 GaussianNB()
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.57      1.00      0.73         4
       True       1.00      0.50      0.67         6

avg / total       0.83      0.70      0.69        10



Confusion matrix:
[[4 0]
 [3 3]]


Classifier: 
 DecisionTreeClassifier(compute_importances=None, criterion=gini,
            max_depth=None, max_features=None, min_density=None,
            min_samples_leaf=1, min_samples_split=2, random_state=None,
            splitter=best)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.38      0.75      0.50         4
       True       0.50      0.17      0.25         6

avg / total       0.45      0.40      0.35        10



Confusion matrix:
[[3 1]
 [5 1]]


Classifier: 
 SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, degree=3, gamma=0.0,
  kernel=rbf, max_iter=-1, probability=False, random_state=None,
  shrinking=True, tol=0.001, verbose=False)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.40      1.00      0.57         4
       True       0.00      0.00      0.00         6

avg / total       0.16      0.40      0.23        10



Confusion matrix:
[[4 0]
 [6 0]]


Classifier: 
 NuSVC(cache_size=200, coef0=0.0, degree=3, gamma=0.0, kernel=rbf, max_iter=-1,
   nu=0.5, probability=False, random_state=None, shrinking=True, tol=0.001,
   verbose=False)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.60      0.75      0.67         4
       True       0.80      0.67      0.73         6

avg / total       0.72      0.70      0.70        10



Confusion matrix:
[[3 1]
 [2 4]]


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

      False       0.50      1.00      0.67         4
       True       1.00      0.33      0.50         6

avg / total       0.80      0.60      0.57        10



Confusion matrix:
[[4 0]
 [4 2]]



Classifying 7 th split of fair apps with unfair app
-------------------------------------------------------------------------------


Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=distance)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.43      0.60      0.50         5
       True       0.33      0.20      0.25         5

avg / total       0.38      0.40      0.38        10



Confusion matrix:
[[3 2]
 [4 1]]


Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=uniform)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.44      0.80      0.57         5
       True       0.00      0.00      0.00         5

avg / total       0.22      0.40      0.29        10



Confusion matrix:
[[4 1]
 [5 0]]


Classifier: 
 GaussianNB()
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.33      0.40      0.36         5
       True       0.25      0.20      0.22         5

avg / total       0.29      0.30      0.29        10



Confusion matrix:
[[2 3]
 [4 1]]


Classifier: 
 DecisionTreeClassifier(compute_importances=None, criterion=gini,
            max_depth=None, max_features=None, min_density=None,
            min_samples_leaf=1, min_samples_split=2, random_state=None,
            splitter=best)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.33      0.20      0.25         5
       True       0.43      0.60      0.50         5

avg / total       0.38      0.40      0.38        10



Confusion matrix:
[[1 4]
 [2 3]]


Classifier: 
 SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, degree=3, gamma=0.0,
  kernel=rbf, max_iter=-1, probability=False, random_state=None,
  shrinking=True, tol=0.001, verbose=False)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.50      0.80      0.62         5
       True       0.50      0.20      0.29         5

avg / total       0.50      0.50      0.45        10



Confusion matrix:
[[4 1]
 [4 1]]


Classifier: 
 NuSVC(cache_size=200, coef0=0.0, degree=3, gamma=0.0, kernel=rbf, max_iter=-1,
   nu=0.5, probability=False, random_state=None, shrinking=True, tol=0.001,
   verbose=False)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.33      0.40      0.36         5
       True       0.25      0.20      0.22         5

avg / total       0.29      0.30      0.29        10



Confusion matrix:
[[2 3]
 [4 1]]


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

      False       0.57      0.80      0.67         5
       True       0.67      0.40      0.50         5

avg / total       0.62      0.60      0.58        10



Confusion matrix:
[[4 1]
 [3 2]]



Classifying 8 th split of fair apps with unfair app
-------------------------------------------------------------------------------


Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=distance)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.71      0.71      0.71         7
       True       0.33      0.33      0.33         3

avg / total       0.60      0.60      0.60        10



Confusion matrix:
[[5 2]
 [2 1]]


Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=uniform)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.83      0.71      0.77         7
       True       0.50      0.67      0.57         3

avg / total       0.73      0.70      0.71        10



Confusion matrix:
[[5 2]
 [1 2]]


Classifier: 
 GaussianNB()
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.78      1.00      0.88         7
       True       1.00      0.33      0.50         3

avg / total       0.84      0.80      0.76        10



Confusion matrix:
[[7 0]
 [2 1]]


Classifier: 
 DecisionTreeClassifier(compute_importances=None, criterion=gini,
            max_depth=None, max_features=None, min_density=None,
            min_samples_leaf=1, min_samples_split=2, random_state=None,
            splitter=best)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.75      0.43      0.55         7
       True       0.33      0.67      0.44         3

avg / total       0.62      0.50      0.52        10



Confusion matrix:
[[3 4]
 [1 2]]


Classifier: 
 SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, degree=3, gamma=0.0,
  kernel=rbf, max_iter=-1, probability=False, random_state=None,
  shrinking=True, tol=0.001, verbose=False)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.00      0.00      0.00         7
       True       0.30      1.00      0.46         3

avg / total       0.09      0.30      0.14        10



Confusion matrix:
[[0 7]
 [0 3]]


Classifier: 
 NuSVC(cache_size=200, coef0=0.0, degree=3, gamma=0.0, kernel=rbf, max_iter=-1,
   nu=0.5, probability=False, random_state=None, shrinking=True, tol=0.001,
   verbose=False)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.86      0.86      0.86         7
       True       0.67      0.67      0.67         3

avg / total       0.80      0.80      0.80        10



Confusion matrix:
[[6 1]
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

      False       0.60      0.43      0.50         7
       True       0.20      0.33      0.25         3

avg / total       0.48      0.40      0.42        10



Confusion matrix:
[[3 4]
 [2 1]]



Classifying 9 th split of fair apps with unfair app
-------------------------------------------------------------------------------


Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=distance)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.83      0.71      0.77         7
       True       0.50      0.67      0.57         3

avg / total       0.73      0.70      0.71        10



Confusion matrix:
[[5 2]
 [1 2]]


Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=uniform)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.83      0.71      0.77         7
       True       0.50      0.67      0.57         3

avg / total       0.73      0.70      0.71        10



Confusion matrix:
[[5 2]
 [1 2]]


Classifier: 
 GaussianNB()
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.78      1.00      0.88         7
       True       1.00      0.33      0.50         3

avg / total       0.84      0.80      0.76        10



Confusion matrix:
[[7 0]
 [2 1]]


Classifier: 
 DecisionTreeClassifier(compute_importances=None, criterion=gini,
            max_depth=None, max_features=None, min_density=None,
            min_samples_leaf=1, min_samples_split=2, random_state=None,
            splitter=best)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.83      0.71      0.77         7
       True       0.50      0.67      0.57         3

avg / total       0.73      0.70      0.71        10



Confusion matrix:
[[5 2]
 [1 2]]


Classifier: 
 SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, degree=3, gamma=0.0,
  kernel=rbf, max_iter=-1, probability=False, random_state=None,
  shrinking=True, tol=0.001, verbose=False)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.00      0.00      0.00         7
       True       0.30      1.00      0.46         3

avg / total       0.09      0.30      0.14        10



Confusion matrix:
[[0 7]
 [0 3]]


Classifier: 
 NuSVC(cache_size=200, coef0=0.0, degree=3, gamma=0.0, kernel=rbf, max_iter=-1,
   nu=0.5, probability=False, random_state=None, shrinking=True, tol=0.001,
   verbose=False)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.83      0.71      0.77         7
       True       0.50      0.67      0.57         3

avg / total       0.73      0.70      0.71        10



Confusion matrix:
[[5 2]
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

      False       0.80      0.57      0.67         7
       True       0.40      0.67      0.50         3

avg / total       0.68      0.60      0.62        10



Confusion matrix:
[[4 3]
 [1 2]]



Classifying 10 th split of fair apps with unfair app
-------------------------------------------------------------------------------


Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=distance)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.57      0.80      0.67         5
       True       0.67      0.40      0.50         5

avg / total       0.62      0.60      0.58        10



Confusion matrix:
[[4 1]
 [3 2]]


Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=uniform)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.57      0.80      0.67         5
       True       0.67      0.40      0.50         5

avg / total       0.62      0.60      0.58        10



Confusion matrix:
[[4 1]
 [3 2]]


Classifier: 
 GaussianNB()
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.56      1.00      0.71         5
       True       1.00      0.20      0.33         5

avg / total       0.78      0.60      0.52        10



Confusion matrix:
[[5 0]
 [4 1]]


Classifier: 
 DecisionTreeClassifier(compute_importances=None, criterion=gini,
            max_depth=None, max_features=None, min_density=None,
            min_samples_leaf=1, min_samples_split=2, random_state=None,
            splitter=best)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.67      0.40      0.50         5
       True       0.57      0.80      0.67         5

avg / total       0.62      0.60      0.58        10



Confusion matrix:
[[2 3]
 [1 4]]


Classifier: 
 SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, degree=3, gamma=0.0,
  kernel=rbf, max_iter=-1, probability=False, random_state=None,
  shrinking=True, tol=0.001, verbose=False)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.67      0.80      0.73         5
       True       0.75      0.60      0.67         5

avg / total       0.71      0.70      0.70        10



Confusion matrix:
[[4 1]
 [2 3]]


Classifier: 
 NuSVC(cache_size=200, coef0=0.0, degree=3, gamma=0.0, kernel=rbf, max_iter=-1,
   nu=0.5, probability=False, random_state=None, shrinking=True, tol=0.001,
   verbose=False)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.50      0.60      0.55         5
       True       0.50      0.40      0.44         5

avg / total       0.50      0.50      0.49        10



Confusion matrix:
[[3 2]
 [3 2]]


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

      False       0.50      0.20      0.29         5
       True       0.50      0.80      0.62         5

avg / total       0.50      0.50      0.45        10



Confusion matrix:
[[1 4]
 [1 4]]



Classifying 11 th split of fair apps with unfair app
-------------------------------------------------------------------------------


Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=distance)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.60      0.75      0.67         4
       True       0.80      0.67      0.73         6

avg / total       0.72      0.70      0.70        10



Confusion matrix:
[[3 1]
 [2 4]]


Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=uniform)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.60      0.75      0.67         4
       True       0.80      0.67      0.73         6

avg / total       0.72      0.70      0.70        10



Confusion matrix:
[[3 1]
 [2 4]]


Classifier: 
 GaussianNB()
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.44      1.00      0.62         4
       True       1.00      0.17      0.29         6

avg / total       0.78      0.50      0.42        10



Confusion matrix:
[[4 0]
 [5 1]]


Classifier: 
 DecisionTreeClassifier(compute_importances=None, criterion=gini,
            max_depth=None, max_features=None, min_density=None,
            min_samples_leaf=1, min_samples_split=2, random_state=None,
            splitter=best)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.33      0.50      0.40         4
       True       0.50      0.33      0.40         6

avg / total       0.43      0.40      0.40        10



Confusion matrix:
[[2 2]
 [4 2]]


Classifier: 
 SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, degree=3, gamma=0.0,
  kernel=rbf, max_iter=-1, probability=False, random_state=None,
  shrinking=True, tol=0.001, verbose=False)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.40      1.00      0.57         4
       True       0.00      0.00      0.00         6

avg / total       0.16      0.40      0.23        10



Confusion matrix:
[[4 0]
 [6 0]]


Classifier: 
 NuSVC(cache_size=200, coef0=0.0, degree=3, gamma=0.0, kernel=rbf, max_iter=-1,
   nu=0.5, probability=False, random_state=None, shrinking=True, tol=0.001,
   verbose=False)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.43      0.75      0.55         4
       True       0.67      0.33      0.44         6

avg / total       0.57      0.50      0.48        10



Confusion matrix:
[[3 1]
 [4 2]]


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

      False       0.33      0.50      0.40         4
       True       0.50      0.33      0.40         6

avg / total       0.43      0.40      0.40        10



Confusion matrix:
[[2 2]
 [4 2]]



Classifying 12 th split of fair apps with unfair app
-------------------------------------------------------------------------------


Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=distance)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.50      0.50      0.50         4
       True       0.67      0.67      0.67         6

avg / total       0.60      0.60      0.60        10



Confusion matrix:
[[2 2]
 [2 4]]


Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=uniform)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.60      0.75      0.67         4
       True       0.80      0.67      0.73         6

avg / total       0.72      0.70      0.70        10



Confusion matrix:
[[3 1]
 [2 4]]


Classifier: 
 GaussianNB()
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.50      0.75      0.60         4
       True       0.75      0.50      0.60         6

avg / total       0.65      0.60      0.60        10



Confusion matrix:
[[3 1]
 [3 3]]


Classifier: 
 DecisionTreeClassifier(compute_importances=None, criterion=gini,
            max_depth=None, max_features=None, min_density=None,
            min_samples_leaf=1, min_samples_split=2, random_state=None,
            splitter=best)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.33      0.50      0.40         4
       True       0.50      0.33      0.40         6

avg / total       0.43      0.40      0.40        10



Confusion matrix:
[[2 2]
 [4 2]]


Classifier: 
 SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, degree=3, gamma=0.0,
  kernel=rbf, max_iter=-1, probability=False, random_state=None,
  shrinking=True, tol=0.001, verbose=False)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.40      1.00      0.57         4
       True       0.00      0.00      0.00         6

avg / total       0.16      0.40      0.23        10



Confusion matrix:
[[4 0]
 [6 0]]


Classifier: 
 NuSVC(cache_size=200, coef0=0.0, degree=3, gamma=0.0, kernel=rbf, max_iter=-1,
   nu=0.5, probability=False, random_state=None, shrinking=True, tol=0.001,
   verbose=False)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.67      1.00      0.80         4
       True       1.00      0.67      0.80         6

avg / total       0.87      0.80      0.80        10



Confusion matrix:
[[4 0]
 [2 4]]


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

      False       0.50      0.50      0.50         4
       True       0.67      0.67      0.67         6

avg / total       0.60      0.60      0.60        10



Confusion matrix:
[[2 2]
 [2 4]]



