#definition

- # Underfitting
- **Underfitting** occurs when a machine learning model is too **simple** to capture the underlying patterns in the data. It happens when the model cannot learn enough from the training data, resulting in poor performance on both the **training set** and the **test/validation set**.
- ### **How Underfitting Looks in Training vs. Validation Loss**
- A sign of underfitting is when:
- - Both **training loss and validation loss** are **high** and decrease very slowly or not at all.
- #### **Visual Example:**
- If you plot **loss vs. epochs**, an underfitted model would look like this:
- 📈 **Training Loss Curve:** Starts low and plateaus or decreases very slowly
- 📈 **Validation Loss Curve:** Starts high and decreases at the same slow rate, staying near the training loss
