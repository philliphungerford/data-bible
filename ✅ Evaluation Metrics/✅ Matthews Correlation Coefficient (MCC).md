---
type: EvaluationMetric
title: Matthews Correlation Coefficient (MCC)
tags:
  - "#evaluationMetric"
---

# Matthews Correlation Coefficient (MCC)

$$
\text{MCC} = \frac{TP \times TN - FP \times FN}{\sqrt{(TP + FP)(TP + FN)(TN + FP)(TN + FN)}}

$$

A balanced measure considering true positives, false positives, true negatives, and false negatives.



- **Usefulness**: The **MCC** is a **balanced metric** that considers all four components of the confusion matrix (True Positives, True Negatives, False Positives, and False Negatives). It is particularly useful in cases where the data is **highly imbalanced**, as it gives a more balanced view of the model’s performance than accuracy.

- **Context**:

    - **Imbalanced datasets** (e.g., fraud detection, rare disease detection)

    - **Classification problems** with very uneven class distributions

- **Key Focus**: Provides a balanced performance measure when accuracy is not sufficient.

- 

