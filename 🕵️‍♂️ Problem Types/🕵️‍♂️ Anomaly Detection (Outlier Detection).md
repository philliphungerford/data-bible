---
type: ProblemType
title: Anomaly Detection (Outlier Detection)
tags:
  - problemType
---


| Algorithm                                                    | Type                     | Use Case                                           | How It Works                                                                                                      | Advantages                                                          | Disadvantages                                                                    |
| :----------------------------------------------------------- | :----------------------- | :------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------ | :------------------------------------------------------------------------------- |
| **Z-Score (Standard Deviation Method)**                      | Statistical              | Detecting outliers in small datasets               | Assumes normal distribution; flags points beyond a threshold (e.g., 3 standard deviations)                        | Simple, interpretable, works well for normally distributed data     | Assumes Gaussian distribution, sensitive to extreme values                       |
| **IQR (Interquartile Range Method)**                         | Statistical              | Detecting outliers in univariate data              | Uses Q1 and Q3 to set a range for normal values (outliers fall outside Q1 - 1.5*IQR and Q3 + 1.5*IQR)             | Robust to non-Gaussian data, easy to implement                      | Ineffective for small datasets, does not work well with multimodal distributions |
| **Isolation Forest**                                         | Tree-based (Ensemble)    | Detecting anomalies in large datasets              | Randomly partitions data and isolates anomalies (which require fewer splits)                                      | Works well for high-dimensional data, scalable                      | Performance depends on hyperparameter tuning                                     |
| **Local Outlier Factor (LOF)**                               | Density-based            | Identifying local anomalies                        | Compares local density of a point to its neighbors to detect deviations                                           | Works well for non-uniform density datasets                         | Computationally expensive for large datasets                                     |
| **One-Class SVM**                                            | Kernel-based (SVM)       | Anomaly detection in high-dimensional space        | Learns a decision boundary around normal data, classifying distant points as anomalies                            | Effective in high-dimensional spaces, works well with small data    | Sensitive to hyperparameters, computationally expensive for large datasets       |
| **DBSCAN (Density-Based Spatial Clustering)**                | Clustering-based         | Identifying anomalies in spatial data              | Identifies core, border, and noise points (outliers are noise points)                                             | Finds arbitrarily shaped anomalies, robust to noise                 | Requires tuning (eps, min_samples), struggles with varying densities             |
| **Autoencoders (Neural Networks)**                           | Deep Learning            | Complex anomaly detection in high-dimensional data | Uses an encoder-decoder architecture to reconstruct normal data and flags high reconstruction errors as anomalies | Works well for non-linear relationships, powerful on large datasets | Requires large labeled datasets, computationally expensive                       |
| **PCA (Principal Component Analysis) for Anomaly Detection** | Dimensionality Reduction | Identifying anomalies in high-dimensional data     | Reduces dimensionality, identifies deviations in principal components                                             | Effective for linear relationships, interpretable                   | Assumes linearity, can miss complex anomalies                                    |
| **Bayesian Networks**                                        | Probabilistic            | Probabilistic anomaly detection                    | Models dependencies between variables and detects anomalies based on probability deviations                       | Captures complex dependencies, robust to missing data               | Computationally expensive, requires domain knowledge                             |

## Key Notes:

- **Statistical Methods (e.g., Z-Score, IQR):** Simple and effective for small, normally distributed datasets.

- **Tree-Based Methods (e.g., Isolation Forest):** Scalable and efficient for large, high-dimensional datasets.

- **Density-Based Methods (e.g., LOF, DBSCAN):** Good for detecting local anomalies in datasets with varying densities.

- **Kernel-Based Methods (e.g., One-Class SVM):** Effective for high-dimensional data but sensitive to parameter tuning.

- **Deep Learning (e.g., Autoencoders):** Powerful for complex and large-scale data, but requires significant computational resources.

- **Probabilistic Approaches (e.g., Bayesian Networks):** Useful for modeling variable dependencies but can be computationally expensive.

