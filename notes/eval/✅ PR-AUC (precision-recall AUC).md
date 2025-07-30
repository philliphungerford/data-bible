#machineLearning/evaluation

- #evaluationMetric
- # PR-AUC (precision-recall AUC)
- The **PR AUC** (Precision-Recall Area Under the Curve) is a metric used to evaluate the performance of a binary classifier, especially in cases where the dataset is imbalanced (i.e., there are many more instances of one class than the other). It combines **Precision** and **Recall** into a single score by plotting the **Precision**-**Recall** curve, then calculating the area under that curve.
- Here's how to interpret PR AUC:
- - **PR AUC value range**: The PR AUC value ranges from 0 to 1.
- - A score of **1** indicates perfect classification, where the classifier has both high precision and high recall across all thresholds.
- - A score of **0.5** suggests that the classifier's performance is no better than random guessing.
- - A score closer to **0** indicates poor performance, with very low precision or recall.
- - [Precision](✅%20precision%20%20positive%20predictive%20value.md): The proportion of positive predictions that are actually correct (i.e., true positives / (true positives + false positives)).
- - [Recall](✅%20recall%20sensitivity%20%20true%20positive%20rate.md): The proportion of actual positive cases that are correctly identified (i.e., true positives / (true positives + false negatives)).
- - **Curve Behavior**: A higher PR AUC typically means that the classifier is better at distinguishing between the classes, particularly when dealing with an imbalanced dataset. A higher PR AUC suggests the classifier performs well even when there are very few positive examples, as it maintains both high precision and high recall.
- In summary:
- - A **high PR AUC** indicates good model performance, particularly in imbalanced datasets.
- - A **low PR AUC** suggests that the model is either making many false positives, missing many positive cases, or both.
