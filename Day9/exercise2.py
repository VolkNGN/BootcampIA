import numpy as np

dataset = np.random.rand(100, 100)

filtered = dataset[dataset > 100]

print("Original Dataset:\n", dataset)
print("Filtered Values > 100:\n", filtered)
