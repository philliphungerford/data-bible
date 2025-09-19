---
type: ProblemType
title: Ordinal Classification
tags:
  - problemType
---

---

**Definition:** Predicts **a numeric value** instead of categories.

**Examples:**

- Movie Ratings

- Pain Scores

- Functionality

- Example 1: A marketing research firm wants to investigate what factors influence the size of soda (small, medium, large or extra large) that people order at a fast-food chain. These factors may include what type of sandwich is ordered (burger or chicken), whether or not fries are also ordered, and age of the consumer. While the outcome variable, size of soda, is obviously ordered, the difference between the various sizes is not consistent. The difference between small and medium is 10 ounces, between medium and large 8, and between large and extra large 12.

- Example 2: A researcher is interested in what factors influence medaling in Olympic swimming. Relevant predictors include at training hours, diet, age, and popularity of swimming in the athlete’s home country. The researcher believes that the distance between gold and silver is larger than the distance between silver and bronze.

- Example 3: A study looks at factors that influence the decision of whether to apply to graduate school. College juniors are asked if they are unlikely, somewhat likely, or very likely to apply to graduate school. Hence, our outcome variable has three categories. Data on parental educational status, whether the undergraduate institution is public or private, and current GPA is also collected. The researchers have reason to believe that the “distances” between these three points are not equal. For example, the “distance” between “unlikely” and “somewhat likely” may be shorter than the distance between “somewhat likely” and “very likely”.

**Common Algorithms:**

🔹 [[➗ Linear Regression]]

🔹 [[➗ Decision Tree]] / [[➗ Random Forest]]

🔹 [[➗ XGBoost]]

🔹 [[➗ Neural Network]]

**Evaluation Metrics:**

✅ [[✅ Mean Absolute Error (MAE)|Mean Absolute Error (MAE)]]

✅[[✅ Mean Squared Error (MSE)]]

✅ [[✅ R² (R-squared)|R² (R-squared)]]



Ordinal Logistic Regression (Proportional Odds Model):

Support Vector Machines (SVM) for Ordinal Regression

Random Forest for Ordinal Regression

Gradient Boosting Machines (GBMs) for Ordinal Data

Neural Networks with Ordinal Cross-Entropy

Generalized Linear Models (GLM) with Ordinal Family

