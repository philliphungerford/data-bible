---
type: Definition
title: Loss
tags:
  - definition
---

# Loss

*A measure of how well a machine learning model is learning during training.* 

It quantifies **the difference between the model's predictions and the actual target** values (ground truth) on the training dataset.

### How It Works:

- During training, the model makes predictions and compares them to the true labels.

- A **loss function** (e.g., Mean Squared Error for regression, Cross-Entropy for classification) calculates the error.

- The model updates its weights using optimization algorithms like **Stochastic Gradient Descent (SGD)** or **Adam** to minimize this loss.

- The training loss is computed after each batch or epoch.

### Key Points:

- **Lower training loss** means the model is fitting the training data well.

- **High training loss** suggests the model is struggling to learn patterns.

- **Overfitting** happens if training loss is low but validation loss is high.

### Example:

If a neural network classifies images of cats and dogs:

- If it predicts "cat" with 0.9 confidence for an actual cat image, the loss will be low.

- If it predicts "dog" with 0.2 confidence for a cat image, the loss will be high.

