#machineLearning/evaluation

- #evaluationMetric
- # precision / positive predictive value
- $$
- \text{Precision} = \frac{\text{True Positives}}{\text{True Positives} + \text{False Positives}}
- $$
- The proportion of positive predictions that are actually correct (i.e., [[✅ true positives]] / ([[✅ true positives]] + [[✅ false positives]])).
- - **Usefulness**: **Precision** is key when you care about the **accuracy of positive predictions**. It is useful when the **cost of false positives** is high. For instance, in online advertising, you want the ads you show to be relevant to avoid wasting money and irritating users.
- - **Context**:
- - **Online advertising** (to make sure ads are relevant to the audience)
- - **Search engine results** (to ensure that results are truly relevant)
- - **Recommendation systems** (to recommend items that the user is likely to engage with)
- - **Key Focus**: Minimizing false positives, improving the relevance of positive predictions.
