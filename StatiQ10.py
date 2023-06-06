import math

def binomial_probability(n, k, p):
    """
    Calculates the binomial probability of k successes in n trials with success probability p.
    """
    q = 1 - p
    coefficient = math.comb(n, k)
    probability = coefficient * (p**k) * (q**(n-k))
    return probability

def expected_value(n, p):
    """
    Calculates the expected value (mean) of a binomial distribution with n trials and success probability p.
    """
    return n * p

# Given data
n = 500  # Total number of bulbs
p = 0.05  # Probability of a bulb being defective

# a. Probability that exactly 20 bulbs are defective
probability_20_defective = binomial_probability(n, 20, p)

# b. Probability that at least 10 bulbs are defective
probability_at_least_10_defective = sum(binomial_probability(n, k, p) for k in range(10, n+1))

# c. Probability that at most 15 bulbs are defective (complement of at least 16 defective)
probability_at_most_15_defective = 1 - sum(binomial_probability(n, k, p) for k in range(16, n+1))

# d. Expected number of defective bulbs in a batch of 500
expected_defective_bulbs = expected_value(n, p)

# Print the results
print("a. Probability of exactly 20 defective bulbs:", probability_20_defective)
print("b. Probability of at least 10 defective bulbs:", probability_at_least_10_defective)
print("c. Probability of at most 15 defective bulbs:", probability_at_most_15_defective)
print("d. Expected number of defective bulbs in a batch of 500:", expected_defective_bulbs)
