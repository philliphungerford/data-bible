#machineLearning/evaluation

- #evaluationMetric
- # recall / sensitivity / true positive rate
- The proportion of actual positive cases that are correctly identified (i.e., [[✅ true positives]] / ([[✅ true positives]] + [[✅ false negatives]])).
- $$
- \text{Recall} = \frac{\text{True Positives}}{\text{True Positives} + \text{False Negatives}}
- $$
- - **Usefulness**: **Sensitivity** is particularly useful when the **cost of missing positive cases** is high. For example, in medical diagnostics (e.g., detecting cancer), it's critical to identify as many actual positive cases as possible, even if some false positives occur.
- - **Context**:
- - **Medical tests** (e.g., detecting diseases)
- - **Fraud detection** (where missing fraud cases can be highly costly)
- - **Search engines** (finding relevant documents or pages)
- - **Spam email detection** (where it's important to catch as many spam emails as possible)
- - **Key Focus**: Minimizing false negatives.
- Focusing on recall is like having a large fishing net. You don't mind capturing (predicting) fish that may not be the ones you want.
