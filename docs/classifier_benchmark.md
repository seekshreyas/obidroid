Classifying 0 th split of fair apps with unfair app
-------------------------------------------------------------------------------


Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=distance)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.50      0.40      0.44         5
       True       0.50      0.60      0.55         5

avg / total       0.50      0.50      0.49        10



Confusion matrix:
[[2 3]
 [2 3]]


Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=uniform)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.50      0.40      0.44         5
       True       0.50      0.60      0.55         5

avg / total       0.50      0.50      0.49        10



Confusion matrix:
[[2 3]
 [2 3]]


Classifier: 
 GaussianNB()
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

      False       0.60      0.60      0.60         5
       True       0.60      0.60      0.60         5

avg / total       0.60      0.60      0.60        10



Confusion matrix:
[[3 2]
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

      False       0.60      0.60      0.60         5
       True       0.60      0.60      0.60         5

avg / total       0.60      0.60      0.60        10



Confusion matrix:
[[3 2]
 [2 3]]



Classifying 1 th split of fair apps with unfair app
-------------------------------------------------------------------------------


Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=distance)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.86      0.75      0.80         8
       True       0.33      0.50      0.40         2

avg / total       0.75      0.70      0.72        10



Confusion matrix:
[[6 2]
 [1 1]]


Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=uniform)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.88      0.88      0.88         8
       True       0.50      0.50      0.50         2

avg / total       0.80      0.80      0.80        10



Confusion matrix:
[[7 1]
 [1 1]]


Classifier: 
 GaussianNB()
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.80      1.00      0.89         8
       True       0.00      0.00      0.00         2

avg / total       0.64      0.80      0.71        10



Confusion matrix:
[[8 0]
 [2 0]]


Classifier: 
 DecisionTreeClassifier(compute_importances=None, criterion=gini,
            max_depth=None, max_features=None, min_density=None,
            min_samples_leaf=1, min_samples_split=2, random_state=None,
            splitter=best)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.67      0.50      0.57         8
       True       0.00      0.00      0.00         2

avg / total       0.53      0.40      0.46        10



Confusion matrix:
[[4 4]
 [2 0]]


Classifier: 
 SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, degree=3, gamma=0.0,
  kernel=rbf, max_iter=-1, probability=False, random_state=None,
  shrinking=True, tol=0.001, verbose=False)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.00      0.00      0.00         8
       True       0.20      1.00      0.33         2

avg / total       0.04      0.20      0.07        10



Confusion matrix:
[[0 8]
 [0 2]]


Classifier: 
 NuSVC(cache_size=200, coef0=0.0, degree=3, gamma=0.0, kernel=rbf, max_iter=-1,
   nu=0.5, probability=False, random_state=None, shrinking=True, tol=0.001,
   verbose=False)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.88      0.88      0.88         8
       True       0.50      0.50      0.50         2

avg / total       0.80      0.80      0.80        10



Confusion matrix:
[[7 1]
 [1 1]]


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

      False       0.86      0.75      0.80         8
       True       0.33      0.50      0.40         2

avg / total       0.75      0.70      0.72        10



Confusion matrix:
[[6 2]
 [1 1]]



Classifying 2 th split of fair apps with unfair app
-------------------------------------------------------------------------------


Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=distance)
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

      False       0.43      0.60      0.50         5
       True       0.33      0.20      0.25         5

avg / total       0.38      0.40      0.38        10



Confusion matrix:
[[3 2]
 [4 1]]


Classifier: 
 DecisionTreeClassifier(compute_importances=None, criterion=gini,
            max_depth=None, max_features=None, min_density=None,
            min_samples_leaf=1, min_samples_split=2, random_state=None,
            splitter=best)
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
 SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, degree=3, gamma=0.0,
  kernel=rbf, max_iter=-1, probability=False, random_state=None,
  shrinking=True, tol=0.001, verbose=False)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.50      0.20      0.29         5
       True       0.50      0.80      0.62         5

avg / total       0.50      0.50      0.45        10



Confusion matrix:
[[1 4]
 [1 4]]


Classifier: 
 NuSVC(cache_size=200, coef0=0.0, degree=3, gamma=0.0, kernel=rbf, max_iter=-1,
   nu=0.5, probability=False, random_state=None, shrinking=True, tol=0.001,
   verbose=False)
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

      False       0.33      0.40      0.36         5
       True       0.25      0.20      0.22         5

avg / total       0.29      0.30      0.29        10



Confusion matrix:
[[2 3]
 [4 1]]



