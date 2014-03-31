Data Size: (323, 10), 	 Model Choice: all
FoldSize: 80
 X_train: (243, 9), Y_train: (243,), X_test: (80, 9), Y_test: (80,)
#### Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=distance)
Classification report:
             precision    recall  f1-score   support

      False       0.99      0.95      0.97        78
       True       0.20      0.50      0.29         2

avg / total       0.97      0.94      0.95        80



Confusion matrix:
[[74  4]
 [ 1  1]]
 X_train: (243, 9), Y_train: (243,), X_test: (80, 9), Y_test: (80,)
#### Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=distance)
Classification report:
             precision    recall  f1-score   support

      False       0.96      0.99      0.97        77
       True       0.00      0.00      0.00         3

avg / total       0.93      0.95      0.94        80



Confusion matrix:
[[76  1]
 [ 3  0]]
 X_train: (243, 9), Y_train: (243,), X_test: (80, 9), Y_test: (80,)
#### Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=distance)
Classification report:
             precision    recall  f1-score   support

      False       0.95      0.99      0.97        76
       True       0.00      0.00      0.00         4

avg / total       0.90      0.94      0.92        80



Confusion matrix:
[[75  1]
 [ 4  0]]
 X_train: (243, 9), Y_train: (243,), X_test: (80, 9), Y_test: (80,)
#### Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=distance)
Classification report:
             precision    recall  f1-score   support

      False       0.85      0.99      0.91        67
       True       0.50      0.08      0.13        13

avg / total       0.79      0.84      0.78        80



Confusion matrix:
[[66  1]
 [12  1]]
FoldSize: 80
 X_train: (243, 9), Y_train: (243,), X_test: (80, 9), Y_test: (80,)
#### Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=uniform)
Classification report:
             precision    recall  f1-score   support

      False       0.99      0.97      0.98        78
       True       0.33      0.50      0.40         2

avg / total       0.97      0.96      0.97        80



Confusion matrix:
[[76  2]
 [ 1  1]]
 X_train: (243, 9), Y_train: (243,), X_test: (80, 9), Y_test: (80,)
#### Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=uniform)
Classification report:
             precision    recall  f1-score   support

      False       0.96      1.00      0.98        77
       True       0.00      0.00      0.00         3

avg / total       0.93      0.96      0.94        80



Confusion matrix:
[[77  0]
 [ 3  0]]
 X_train: (243, 9), Y_train: (243,), X_test: (80, 9), Y_test: (80,)
#### Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=uniform)
Classification report:
             precision    recall  f1-score   support

      False       0.95      1.00      0.97        76
       True       0.00      0.00      0.00         4

avg / total       0.90      0.95      0.93        80



Confusion matrix:
[[76  0]
 [ 4  0]]
 X_train: (243, 9), Y_train: (243,), X_test: (80, 9), Y_test: (80,)
#### Classifier: 
 KNeighborsClassifier(algorithm=auto, leaf_size=30, metric=minkowski,
           n_neighbors=3, p=2, weights=uniform)
Classification report:
             precision    recall  f1-score   support

      False       0.85      0.99      0.91        67
       True       0.50      0.08      0.13        13

avg / total       0.79      0.84      0.78        80



Confusion matrix:
[[66  1]
 [12  1]]
FoldSize: 80
 X_train: (243, 9), Y_train: (243,), X_test: (80, 9), Y_test: (80,)
#### Classifier: 
 GaussianNB()
Classification report:
             precision    recall  f1-score   support

      False       0.99      0.91      0.95        78
       True       0.12      0.50      0.20         2

avg / total       0.96      0.90      0.93        80



Confusion matrix:
[[71  7]
 [ 1  1]]
 X_train: (243, 9), Y_train: (243,), X_test: (80, 9), Y_test: (80,)
#### Classifier: 
 GaussianNB()
Classification report:
             precision    recall  f1-score   support

      False       0.99      0.95      0.97        77
       True       0.33      0.67      0.44         3

avg / total       0.96      0.94      0.95        80



Confusion matrix:
[[73  4]
 [ 1  2]]
 X_train: (243, 9), Y_train: (243,), X_test: (80, 9), Y_test: (80,)
#### Classifier: 
 GaussianNB()
Classification report:
             precision    recall  f1-score   support

      False       0.95      1.00      0.97        76
       True       0.00      0.00      0.00         4

avg / total       0.90      0.95      0.93        80



Confusion matrix:
[[76  0]
 [ 4  0]]
 X_train: (243, 9), Y_train: (243,), X_test: (80, 9), Y_test: (80,)
#### Classifier: 
 GaussianNB()
Classification report:
             precision    recall  f1-score   support

      False       0.74      0.21      0.33        67
       True       0.13      0.62      0.22        13

avg / total       0.64      0.28      0.31        80



Confusion matrix:
[[14 53]
 [ 5  8]]
FoldSize: 80
 X_train: (243, 9), Y_train: (243,), X_test: (80, 9), Y_test: (80,)
#### Classifier: 
 DecisionTreeClassifier(compute_importances=None, criterion=gini,
            max_depth=None, max_features=None, min_density=None,
            min_samples_leaf=1, min_samples_split=2, random_state=None,
            splitter=best)
Classification report:
             precision    recall  f1-score   support

      False       0.97      0.87      0.92        78
       True       0.00      0.00      0.00         2

avg / total       0.95      0.85      0.90        80



Confusion matrix:
[[68 10]
 [ 2  0]]
 X_train: (243, 9), Y_train: (243,), X_test: (80, 9), Y_test: (80,)
