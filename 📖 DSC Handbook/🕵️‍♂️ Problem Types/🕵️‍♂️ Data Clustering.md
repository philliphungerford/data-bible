---
type: ProblemType
title: Data Clustering
tags:
  - problemType
---

## **What is Clustering?**

Clustering is an **unsupervised machine learning** technique used to group similar data points together based on patterns in the data. Unlike classification or regression, clustering does **not require labeled data**. Instead, it discovers natural groupings within the dataset.

---

## **When to Use Clustering?**

Clustering is useful when: ✅ You want to **group similar entities** (e.g., customer segmentation). ✅ You need to **identify patterns** in data without predefined labels. ✅ You are performing **anomaly detection** (e.g., fraud detection, network security). ✅ You are exploring **high-dimensional data** for pattern discovery (e.g., gene expression analysis).

---

### Clustering Models

**Goal**: Understand various clustering models and their appropriate use cases for grouping data points based on similarity.

| Algorithm                                                                                                                            | Type           | Use Case                                              | How It Works                                                                          | Advantages                                                                                   | Disadvantages                                                      |
| :----------------------------------------------------------------------------------------------------------------------------------- | :------------- | :---------------------------------------------------- | :------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------- | :----------------------------------------------------------------- |
| [K-Means Clustering](https://app.capacities.io/5c80aa35-933b-4978-88d3-dfa36cb3a18f/905787b7-cd9b-4081-b052-8a5bb03d5d2a)            | Partitioning   | Grouping data into k clusters based on similarity     | Iteratively assigns points to the nearest centroid and updates centroids              | Simple, scalable, efficient for large datasets                                               | Requires pre-setting k, sensitive to initialization and outliers   |
| **Hierarchical Clustering**                                                                                                          | Hierarchical   | Building nested clusters (dendrogram visualization)   | Recursively merges (agglomerative) or splits (divisive) clusters based on distance    | Does not require a pre-specified number of clusters, intuitive visualization                 | Computationally expensive, sensitive to linkage criteria           |
| [DBSCAN](https://app.capacities.io/5c80aa35-933b-4978-88d3-dfa36cb3a18f/7d3b7c6b-8bca-47ba-9e8a-fd6cc9bf37cb)                        | Density-based  | Discovering arbitrarily shaped clusters, noise points | Groups points that are closely packed, separating noise out                           | Can find non-spherical clusters, robust to noise                                             | Requires tuning of density parameters (eps, min_samples)           |
| **Mean Shift**                                                                                                                       | Density-based  | Clustering without pre-defining number of clusters    | Shifts data points towards the mode of the data distribution                          | Automatically determines the number of clusters, robust to outliers                          | Can be computationally expensive, sensitive to bandwidth choice    |
| [Gaussian Mixture Models (GMM)](https://app.capacities.io/5c80aa35-933b-4978-88d3-dfa36cb3a18f/b27e5f4b-cc00-4573-ba2f-bb684c935115) | Probabilistic  | Soft clustering with overlapping clusters             | Assumes data is generated from a mixture of Gaussian distributions, uses EM algorithm | Provides probability for each point's cluster membership, flexible cluster shape             | Requires selection of number of components, can be slow            |
| **Spectral Clustering**                                                                                                              | Graph-based    | Clustering complex, non-convex shapes                 | Uses eigenvalues of a similarity matrix to reduce dimensions and cluster points       | Effective for non-linear cluster boundaries, works on graph data                             | Computationally intensive for large datasets, sensitive to scaling |
| **Affinity Propagation**                                                                                                             | Exemplar-based | Clustering by finding representative examples         | Exchanges messages between points until convergence on exemplars                      | Does not require pre-setting the number of clusters, works well with non-Euclidean distances | Can be memory intensive, sensitive to damping factor               |

## Key Notes:

- **Partitioning Methods (e.g., K-Means):** Best for spherical, well-separated clusters but require a predetermined number of clusters.

- **Hierarchical Methods:** Provide a tree-like structure, useful for understanding nested relationships, but may struggle with very large datasets.

- **Density-based Methods (e.g., DBSCAN, Mean Shift):** Excellent for finding arbitrary shapes and dealing with noise, yet sensitive to parameter settings.

- **Probabilistic Methods (e.g., GMM):** Offer soft clustering and flexibility in shape, though they require assumptions about data distribution.

- **Graph-based Methods (e.g., Spectral Clustering):** Suitable for complex clusters but can be computationally heavy.

#### Key Points:

1. **K-Means Clustering**:

    - **Type**: Partitional clustering algorithm.

    - **Use case**: Used to partition data into `k` distinct, non-overlapping clusters based on feature similarity.

    - **How it works**: The algorithm assigns each data point to one of `k` centroids and iteratively updates the centroids by minimizing the sum of squared distances between points and their assigned centroid.

    - **Advantages**: Simple and fast, works well with spherical (convex) clusters, easy to interpret.

    - **Disadvantages**: Sensitive to the initial placement of centroids, requires specifying the number of clusters (k), struggles with non-spherical or unevenly sized clusters.

2. **Hierarchical Clustering**:

    - **Type**: Agglomerative or divisive clustering algorithm.

    - **Use case**: Creates a hierarchy of clusters that can be visualized as a dendrogram, often used in exploratory analysis.

    - **How it works**: Agglomerative hierarchical clustering starts with each point as a separate cluster and iteratively merges the closest clusters. Divisive clustering starts with all points in a single cluster and recursively splits them into smaller clusters.

    - **Advantages**: No need to predefine the number of clusters, easy to visualize using dendrograms, works well for small datasets.

    - **Disadvantages**: Computationally expensive for large datasets, sensitive to noise, doesn't scale well for very large data.

3. **DBSCAN (Density-Based Spatial Clustering of Applications with Noise)**:

    - **Type**: Density-based clustering algorithm.

    - **Use case**: Detects clusters of varying shapes and sizes, particularly useful for datasets with noise and outliers.

    - **How it works**: It defines clusters as areas of high density separated by areas of low density. Points in low-density regions are considered noise and are not assigned to any cluster.

    - **Advantages**: Can find clusters of arbitrary shape, works well with noisy data, doesn't require specifying the number of clusters.

    - **Disadvantages**: Sensitive to the choice of `epsilon` (neighborhood radius) and `min_samples` (minimum points per cluster), struggles with clusters of varying densities.

4. **Gaussian Mixture Models (GMM)**:

    - **Type**: Probabilistic model-based clustering algorithm.

    - **Use case**: Assumes that the data is generated from a mixture of several Gaussian distributions and assigns probabilities to data points based on the likelihood of each point belonging to a specific cluster.

    - **How it works**: GMM uses the Expectation-Maximization (EM) algorithm to iteratively estimate the parameters of the Gaussian distributions (mean, covariance) and the assignment probabilities for each data point.

    - **Advantages**: Can model elliptical clusters, works well with overlapping clusters, gives a probabilistic interpretation of clustering.

    - **Disadvantages**: Assumes Gaussian distributions, sensitive to the initialization of parameters, computationally expensive.

5. **K-Medoids (PAM - Partitioning Around Medoids)**:

    - **Type**: Partitional clustering algorithm (similar to K-means).

    - **Use case**: Used when data contains outliers or is not suitable for K-means, as it minimizes the sum of dissimilarities rather than squared distances.

    - **How it works**: Instead of centroids, K-medoids uses actual data points as the "medoid" for each cluster. The algorithm iterates to find the best representative point (medoid) for each cluster.

    - **Advantages**: Less sensitive to outliers than K-means, works well with arbitrary distance measures.

    - **Disadvantages**: Computationally more expensive than K-means, especially for large datasets.

6. **Affinity Propagation**:

    - **Type**: Graph-based clustering algorithm.

    - **Use case**: Clusters data based on a message-passing model, where data points "send messages" to other points about how well they represent each other.

    - **How it works**: Each data point can potentially be a cluster center. The algorithm uses a similarity matrix to iteratively exchange messages to find the most representative cluster centers.

    - **Advantages**: No need to specify the number of clusters, can find varying cluster sizes.

    - **Disadvantages**: Requires careful tuning of hyperparameters like preference and damping, can be computationally expensive.

7. **Spectral Clustering**:

    - **Type**: Graph-based clustering algorithm.

    - **Use case**: Useful for non-convex clusters, works well in cases where clusters are connected by edges in a graph (e.g., image segmentation).

    - **How it works**: It uses the eigenvalues of the similarity matrix to perform dimensionality reduction before clustering in fewer dimensions. The data is treated as a graph, where nodes represent data points and edges represent similarities.

    - **Advantages**: Can handle complex cluster structures, suitable for non-convex shapes.

    - **Disadvantages**: Computationally expensive for large datasets, requires a similarity matrix and careful tuning.

8. **Mean Shift Clustering**:

    - **Type**: Density-based clustering algorithm.

    - **Use case**: Identifies clusters by shifting data points towards the region of highest density in the feature space.

    - **How it works**: The algorithm shifts a window (kernel) over the data, moving it towards the mean of points within the window until convergence. This results in the identification of dense regions or clusters.

    - **Advantages**: No need to specify the number of clusters, can detect arbitrarily shaped clusters.

    - **Disadvantages**: Computationally expensive, sensitive to the choice of window size (bandwidth), struggles with varying densities.

9. **Agglomerative Clustering**:

    - **Type**: Hierarchical clustering algorithm.

    - **Use case**: Useful for small datasets or when you need to understand the nested structure of data.

    - **How it works**: The algorithm starts with each data point as its own cluster and progressively merges the closest clusters based on some distance measure until a stopping criterion is reached.

    - **Advantages**: Does not require the number of clusters to be pre-specified, produces a hierarchical structure.

    - **Disadvantages**: Not efficient for large datasets, sensitive to the choice of distance measure.

10. **Self-Organizing Maps (SOM)**:

    - **Type**: Neural network-based clustering algorithm.

    - **Use case**: Useful for visualizing high-dimensional data in lower dimensions, often used in unsupervised learning tasks.

    - **How it works**: SOM maps high-dimensional data to a lower-dimensional grid (typically 2D) while preserving topological relationships. The neurons in the grid adjust their weights to represent the data.

    - **Advantages**: Can visualize high-dimensional data, good for exploratory analysis.

    - **Disadvantages**: Sensitive to initialization, not as interpretable as other clustering methods.



#### Choosing the Right Model:

- **K-Means**: Suitable for spherical clusters and when you know the number of clusters beforehand.

- **Hierarchical**: Ideal for small datasets and when you want to visualize relationships between clusters.

- **DBSCAN**: Best when dealing with noise and non-convex clusters.

- **GMM**: Works well when you suspect that your data might come from several overlapping distributions.

- **K-Medoids**: Useful when dealing with outliers or non-Euclidean distance measures.

- **Spectral & Mean Shift**: Works well for complex, non-linear clusters.

#### Links:

- [[Clustering Algorithms Cheat Sheet]]

- [[Evaluating Clustering Models]]

- [[Dimensionality Reduction Techniques]]

---

This note should help clarify the various clustering models and guide you in selecting the appropriate one for your data based on its characteristics.

