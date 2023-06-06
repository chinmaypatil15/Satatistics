from scipy.stats import ttest_ind

# Group A data
mean_A = 2.5
std_A = 0.8
n_A = 30

# Group B data
mean_B = 2.2
std_B = 0.6
n_B = 30

# Perform t-test
t_statistic, p_value = ttest_ind(
    a=[mean_A] * n_A,  # Creating a list of mean_A repeated n_A times
    b=[mean_B] * n_B,  # Creating a list of mean_B repeated n_B times
    equal_var=False  # Assuming unequal variances
)

# Define the significance level
alpha = 0.05

# Compare p-value with significance level
if p_value < alpha:
    print("Reject the null hypothesis")
else:
    print("Fail to reject the null hypothesis")

# Conclusion
if p_value < alpha:
    print("There is a significant difference in the mean improvement scores between the two groups.")
else:
    print("There is no significant difference in the mean improvement scores between the two groups.")
