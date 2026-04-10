import time
import random

# Linear Search
def linear_search(arr, target):
    comparisons = 0

    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == target:
            return i, comparisons

    return -1, comparisons

# Binary Search
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    comparisons = 0

    while left <= right:
        mid = (left + right) // 2
        comparisons += 1

        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1, comparisons

# Generate Data
size = 10000
arr = sorted(random.sample(range(1, 100000), size))

# Pick a random target from the array
target = random.choice(arr)

print(f"Target to find: {target}\n")

# Linear Search Timing
start = time.time()
index, comparisons = linear_search(arr, target)
end = time.time()

print("Linear Search:")
print(f"Index found: {index}")
print(f"Comparisons: {comparisons}")
print(f"Time taken: {end - start:.6f} seconds\n")

# Binary Search Timing
start = time.time()
index, comparisons = binary_search(arr, target)
end = time.time()

print("Binary Search:")
print(f"Index found: {index}")
print(f"Comparisons: {comparisons}")
print(f"Time taken: {end - start:.6f} seconds\n")