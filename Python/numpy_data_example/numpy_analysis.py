import numpy as np

# Generate random data.
data = np.random.randint(0, 100, size=(5,5))

# Basic analysis.
mean_value = np.mean(data)
max_value = np.max(data)
min_value = np.min(data)

# Print results.
print("Generated Data: ")
print(*data, sep="\n")
print(f"Analysis: \nMean: {mean_value}\nMax: {max_value}\nMin: {min_value}")
