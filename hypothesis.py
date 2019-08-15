import math
import random

def normal_cdf(x, mu=0, sigma=1):
	return (1 + math.erf((x - mu) /math.sqrt(2)/ sigma)) /2

def inverse_normal_cdf(p, mu=0, sigma=1, tolerance=0.00001):
	if mu != 0 or sigma != 1:
		return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)
    
	low_z, low_p = -10.0, 0
	hi_z, hi_p = 10.0, 1

	while hi_z - low_z > tolerance:
		mid_z = (low_z + hi_z) / 2
		mid_p = normal_cdf(mid_z)
		if mid_p < p:
			low_z, low_p = mid_z, mid_p
		elif mid_p > p:
			hi_z, hi_p = mid_z, mid_p
		else:
			break
        
	return mid_z

def nornal_approximation_to_binomial(n,p):
    mu = n * p
    sigma = math.sqrt(p * (1-p) * n)
    return mu, sigma

normal_probability_below = normal_cdf

def normal_probability_above(lo, mu=0, sigma=1):
    return 1 - normal_cdf(lo, mu, sigma)

def normal_probability_between(lo, mu=0, sigma=1):
    return normal_cdf(hi, mu, sigma) - normal_cdf(lo, mu, sigma)

def normal_probability_outside(lo, mu=0, sigma=1):
    return 1 - normal_probability_between(lo, hi, mu, sigma)
    
def normal_upper_bound(probability, mu=0, sigma=1):
    return inverse_normal_cdf(probability, mu, sigma)

def normal_lower_bound(probability, mu=0, sigma=1):
    return inverse_normal_cdf(1 - probability, mu, sigma)

def normal_two_sided_bounds(probability, mu=0, sigma=1):
    tail_probability = (1-probability) / 2
    upper_bound = normal_lower_bound(tail_probability, mu, sigma)
    lower_bound = normal_upper_bound(tail_probability, mu, sigma)
    return lower_bound, upper_bound



mu_0, sigma_0 = nornal_approximation_to_binomial(1000, 0.5)

print(normal_two_sided_bounds(0.95, mu_0, sigma_0))

