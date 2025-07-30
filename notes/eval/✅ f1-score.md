#machineLearning/evaluation

- #evaluationMetric
- # f1-score
- $$
- F1 = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}
- $$
- Harmonic mean of precision and recall, balancing their trade-off.
- - **Usefulness**: The **F1-Score** is useful when you want to balance **Precision and Recall**. It is especially valuable when you care about both false positives and false negatives and your classes are imbalanced. F1 combines both metrics into one number, giving you a clear tradeoff between precision and recall.
- - **Context**:
- - **Imbalanced datasets** (e.g., rare disease detection)
- - **Information retrieval systems** (balancing precision and recall)
- - **Natural language processing (NLP)** tasks (such as entity recognition, where both precision and recall are important)
- - **Key Focus**: Balancing the tradeoff between precision and recall when there is an imbalance.
