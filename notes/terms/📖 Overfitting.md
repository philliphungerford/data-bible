#definition

- # Overfitting
- [[image]]
- Overfitting happens when a machine learning model learns the **training data too well**, to the point that it **memorizes** it instead of generalizing patterns. This results in excellent performance on the training set but poor performance on unseen (validation/test) data.
- ### **How Overfitting Looks in Training vs. Validation Loss**
- A classic sign of overfitting is when:
- - **Training loss continues to decrease**, but
- - **Validation loss stops decreasing and starts increasing** after a certain point.
- #### **Visual Example:**
- If you plot **loss vs. epochs**, an overfitted model would look like this:
- 📉 **Training Loss Curve:** Keeps decreasing
- 📈 **Validation Loss Curve:** Decreases at first, then increases
