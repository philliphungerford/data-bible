#machineLearning/evaluation

- # specificity / true negative rate
- $$
- \text{Specificity} = \frac{\text{True Negatives}}{\text{True Negatives} + \text{False Positives}}
- $$
- **Specificity** (also known as the **True Negative Rate**) is a metric that measures the proportion of actual negative instances that are correctly identified by the model. It answers the question: *"Of all the actual negative instances, how many did the model correctly identify?" (ie.* [[✅ true negatives]] / [[✅ true negatives]] + [[✅ false positives]])
- - **Usefulness**: **Specificity** is important when the **cost of falsely classifying a negative case as positive** is high. For instance, in scenarios like fraud detection or legal applications, you don't want to falsely accuse someone of a crime.
- - **Context**:
- - **Medical tests** (e.g., ruling out a disease in healthy people)
- - **Legal or security systems** (to avoid falsely accusing innocent people)
- - **Spam email detection** (to avoid labeling legitimate emails as spam)
- - **Key Focus**: Minimizing false positives.
