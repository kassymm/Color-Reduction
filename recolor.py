from PIL import Image
import numpy as np
import argparse
from collections import defaultdict



def load_image(image_path):
    try:
        with Image.open(image_path).convert("RGB") as image:
            pixels = np.array(image)
            height, width, _ = pixels.shape
            return pixels, height, width

    except Exception as e:
        print(f"Can't load image: {e}")
        return None, None, None


def create_image(pixels, height, width, output_path = None):
    try:
        pixels = pixels.reshape(height, width, -1).astype(np.uint8)
        image = Image.fromarray(pixels, "RGB")
        if output_path:
            image.save(output_path)
            # print(f"Image saved to '{output_path}'")

        return image
    
    except Exception as e:
        print(f"Error creating image: {e}")
        return None
    

class KMeans:
    def __init__(self, num_clusters = 2, num_init = 25, max_iterations = 100, tolerance = 1e-6, random_seed = 0):
        self.num_clusters = num_clusters
        self.max_iterations = max_iterations
        self.tolerance = tolerance
        self.num_init = num_init
        self.random_seed = random_seed
    
    def fit(self, pixels):

        unique_colors = np.unique(pixels, axis=0)
        lowest_cost = np.inf

        # for i in range(self.num_init):
        i = 0
        while i < self.num_init:
            self.random_seed += 1
            np.random.seed(self.random_seed)
            indices = np.random.choice(len(unique_colors), self.num_clusters, replace = False)
            centroids = unique_colors[indices]
            cost = np.inf


            for _ in range(self.max_iterations):

                distances = np.linalg.norm(pixels[:, np.newaxis, :] - centroids, axis = 2)

                labels = np.argmin(distances, axis = 1)

                if len(np.unique(labels)) < self.num_clusters:
                    print("BOOM")
                    i -= 1
                    break

                centroids = np.array([pixels[labels == i].mean(axis=0) for i in range(self.num_clusters)])

                dist = np.sum((pixels - centroids[labels])**2, axis = 1)
                new_cost = np.sum(dist)


                # if np.linalg.norm(new_centroids - centroids) < self.tolerance:
                #     print(f"Stopped after {_} steps")
                #     break

                if new_cost > cost - self.tolerance:
                    print(f"Iteration {i+1}. Stopped after {_} steps. Cost = {cost}")
                    break
                cost = new_cost


            if cost < lowest_cost:
                lowest_cost = cost
                quantized_pixels = centroids[labels]
                # print(f"new centroids after step {_}:\n {centroids}")
            
            i += 1
        print(f"Lowest cost by kmeans: {lowest_cost}")
        return quantized_pixels, lowest_cost

def quantize_image(image_path, output_path, num_colors, random_seed = 0):

    pixels, height, width = load_image(image_path = image_path)
    kmeans = KMeans(num_clusters=num_colors)
    quantized_pixels, lowest_cost = kmeans.fit(pixels.reshape(-1, 3))
    create_image(quantized_pixels, height = height, width = width, output_path = output_path)
    # print(f"works for seed = {random_seed}")




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="KMeans Image Recoloring")
    parser.add_argument("input_image", type=str, help="Path to the input image")
    parser.add_argument("output_image", type=str, help="Path to save the output image")
    parser.add_argument("num_colors", type=int, help="Number of colors for quantization")

    args = parser.parse_args()

    quantize_image(args.input_image, args.output_image, args.num_colors, random_seed = 2)

