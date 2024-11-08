from recolor import KMeans, load_image
from KMeansIP import upper_bound, group_pixels_by_color, precompute_color_distances, find_clusters_backtracking

pixels, height, width = load_image("20col.png")
unique_colors, color_count = group_pixels_by_color(pixels)
distance_matrix = precompute_color_distances(unique_colors = unique_colors)
color_index = {tuple(color): idx for idx, color in enumerate(unique_colors)}
kmeans = KMeans(num_clusters=8, num_init=100)
quantized_pixels, lowest_cost = kmeans.fit(pixels.reshape(-1, 3), )
possible_clusters, costs = find_clusters_backtracking(unique_colors, color_count, distance_matrix, color_index, lowest_cost)



clusters_matrix = []
for cluster in possible_clusters:
    colors_binary = []
    for color in unique_colors:
        if tuple(color) in map(tuple, cluster):
            colors_binary.append(1)
        else:
            colors_binary.append(0)
    clusters_matrix.append(colors_binary)

print("Clusters Matrix is formed")

def write_dat_file(clusters_matrix, costs, num_clusters=8):
    with open('data.dat', 'w') as f:

        f.write(f"param m := {len(clusters_matrix)};\n\n")
        f.write("param n := 20;\n\n")
        f.write("param k := 8;\n\n")


        f.write("param D :=\n")
        for i, cost in enumerate(costs, start=1):
            f.write(f"{i} {cost}\n")
        f.write(";\n\n")


        f.write("param C : " + " ".join(map(str, range(1, len(clusters_matrix[0]) + 1))) + " :=\n")
        for i, row in enumerate(clusters_matrix, start=1):
            row_str = " ".join(map(str, row))
            f.write(f"{i} {row_str}\n")
        f.write(";\n\n")

        f.write("end;")
        f.write("\n")


write_dat_file(clusters_matrix, costs)