Classifying 3 th split of fair apps with unfair app
-------------------------------------------------------------------------------


Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=distance)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.80      0.80      0.80         5
       True       0.80      0.80      0.80         5

avg / total       0.80      0.80      0.80        10



Confusion matrix:
[[4 1]
 [1 4]]


Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=uniform)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.80      0.80      0.80         5
       True       0.80      0.80      0.80         5

avg / total       0.80      0.80      0.80        10



Confusion matrix:
[[4 1]
 [1 4]]


Classifier: 
 GaussianNB()
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.62      1.00      0.77         5
       True       1.00      0.40      0.57         5

avg / total       0.81      0.70      0.67        10



Confusion matrix:
[[5 0]
 [3 2]]


Classifier: 
 DecisionTreeClassifier(compute_importances=None, criterion=gini,
            max_depth=None, max_features=None, min_density=None,
            min_samples_leaf=1, min_samples_split=2, random_state=None,
            splitter=best)
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
 SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, degree=3, gamma=0.0,
  kernel=rbf, max_iter=-1, probability=False, random_state=None,
  shrinking=True, tol=0.001, verbose=False)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       1.00      0.40      0.57         5
       True       0.62      1.00      0.77         5

avg / total       0.81      0.70      0.67        10



Confusion matrix:
[[2 3]
 [0 5]]


Classifier: 
 NuSVC(cache_size=200, coef0=0.0, degree=3, gamma=0.0, kernel=rbf, max_iter=-1,
   nu=0.5, probability=False, random_state=None, shrinking=True, tol=0.001,
   verbose=False)
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

      False       0.40      0.40      0.40         5
       True       0.40      0.40      0.40         5

avg / total       0.40      0.40      0.40        10



Confusion matrix:
[[2 3]
 [3 2]]



Classifying 4 th split of fair apps with unfair app
-------------------------------------------------------------------------------


Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=distance)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.80      0.57      0.67         7
       True       0.40      0.67      0.50         3

avg / total       0.68      0.60      0.62        10



Confusion matrix:
[[4 3]
 [1 2]]


Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=uniform)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.80      0.57      0.67         7
       True       0.40      0.67      0.50         3

avg / total       0.68      0.60      0.62        10



