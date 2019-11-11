import math
import random
from matplotlib import pyplot as plt
from collections import Counter

def bucketize(point, bucket_size):
    return bucket_size * math.floor(point / bucket_size)

def make_histogram(points, bucket_size):
    return Counter(bucketize(point, bucket_size) for point in points)
def plot_histogram(points, bucket_size, title=''):
    histogram = make_histogram(points, bucket_size)
    plt.bar(histogram.keys(), histogram.values(), width=bucket_size)
    plt.title(title)
    plt.show()    

random.seed(0)
uniform = [200 * random.random() - 100 for _ in range(10000)]
plot_histogram(uniform, 10, 'Uniform histogram')