#### Classifier: 
 DecisionTreeClassifier(compute_importances=None, criterion=gini,
            max_depth=None, max_features=None, min_density=None,
            min_samples_leaf=1, min_samples_split=2, random_state=None,
            splitter=best)
Classification report:
             precision    recall  f1-score   support

      False       0.96      0.91      0.93        77
       True       0.00      0.00      0.00         3

avg / total       0.92      0.88      0.90        80



Confusion matrix:
[[70  7]
 [ 3  0]]
 X_train: (243, 9), Y_train: (243,), X_test: (80, 9), Y_test: (80,)
#### Classifier: 
 DecisionTreeClassifier(compute_importances=None, criterion=gini,
            max_depth=None, max_features=None, min_density=None,
            min_samples_leaf=1, min_samples_split=2, random_state=None,
            splitter=best)
Classification report:
             precision    recall  f1-score   support

      False       0.97      0.86      0.91        76
       True       0.15      0.50      0.24         4

avg / total       0.93      0.84      0.88        80



Confusion matrix:
[[65 11]
 [ 2  2]]
 X_train: (243, 9), Y_train: (243,), X_test: (80, 9), Y_test: (80,)
#### Classifier: 
 DecisionTreeClassifier(compute_importances=None, criterion=gini,
            max_depth=None, max_features=None, min_density=None,
            min_samples_leaf=1, min_samples_split=2, random_state=None,
            splitter=best)
Classification report:
             precision    recall  f1-score   support

      False       0.87      0.97      0.92        67
       True       0.60      0.23      0.33        13

avg / total       0.82      0.85      0.82        80



Confusion matrix:
[[65  2]
 [10  3]]
FoldSize: 80
 X_train: (243, 9), Y_train: (243,), X_test: (80, 9), Y_test: (80,)
#### Classifier: 
 SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, degree=3, gamma=0.0,
  kernel=rbf, max_iter=-1, probability=False, random_state=None,
  shrinking=True, tol=0.001, verbose=False)
Classification report:
             precision    recall  f1-score   support

      False       0.97      1.00      0.99        78
       True       0.00      0.00      0.00         2

avg / total       0.95      0.97      0.96        80



Confusion matrix:
[[78  0]
 [ 2  0]]
 X_train: (243, 9), Y_train: (243,), X_test: (80, 9), Y_test: (80,)
#### Classifier: 
 SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, degree=3, gamma=0.0,
  kernel=rbf, max_iter=-1, probability=False, random_state=None,
  shrinking=True, tol=0.001, verbose=False)
Classification report:
             precision    recall  f1-score   support

      False       0.96      1.00      0.98        77
       True       0.00      0.00      0.00         3

avg / total       0.93      0.96      0.94        80



Confusion matrix:
[[77  0]
 [ 3  0]]
 X_train: (243, 9), Y_train: (243,), X_test: (80, 9), Y_test: (80,)
#### Classifier: 
 SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, degree=3, gamma=0.0,
  kernel=rbf, max_iter=-1, probability=False, random_state=None,
  shrinking=True, tol=0.001, verbose=False)
Classification report:
             precision    recall  f1-score   support

      False       0.95      1.00      0.97        76
       True       0.00      0.00      0.00         4

avg / total       0.90      0.95      0.93        80



Confusion matrix:
[[76  0]
 [ 4  0]]
 X_train: (243, 9), Y_train: (243,), X_test: (80, 9), Y_test: (80,)
#### Classifier: 
 SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, degree=3, gamma=0.0,
  kernel=rbf, max_iter=-1, probability=False, random_state=None,
  shrinking=True, tol=0.001, verbose=False)
Classification report:
             precision    recall  f1-score   support

      False       0.84      1.00      0.91        67
       True       0.00      0.00      0.00        13

avg / total       0.70      0.84      0.76        80



Confusion matrix:
[[67  0]
 [13  0]]
FoldSize: 80
 X_train: (243, 9), Y_train: (243,), X_test: (80, 9), Y_test: (80,)
#### Classifier: 
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
Classification report:
             precision    recall  f1-score   support

      False       0.97      0.96      0.97        78
       True       0.00      0.00      0.00         2

avg / total       0.95      0.94      0.94        80



Confusion matrix:
[[75  3]
 [ 2  0]]
 X_train: (243, 9), Y_train: (243,), X_test: (80, 9), Y_test: (80,)
#### Classifier: 
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
Classification report:
             precision    recall  f1-score   support

      False       0.96      0.99      0.97        77
       True       0.00      0.00      0.00         3

avg / total       0.93      0.95      0.94        80



Confusion matrix:
[[76  1]
 [ 3  0]]
 X_train: (243, 9), Y_train: (243,), X_test: (80, 9), Y_test: (80,)
#### Classifier: 
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
Classification report:
             precision    recall  f1-score   support

      False       0.95      1.00      0.97        76
       True       0.00      0.00      0.00         4

avg / total       0.90      0.95      0.93        80



Confusion matrix:
[[76  0]
 [ 4  0]]
 X_train: (243, 9), Y_train: (243,), X_test: (80, 9), Y_test: (80,)
#### Classifier: 
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
Classification report:
             precision    recall  f1-score   support

      False       0.87      0.97      0.92        67
       True       0.60      0.23      0.33        13

avg / total       0.82      0.85      0.82        80



Confusion matrix:
[[65  2]
 [10  3]]