Confusion matrix:
[[4 3]
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
       True       0.22      0.67      0.33         3

avg / total       0.07      0.20      0.10        10



Confusion matrix:
[[0 7]
 [1 2]]


Classifier: 
 NuSVC(cache_size=200, coef0=0.0, degree=3, gamma=0.0, kernel=rbf, max_iter=-1,
   nu=0.5, probability=False, random_state=None, shrinking=True, tol=0.001,
   verbose=False)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.67      0.29      0.40         7
       True       0.29      0.67      0.40         3

avg / total       0.55      0.40      0.40        10



Confusion matrix:
[[2 5]
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



Classifying 5 th split of fair apps with unfair app
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

      False       0.60      0.60      0.60         5
       True       0.60      0.60      0.60         5

avg / total       0.60      0.60      0.60        10



Confusion matrix:
[[3 2]
 [2 3]]


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

      False       0.75      0.60      0.67         5
       True       0.67      0.80      0.73         5

avg / total       0.71      0.70      0.70        10



Confusion matrix:
[[3 2]
 [1 4]]



Classifying 6 th split of fair apps with unfair app
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

      False       0.67      1.00      0.80         6
       True       1.00      0.25      0.40         4

avg / total       0.80      0.70      0.64        10



Confusion matrix:
[[6 0]
 [3 1]]


Classifier: 
 DecisionTreeClassifier(compute_importances=None, criterion=gini,
            max_depth=None, max_features=None, min_density=None,
            min_samples_leaf=1, min_samples_split=2, random_state=None,
            splitter=best)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.67      0.33      0.44         6
       True       0.43      0.75      0.55         4

avg / total       0.57      0.50      0.48        10



Confusion matrix:
[[2 4]
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

      False       0.75      1.00      0.86         6
       True       1.00      0.50      0.67         4

avg / total       0.85      0.80      0.78        10



Confusion matrix:
[[6 0]
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

      False       0.60      0.50      0.55         6
       True       0.40      0.50      0.44         4

avg / total       0.52      0.50      0.51        10



Confusion matrix:
[[3 3]
 [2 2]]



Classifying 7 th split of fair apps with unfair app
-------------------------------------------------------------------------------


Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=distance)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.50      1.00      0.67         4
       True       1.00      0.33      0.50         6

avg / total       0.80      0.60      0.57        10



Confusion matrix:
[[4 0]
 [4 2]]


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

      False       0.40      1.00      0.57         4
       True       0.00      0.00      0.00         6

avg / total       0.16      0.40      0.23        10



Confusion matrix:
[[4 0]
 [6 0]]


Classifier: 
 DecisionTreeClassifier(compute_importances=None, criterion=gini,
            max_depth=None, max_features=None, min_density=None,
            min_samples_leaf=1, min_samples_split=2, random_state=None,
            splitter=best)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.40      0.50      0.44         4
       True       0.60      0.50      0.55         6

avg / total       0.52      0.50      0.51        10



Confusion matrix:
[[2 2]
 [3 3]]


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

      False       0.38      0.75      0.50         4
       True       0.50      0.17      0.25         6

avg / total       0.45      0.40      0.35        10



Confusion matrix:
[[3 1]
 [5 1]]


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

      False       0.38      0.75      0.50         4
       True       0.50      0.17      0.25         6

avg / total       0.45      0.40      0.35        10



Confusion matrix:
[[3 1]
 [5 1]]



Classifying 8 th split of fair apps with unfair app
-------------------------------------------------------------------------------


Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=distance)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.17      0.50      0.25         2
       True       0.75      0.38      0.50         8

avg / total       0.63      0.40      0.45        10



Confusion matrix:
[[1 1]
 [5 3]]


Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=uniform)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.17      0.50      0.25         2
       True       0.75      0.38      0.50         8

avg / total       0.63      0.40      0.45        10



Confusion matrix:
[[1 1]
 [5 3]]


Classifier: 
 GaussianNB()
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.17      0.50      0.25         2
       True       0.75      0.38      0.50         8

avg / total       0.63      0.40      0.45        10



Confusion matrix:
[[1 1]
 [5 3]]


Classifier: 
 DecisionTreeClassifier(compute_importances=None, criterion=gini,
            max_depth=None, max_features=None, min_density=None,
            min_samples_leaf=1, min_samples_split=2, random_state=None,
            splitter=best)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.12      0.50      0.20         2
       True       0.50      0.12      0.20         8

avg / total       0.42      0.20      0.20        10



Confusion matrix:
[[1 1]
 [7 1]]


Classifier: 
 SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, degree=3, gamma=0.0,
  kernel=rbf, max_iter=-1, probability=False, random_state=None,
  shrinking=True, tol=0.001, verbose=False)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.20      1.00      0.33         2
       True       0.00      0.00      0.00         8

avg / total       0.04      0.20      0.07        10



Confusion matrix:
[[2 0]
 [8 0]]


Classifier: 
 NuSVC(cache_size=200, coef0=0.0, degree=3, gamma=0.0, kernel=rbf, max_iter=-1,
   nu=0.5, probability=False, random_state=None, shrinking=True, tol=0.001,
   verbose=False)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.14      0.50      0.22         2
       True       0.67      0.25      0.36         8

avg / total       0.56      0.30      0.34        10



Confusion matrix:
[[1 1]
 [6 2]]


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

      False       0.14      0.50      0.22         2
       True       0.67      0.25      0.36         8

avg / total       0.56      0.30      0.34        10



Confusion matrix:
[[1 1]
 [6 2]]



Classifying 9 th split of fair apps with unfair app
-------------------------------------------------------------------------------


Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=distance)
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

      False       0.44      0.80      0.57         5
       True       0.00      0.00      0.00         5

avg / total       0.22      0.40      0.29        10



Confusion matrix:
[[4 1]
 [5 0]]


Classifier: 
 SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, degree=3, gamma=0.0,
  kernel=rbf, max_iter=-1, probability=False, random_state=None,
  shrinking=True, tol=0.001, verbose=False)
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
 NuSVC(cache_size=200, coef0=0.0, degree=3, gamma=0.0, kernel=rbf, max_iter=-1,
   nu=0.5, probability=False, random_state=None, shrinking=True, tol=0.001,
   verbose=False)
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

      False       0.50      1.00      0.67         5
       True       0.00      0.00      0.00         5

avg / total       0.25      0.50      0.33        10



Confusion matrix:
[[5 0]
 [5 0]]



Classifying 10 th split of fair apps with unfair app
-------------------------------------------------------------------------------


Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=distance)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       1.00      0.56      0.71         9
       True       0.20      1.00      0.33         1

avg / total       0.92      0.60      0.68        10



