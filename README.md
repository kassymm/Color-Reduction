# Color Reduction Project

This project applies K-means clustering for color reduction in images. By grouping similar colors, it reduces the overall number of unique colors while preserving the visual fidelity of the original image. This approach is efficient and visually appealing for applications where color constraints are essential, such as digital art, compression, and design.

<div style="display: flex; justify-content: space-around;">
  <img src="images/gandalf.jpg" alt="Original Image" width="45%">
  <img src="images/gandalf_out.jpg" alt="Color Reduced Image" width="45%">
</div>

## Repository Structure

**recolor.py** file implements KMeans algorithm (Question 1);
**KMeansIP.py** file finds all possible clusters with a cost less than the value obtained my KMeans;
**dat_get.py** file takes the output from KMeansIP.py functions and writes a data.dat file for GLPK;
**problem.mod** sets the problem for GLPK;
**data.dat** contains the inputs for GLPK;
**output.txt** contains the output of the GLPK and the optimal objective function value (255337500.869213);
**LinearProblem.pdf** describes the IP problem.
**images** folder contains application examples.

## Key Features

- **K-means Clustering**: Implements an optimized version of K-means clustering to reduce colors.
- **Backtracking Optimization**: Uses a backtracking approach to select optimal cluster centroids, focusing on minimizing redundant clusters and computational load.
- **Cost Constraint**: Limits clusters based on a cost threshold (M), ensuring balanced and visually consistent clusters.
- **Efficient Initialization**: Avoids empty clusters by initializing centroids with distinct RGB values, reducing processing time and ensuring convergence.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/kassymm/Color-Reduction.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Color-Reduction
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

**Running the Color Reduction Algorithm**:
   Run the main script to perform 10 color reduction on an example image:
   ```bash
   python recolor.py images/image.png images/reduced_image.png 10
   ```


## Mathematical Formulation

The color reduction process relies on K-means clustering combined with Integer Programming for optimal cluster selection:

- **Objective**: Minimize the total clustering cost.
- **Constraints**: Ensure each pixel is assigned to one cluster, with a limited number of clusters (`k`).

Refer to the detailed formulation in `LineraProblem.pdf` for an in-depth explanation of clustering constraints and optimization conditions.

## Results

After processing, results are saved in the `output.txt` file. Sample images demonstrate the effect of color reduction, retaining visual quality with fewer colors.

## Future Improvements

- **Enhanced Color Selection**: Experiment with different color selection techniques for better visual outcomes.
- **Adaptive Clustering**: Integrate adaptive clustering based on image content for more tailored reductions.
- **Real-Time Processing**: Optimize code for real-time color reduction on larger images.

## Contributing

Feel free to open issues or pull requests to suggest improvements, fix bugs, or add new features.

---

This README provides an overview of the project structure, key functionalities, setup instructions, and usage guidelines. Enjoy exploring color reduction with K-means clustering!
