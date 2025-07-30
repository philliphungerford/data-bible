---
type: Definition
title: Learning Curves/Rates
tags:
  - definition
---

# Learning Curves/Rates

[image](image%20(1).md)

In neural network training, learning curves are plots that show how a model's performance (like accuracy or loss) changes as the amount of training data increases. They help diagnose issues like overfitting and underfitting and determine if adding more data will improve the model's performance. For loss they show [[📖 Epoch]] on the x axis and [[📖 Loss]] on the y axis. 



- **Why they're important:**

    - **Overfitting:** If the training loss is much lower than the validation loss, and the validation loss doesn't improve with more data, the model might be overfitting, meaning it's learning the training data too well and not generalizing to new data. 

    - **Underfitting:** If both training and validation losses are high and don't improve much with more data, the model might be underfitting, meaning it's not complex enough to capture the underlying patterns in the data. 

    - **Data Sufficiency:** Learning curves help determine if adding more training data will significantly improve model performance. 

- **Interpreting Learning Curves:**

    - **Steep Curve:** A steep curve indicates that the model learns quickly initially, but the rate of improvement slows down as more data is added. 

    - **Flat Curve:** A flat curve suggests that the model has reached a plateau, and adding more data may not lead to significant improvements. 

- **Types of Learning Curves:**

    - **Diminishing Returns:** The rate of improvement decreases as more data is added. 

    - **Increasing Returns:** The rate of improvement increases as more data is added. 

    - **S-Curve:** A combination of both diminishing and increasing returns. 

    - **Complex Curve:** Multiple peaks and plateaus, often seen in complex tasks.

