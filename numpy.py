import numpy as np

# Step 1: Simulate rolling two dice 1000 times
rolls = np.random.randint(1, 7, size=(1000, 2))  # 1000 rolls × 2 dice
print("🎲 First 10 Rolls:\n", rolls[:10])

# Step 2: Calculate the sum of both dice
sums = np.sum(rolls, axis=1)

# Step 3: Frequency of each possible sum (2–12)
unique, counts = np.unique(sums, return_counts=True)
print("\nSum Frequencies:")
for u, c in zip(unique, counts):
    print(f"Sum {u}: {c} times")

# Step 4: Probability of each sum
probabilities = counts / len(sums)
print("\nProbabilities of Each Sum:")
for u, p in zip(unique, probabilities):
    print(f"Sum {u}: {p:.2%}")

# Step 5: Most common sum
most_common = unique[np.argmax(counts)]
print("\nMost Common Sum:", most_common)