Confusion matrix:
[[5 4]
 [0 1]]


Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=uniform)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       1.00      0.67      0.80         9
       True       0.25      1.00      0.40         1

avg / total       0.93      0.70      0.76        10



Confusion matrix:
[[6 3]
 [0 1]]


Classifier: 
 GaussianNB()
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       1.00      0.78      0.88         9
       True       0.33      1.00      0.50         1

avg / total       0.93      0.80      0.84        10



Confusion matrix:
[[7 2]
 [0 1]]


Classifier: 
 DecisionTreeClassifier(compute_importances=None, criterion=gini,
            max_depth=None, max_features=None, min_density=None,
            min_samples_leaf=1, min_samples_split=2, random_state=None,
            splitter=best)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       1.00      0.22      0.36         9
       True       0.12      1.00      0.22         1

avg / total       0.91      0.30      0.35        10



Confusion matrix:
[[2 7]
 [0 1]]


Classifier: 
 SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, degree=3, gamma=0.0,
  kernel=rbf, max_iter=-1, probability=False, random_state=None,
  shrinking=True, tol=0.001, verbose=False)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.00      0.00      0.00         9
       True       0.10      1.00      0.18         1

avg / total       0.01      0.10      0.02        10



Confusion matrix:
[[0 9]
 [0 1]]


Classifier: 
 NuSVC(cache_size=200, coef0=0.0, degree=3, gamma=0.0, kernel=rbf, max_iter=-1,
   nu=0.5, probability=False, random_state=None, shrinking=True, tol=0.001,
   verbose=False)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       1.00      0.44      0.62         9
       True       0.17      1.00      0.29         1

avg / total       0.92      0.50      0.58        10



Confusion matrix:
[[4 5]
 [0 1]]


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

      False       1.00      0.11      0.20         9
       True       0.11      1.00      0.20         1

avg / total       0.91      0.20      0.20        10



Confusion matrix:
[[1 8]
 [0 1]]



Classifying 11 th split of fair apps with unfair app
-------------------------------------------------------------------------------


Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=distance)
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
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=uniform)
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
 GaussianNB()
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
 DecisionTreeClassifier(compute_importances=None, criterion=gini,
            max_depth=None, max_features=None, min_density=None,
            min_samples_leaf=1, min_samples_split=2, random_state=None,
            splitter=best)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.29      0.50      0.36         4
       True       0.33      0.17      0.22         6

avg / total       0.31      0.30      0.28        10



Confusion matrix:
[[2 2]
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

      False       0.38      0.75      0.50         4
       True       0.50      0.17      0.25         6

avg / total       0.45      0.40      0.35        10



Confusion matrix:
[[3 1]
 [5 1]]


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

      False       0.29      0.50      0.36         4
       True       0.33      0.17      0.22         6

avg / total       0.31      0.30      0.28        10



Confusion matrix:
[[2 2]
 [5 1]]



Classifying 12 th split of fair apps with unfair app
-------------------------------------------------------------------------------


Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=distance)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.67      0.67      0.67         6
       True       0.50      0.50      0.50         4

avg / total       0.60      0.60      0.60        10



Confusion matrix:
[[4 2]
 [2 2]]


Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=uniform)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.67      0.67      0.67         6
       True       0.50      0.50      0.50         4

avg / total       0.60      0.60      0.60        10



Confusion matrix:
[[4 2]
 [2 2]]


Classifier: 
 GaussianNB()
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.56      0.83      0.67         6
       True       0.00      0.00      0.00         4

avg / total       0.33      0.50      0.40        10



Confusion matrix:
[[5 1]
 [4 0]]


Classifier: 
 DecisionTreeClassifier(compute_importances=None, criterion=gini,
            max_depth=None, max_features=None, min_density=None,
            min_samples_leaf=1, min_samples_split=2, random_state=None,
            splitter=best)
###############################################################################
Classification report:
             precision    recall  f1-score   support

      False       0.62      0.83      0.71         6
       True       0.50      0.25      0.33         4

avg / total       0.57      0.60      0.56        10



Confusion matrix:
[[5 1]
 [3 1]]


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

      False       0.50      0.67      0.57         6
       True       0.00      0.00      0.00         4

avg / total       0.30      0.40      0.34        10



Confusion matrix:
[[4 2]
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

      False       0.67      1.00      0.80         6
       True       1.00      0.25      0.40         4

avg / total       0.80      0.70      0.64        10



Confusion matrix:
[[6 0]
 [3 1]]



