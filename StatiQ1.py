import pandas as pd
import numpy as np

# Create a DataFrame with SAT scores and college GPA data
data = {
    'SAT Scores': [1350, 1400, 1500, 1550, 1600],
    'College GPA': [3.0, 3.2, 3.5, 3.7, 4.0]
}
df = pd.DataFrame(data)

# Calculate statistics
correlation_coefficient = df['SAT Scores'].corr(df['College GPA'])
mean_sat_scores = np.mean(df['SAT Scores'])
mean_college_gpa = np.mean(df['College GPA'])
std_sat_scores = np.std(df['SAT Scores'])
std_college_gpa = np.std(df['College GPA'])

# Print the statistics
print("Correlation Coefficient:", correlation_coefficient)
print("Mean SAT Scores:", mean_sat_scores)
print("Mean College GPA:", mean_college_gpa)
print("Standard Deviation of SAT Scores:", std_sat_scores)
print("Standard Deviation of College GPA:", std_college_gpa)
