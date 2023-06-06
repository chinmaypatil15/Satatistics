import math

# Given regression equations
equation1 = lambda x: 2*x + 3 - 8
equation2 = lambda x: 2*x + x - 5

# Variance of X
variance_X = 4

# a. Variance of Y
# Calculate Y values using equation2
variance_Y = variance_X * (2**2)  # Variance of Y = Variance of X * (Slope of Y on X)^2

# b. Coefficient of determination of X and Y
# The coefficient of determination (R^2) is the square of the correlation coefficient (r),
# which is not provided in the given information, so we cannot calculate it.

# c. Standard error of estimate
# Standard error of estimate of X on Y
# We need the correlation coefficient to calculate this, which is not provided.
std_error_X_on_Y = None

# Standard error of estimate of Y on X
# We need the correlation coefficient to calculate this, which is not provided.
std_error_Y_on_X = None

# Print the results
print("Variance of Y:", variance_Y)
print("Coefficient of determination of X and Y: N/A")
print("Standard error of estimate of X on Y:", std_error_X_on_Y)
print("Standard error of estimate of Y on X:", std_error_Y_on_X)
