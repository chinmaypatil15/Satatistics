import numpy as np
from scipy.stats import norm

# Given information
mean_height = 170
std_deviation = 10
sample_size = 1000

# a. Percentage of individuals with heights between 160 cm and 180 cm
z_160 = (160 - mean_height) / std_deviation
z_180 = (180 - mean_height) / std_deviation
percentage_between_160_180 = norm.cdf(z_180) - norm.cdf(z_160)
print(f"Percentage of individuals between 160 cm and 180 cm: {percentage_between_160_180*100:.2f}%")

# b. Probability that the average height of 100 individuals is greater than 175 cm
sample_mean_std_deviation = std_deviation / np.sqrt(sample_size)
z_175 = (175 - mean_height) / sample_mean_std_deviation
probability_avg_height_gt_175 = 1 - norm.cdf(z_175)
print(f"Probability of average height > 175 cm for a sample of 100 individuals: {probability_avg_height_gt_175*100:.2f}%")

# c. Z-score corresponding to a height of 185 cm
z_185 = (185 - mean_height) / std_deviation
print(f"Z-score corresponding to a height of 185 cm: {z_185:.2f}")

# d. Height corresponding to the threshold of 5%
threshold_height = norm.ppf(0.05, mean_height, std_deviation)
print(f"Height corresponding to the 5% threshold: {threshold_height:.2f} cm")

# e. Coefficient of Variation (CV)
cv = (std_deviation / mean_height) * 100
print(f"Coefficient of Variation (CV): {cv:.2f}%")

# f. Skewness of the dataset
skewness = 0  # Given that skewness is approximately zero
print(f"Skewness of the dataset: {skewness}")
