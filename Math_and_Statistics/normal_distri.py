import numpy as np
import matplotlib.pyplot as plt

# Parameters for the normal distribution
mean = 0    # mean
std_dev = 1 # standard deviation
num_samples = 1000 # number of samples

# Generate random samples from a normal distribution
samples = np.random.normal(mean, std_dev, num_samples)

# Plotting the histogram
plt.figure(figsize=(10, 6))
plt.hist(samples, bins=30, density=True, alpha=0.6, color='b')

# Plotting the probability density function (PDF)
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = np.exp(-0.5 * ((x - mean) / std_dev) ** 2) / (std_dev * np.sqrt(2 * np.pi))
plt.plot(x, p, 'k', linewidth=2)

title = "Normal Distribution\nMean = {:.2f}, Std Dev = {:.2f}".format(mean, std_dev)
plt.title(title)
plt.xlabel('Value')
plt.ylabel('Density')
plt.grid()
plt.show()
