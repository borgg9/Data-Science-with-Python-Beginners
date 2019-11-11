from matplotlib import pyplot as plt
import numpy as np

spread = np.random.rand(50) * 100
center = np.ones(25) * 50
flier_high = np.random.rand(10) * -100 + 100
flier_low = np.random.rand(10) * -100
data = np.concatenate((spread, center, flier_high, flier_low), 0)

#basic plot
plt.boxplot(data)
plt.show()

# Notches plot
plt.figure()
plt.boxplot(data, 1)
plt.show()

# change outlier point symbols
plt.figure()
plt.boxplot(data, 0, 'gD')
plt.show()

# horizontal boxes
plt.figure()
plt.boxplot(data, 0, 'rs', 0)
plt.show()

