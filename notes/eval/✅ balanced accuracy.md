#machineLearning/evaluation

- # balanced accuracy
- $$
- \text{Balanced Accuracy} = \frac{\text{Sensitivity} + \text{Specificity}}{2}
- $$
- Average of sensitivity and specificity, useful for imbalanced classes.
- - **Usefulness**: **Balanced Accuracy** is helpful when you have an **imbalanced dataset** and want to average the **Sensitivity (Recall)** and **Specificity**. It ensures that both classes are treated equally in terms of performance, unlike traditional accuracy, which might be skewed by the majority class.
- - **Context**:
- - **Imbalanced datasets** (e.g., rare event detection, fraud detection)
- - **Classification tasks** where both positive and negative classes need to be considered equally
- - **Key Focus**: Balancing the performance between the positive and negative classes.
