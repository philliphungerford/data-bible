---
type: Definition
title: Epoch
tags:
  - definition
---

# Epoch

One complete pass through the entire training dataset during the training process of a model.

### Example:

- Suppose you have **1,000** training examples and you set **batch size = 100**.

- This means **one epoch** will consist of **10 iterations** (since 1000/100=101000 / 100 = 101000/100=10).

- If you train for **10 epochs**, the model will have seen the entire dataset **10 times**.

### Key Considerations:

- **Too few epochs** might lead to **underfitting** (not learning enough patterns).

- **Too many epochs** might lead to **overfitting** (memorizing training data instead of generalizing well).


