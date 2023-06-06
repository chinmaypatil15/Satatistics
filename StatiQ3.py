import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Read the CSV file
data = pd.read_csv('G:\project\Satatistics\data.csv')

# Extract the 'Blood Pressure Before' and 'Blood Pressure After' columns
bp_before = data[' Blood Pressure Before (mmHg)']
bp_after = data[' Blood Pressure After (mmHg)']

# Measure the dispersion in both columns (Range and Interquartile Range)
bp_before_range = np.ptp(bp_before)
bp_after_range = np.ptp(bp_after)
bp_before_iqr = np.percentile(bp_before, 75) - np.percentile(bp_before, 25)
bp_after_iqr = np.percentile(bp_after, 75) - np.percentile(bp_after, 25)

# Interpretation of dispersion
print("Dispersion in Blood Pressure Before:", bp_before_range)
print("Dispersion in Blood Pressure After:", bp_after_range)
print("Interquartile Range (IQR) of Blood Pressure Before:", bp_before_iqr)
print("Interquartile Range (IQR) of Blood Pressure After:", bp_after_iqr)

# Calculate the mean and 5% confidence interval
bp_before_mean = np.mean(bp_before)
bp_after_mean = np.mean(bp_after)
confidence_interval = stats.norm.interval(0.95, loc=bp_before_mean, scale=stats.sem(bp_before))

# Plot the mean and confidence interval
plt.bar(['Blood Pressure Before', 'Blood Pressure After'], [bp_before_mean, bp_after_mean])
plt.errorbar(['Blood Pressure Before'], [bp_before_mean], yerr=[confidence_interval[1]-bp_before_mean], fmt='o', capsize=5, label='95% CI')
plt.ylabel('Mean')
plt.title('Mean of Blood Pressure Before and After')
plt.legend()
plt.show()

# Calculate the Mean Absolute Deviation (MAD) and Standard Deviation (SD)
bp_before_mad = np.mean(np.abs(bp_before - np.mean(bp_before)))
bp_after_mad = np.mean(np.abs(bp_after - np.mean(bp_after)))
bp_before_sd = np.std(bp_before)
bp_after_sd = np.std(bp_after)

# Interpretation of MAD and SD
print("Mean Absolute Deviation (MAD) of Blood Pressure Before:", bp_before_mad)
print("Mean Absolute Deviation (MAD) of Blood Pressure After:", bp_after_mad)
print("Standard Deviation (SD) of Blood Pressure Before:", bp_before_sd)
print("Standard Deviation (SD) of Blood Pressure After:", bp_after_sd)

# Calculate the correlation coefficient and p-value
correlation_coefficient, p_value = stats.pearsonr(bp_before, bp_after)

# Interpretation of correlation coefficient and significance level
print("Correlation Coefficient:", correlation_coefficient)
print("p-value:", p_value)
if p_value < 0.01:
    print("The correlation is statistically significant at the 1% level.")
else:
    print("The correlation is not statistically significant at the 1% level.")
