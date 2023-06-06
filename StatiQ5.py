p_company_A = 0.8  # Probability of selecting a taxi from Company A
p_company_B = 0.2  # Probability of selecting a taxi from Company B

p_late_given_A = 0.05  # Probability of a taxi from Company A being late
p_late_given_B = 0.10  # Probability of a taxi from Company B being late

# Calculate the probability that a randomly selected taxi is late
p_late = p_company_A * p_late_given_A + p_company_B * p_late_given_B

# Calculate the probability that a late taxi belongs to Company A using Bayes' theorem
p_A_given_late = (p_company_A * p_late_given_A) / p_late

print("The probability that a randomly selected late taxi belongs to Company A is:", p_A_given_late)
