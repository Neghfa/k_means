# K-Means Clustering Algorithm in Python

## Overview
This project implements the K-Means clustering algorithm to group 3D data points into a specified number of clusters (k). The algorithm iteratively updates centroids based on the mean of assigned points until convergence is achieved within a given accuracy.

## Features
- Clusters 3D points from a dataset into k groups.
- Includes built-in functions to:
    - Calculate distances between points.
    - Assign points to the nearest centroid.
    - Update centroids based on assigned points.
    - Check for convergence.

## Steps
1. Randomly initializes k centroids from the dataset.
2. Assigns points to the nearest centroid.
3. Updates centroids based on the mean of assigned points.
4. Repeats until centroids converge to within the specified accuracy.

## Requirements
- A dataset file (thepoints.txt) with 3D points with format like below

```python
x1, y1, z1
x2, y2, z2
...
```

