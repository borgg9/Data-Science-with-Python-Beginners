import math
import random

def normal_cdf(x, mu=0, sigma=1):
	return (1 + math.erf((x - mu) /math.sqrt(2)/ sigma)) /2

def inverse_normal_cdf(p, mu=0, sigma=1, tolerance=0.00001):
	if mu != 0 or sigma != 1:
		return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)

	low_z, low_p = -10.0, 0
	hig_z, hig_p = 10.0, 1

	while hig_z - low_z > tolerance:
		mid_z = (low_z + hig_z) / 2
		mid_p = normal_cdf(mid_z)
		if mid_p < p:
			low_z, low_p = mid_z, mid_p
		elif mid_p > p:
			hig_z, hig_p = mid_z, mid_p
		else:
			break

	return mid_z

def normal_approximation_to_binomial(n,p):
	mu = n * p
	sigma = math.sqrt(p * (1-p) * n)
	return mu, sigma


normal_probability_below = normal_cdf

# it's above the threshold if it's not below the threshold
def normal_probability_above(lo, mu=0, sigma=1):
	return 1 - normal_cdf(lo, mu, sigma)

# it's between if it's less than hi, but not less than lo
def normal_probability_between(lo, hi, mu=0, sigma=1):
	return normal_cdf(hi, mu, sigma) - normal_cdf(lo, mu, sigma)

# it's outside if it's not between
def normal_probability_outside(lo, hi, mu=0, sigma=1):
	return 1 - normal_probability_between(lo, hi, mu=0, sigma=1)



# do the reverse, find either the nontail region or the (symmetric) interval around the mean that accounts fro a certain level of likelihood.

def normal_upper_bound(probability, mu=0, sigma=1):
	#return the z for which P(Z <= z) = probability
	return inverse_normal_cdf(probability, mu, sigma)

def normal_lower_bound(probability, mu=0, sigma=1):
	#return the z for which P(Z >= z) = probability
	return inverse_normal_cdf(1 - probability, mu, sigma)

def normal_two_sided_bounds(probability, mu=0, sigma=1):
	#return the symmetric (about the mean) bounds that contain the specified probability
	tail_probability = (1 - probability) / 2
	upper_bound = normal_lower_bound(tail_probability,mu, sigma)
	lower_bound = normal_upper_bound(tail_probability, mu, sigma)
	return lower_bound, upper_bound

mu_0, sigma_0 = normal_approximation_to_binomial(1000, 0.5)

print (normal_two_sided_bounds(0.95, mu_0, sigma_0))

# we can calculate the power of the test with
# 95% bounds based on assumption p is 0.5
lo, hi = normal_two_sided_bounds(0.95, mu_0, sigma_0)

# actual mu and sigma based on p = 0.55
mu_1, sigma_1 = normal_approximation_to_binomial(1000, 0.55)

# a type 2 error means we fail to reject the null hypothesis
# which will happen when X is still in our original interval
type_2_probability = normal_probability_between(lo, hi, mu_1, sigma_1)
power = 1 - type_2_probability


print (power)

# one-sided test
hi = normal_upper_bound(0.95, mu_0, sigma_0)
print ("hi is: ", hi)

type_2_probability= normal_probability_below(hi, mu_1, sigma_1)
power = 1 - type_2_probability
print (power)

# alternative way of thinking aobut the test involves p-values
# for the two-sided test
def two_sided_p_value(x, mu=0, sigma=1):
	if x >= mu:
		# if x is greater than the mean, the tail is what's greater than x 
		return 2 * normal_probability_above(x, mu, sigma)
	else:
		# if x is less than the mean, the tail is what's less than x
		return 2 * normal_probability_below(x, mu, sigma)

print (two_sided_p_value(529.5, mu_0, sigma_0))

# this is a sensible estimate that is with a simulation
extreme_value_count = 0
for _ in range(1000):
	num_heads = sum(1 if random.random() < 0.5 else 0
					for _ in range(1000))
	if num_heads >= 530 or num_heads <= 470:
		extreme_value_count += 1

print (extreme_value_count/100000)

print (two_sided_p_value(531.5, mu_0, sigma_0))

upper_p_value = normal_probability_above
lowe_p_value = normal_probability_below

print (upper_p_value(524.5, mu_0, sigma_0))
print (upper_p_value(526.5, mu_0, sigma_0))