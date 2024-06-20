import numpy as np
from sklearn.cluster import KMeans

def k_means_clustering(data, num_clusters):
    kmeans = KMeans(n_clusters=num_clusters, random_state=42, n_init=10)
    kmeans.fit(data)
    return kmeans.labels_
