import pandas as pd
from scipy import stats

# Read the CSV file
data = pd.read_csv(r'G:\project\Satatistics\data.csv')

# Extract the 'Blood Pressure Before' and 'Blood Pressure After' columns
bp_before = data[' Blood Pressure Before (mmHg)']
bp_after = data[' Blood Pressure After (mmHg)']

# Compute the change in blood pressure
bp_change = bp_after - bp_before

# Perform the Shapiro-Wilk test for normality
statistic, p_value = stats.shapiro(bp_change)

# Interpret the results
alpha = 0.05
if p_value > alpha:
    print("The change in blood pressure follows a normal distribution.")
else:
    print("The change in blood pressure does not follow a normal distribution.")
