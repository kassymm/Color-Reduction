import numpy as np
from recolor import KMeans


def upper_bound(pixels, num_clusters = 8):
    kmeans = KMeans(num_clusters)
    quantized_pixels, lowest_cost = kmeans.fit(pixels.reshape(-1, 3))
    return lowest_cost

def group_pixels_by_color(pixels):
    unique_colors, counts = np.unique(pixels.reshape(-1, 3), axis=0, return_counts=True)
    color_count = dict(zip(map(tuple, unique_colors), counts))
    return unique_colors, color_count

def precompute_color_distances(unique_colors):
    unique_colors = unique_colors.astype(np.int64)
    diff = unique_colors[:, np.newaxis, :] - unique_colors[np.newaxis, :, :]
    distance_matrix = np.sum(diff ** 2, axis=2) 
    return distance_matrix


def calculate_cluster_cost(cluster, color_count, distance_matrix, color_index):
    indices = [color_index[tuple(color)] for color in cluster]
    cluster_color_counts = np.array([color_count[tuple(color)] for color in cluster])
    cluster_distances = distance_matrix[np.ix_(indices, indices)]
    weight_matrix = np.outer(cluster_color_counts, cluster_color_counts)
    total_weight = np.sum(cluster_color_counts)
    cost = np.sum(cluster_distances * weight_matrix) / (2 * total_weight)
    return cost

def find_clusters_backtracking(unique_colors, color_count, distance_matrix, color_index, M):

    clusters = []
    costs = []
    
    def backtrack(cluster, i):
        if len(cluster) > 0:
            cost = calculate_cluster_cost(cluster, color_count, distance_matrix, color_index)
            if cost <= M:
                clusters.append(list(cluster))
                costs.append(cost)
            else:
                return
        if i == len(unique_colors):
            return
        
        cluster.append(unique_colors[i])
        backtrack(cluster, i+1)
        cluster.pop()
        backtrack(cluster, i+1)

    backtrack([], 0)
    return clusters, costs











