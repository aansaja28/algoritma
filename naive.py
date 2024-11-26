import random

random_numbers = [random.randint(0, 100) for _ in range(50)]

# Naive Sort 
def naive_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

numbers_naive = random_numbers.copy()

print("Original Numbers:", random_numbers)
print("\nNaive Sort Result:", naive_sort(numbers_naive))