---
type: HowTo
---

# Popular Plots in R and Python

This document outlines some of the most popular plots used in data visualization in R and Python, along with example code to create them. Each section includes code snippets for generating these plots using common libraries: `ggplot2` in R and `matplotlib`/`seaborn` in Python.

## 1. Scatter Plot

Scatter plots display individual data points on a two-dimensional plane, useful for showing relationships between two continuous variables.

### R (ggplot2)

```R
# Load library
library(ggplot2)

# Sample data
data <- mtcars

# Scatter plot
ggplot(data, aes(x = mpg, y = wt)) +
  geom_point() +
  labs(title = "Scatter Plot: MPG vs Weight", x = "Miles per Gallon", y = "Weight")
ggsave("scatter_r.png")
```

### Python (matplotlib)

```python
import matplotlib.pyplot as plt
import pandas as pd

# Sample data
data = pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/mtcars.csv")

# Scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(data['mpg'], data['wt'])
plt.title("Scatter Plot: MPG vs Weight")
plt.xlabel("Miles per Gallon")
plt.ylabel("Weight")
plt.savefig("scatter_python.png")
plt.close()
```

## 2. Line Plot

Line plots are used to display data points connected by straight lines, often for time series or sequential data.

### R (ggplot2)

```R
# Load library
library(ggplot2)

# Sample data
data <- data.frame(
  time = 1:10,
  value = c(2, 4, 5, 4, 6, 7, 8, 9, 10, 12)
)

# Line plot
ggplot(data, aes(x = time, y = value)) +
  geom_line() +
  geom_point() +
  labs(title = "Line Plot: Value over Time", x = "Time", y = "Value")
ggsave("line_r.png")
```

### Python (matplotlib)

```python
import matplotlib.pyplot as plt
import numpy as np

# Sample data
time = np.arange(1, 11)
value = [2, 4, 5, 4, 6, 7, 8, 9, 10, 12]

# Line plot
plt.figure(figsize=(8, 6))
plt.plot(time, value, marker='o')
plt.title("Line Plot: Value over Time")
plt.xlabel("Time")
plt.ylabel("Value")
plt.savefig("line_python.png")
plt.close()
```

## 3. Bar Plot

Bar plots represent categorical data with rectangular bars, useful for comparing quantities across categories.

### R (ggplot2)

```R
# Load library
library(ggplot2)

# Sample data
data <- data.frame(
  category = c("A", "B", "C", "D"),
  value = c(10, 20, 15, 25)
)

# Bar plot
ggplot(data, aes(x = category, y = value)) +
  geom_bar(stat = "identity") +
  labs(title = "Bar Plot: Category Counts", x = "Category", y = "Value")
ggsave("bar_r.png")
```

### Python (seaborn)

```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Sample data
data = pd.DataFrame({
    'category': ['A', 'B', 'C', 'D'],
    'value': [10, 20, 15, 25]
})

# Bar plot
plt.figure(figsize=(8, 6))
sns.barplot(x='category', y='value', data=data)
plt.title("Bar Plot: Category Counts")
plt.xlabel("Category")
plt.ylabel("Value")
plt.savefig("bar_python.png")
plt.close()
```

## 4. Histogram

Histograms display the distribution of a continuous variable by dividing it into bins.

### R (ggplot2)

```R
# Load library
library(ggplot2)

# Sample data
data <- mtcars

# Histogram
ggplot(data, aes(x = mpg)) +
  geom_histogram(binwidth = 2, fill = "blue", color = "black") +
  labs(title = "Histogram: MPG Distribution", x = "Miles per Gallon", y = "Count")
ggsave("histogram_r.png")
```

### Python (matplotlib)

```python
import matplotlib.pyplot as plt
import pandas as pd

# Sample data
data = pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/mtcars.csv")

# Histogram
plt.figure(figsize=(8, 6))
plt.hist(data['mpg'], bins=10, color='blue', edgecolor='black')
plt.title("Histogram: MPG Distribution")
plt.xlabel("Miles per Gallon")
plt.ylabel("Count")
plt.savefig("histogram_python.png")
plt.close()
```

## 5. Box Plot

Box plots summarize the distribution of data, showing median, quartiles, and potential outliers.

### R (ggplot2)

```R
# Load library
library(ggplot2)

# Sample data
data <- mtcars

# Box plot
ggplot(data, aes(x = factor(cyl), y = mpg)) +
  geom_boxplot() +
  labs(title = "Box Plot: MPG by Cylinder", x = "Cylinders", y = "Miles per Gallon")
ggsave("box_r.png")
```

### Python (seaborn)

```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Sample data
data = pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/mtcars.csv")

# Box plot
plt.figure(figsize=(8, 6))
sns.boxplot(x='cyl', y='mpg', data=data)
plt.title("Box Plot: MPG by Cylinder")
plt.xlabel("Cylinders")
plt.ylabel("Miles per Gallon")
plt.savefig("box_python.png")
plt.close
```