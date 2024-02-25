import timeit
import random

# Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Generate random data sets
data_sets = {
    "Small": [random.randint(0, 1000) for _ in range(100)],
    "Medium": [random.randint(0, 1000) for _ in range(1000)],
    "Large": [random.randint(0, 1000) for _ in range(10000)]
}

# Compare execution time of different sorting algorithms
for name, data in data_sets.items():
    print(f"Data Set: {name}")
    
    # Merge Sort
    merge_time = timeit.timeit(lambda: merge_sort(data.copy()), number=1)
    print(f"Merge Sort Time: {merge_time}")

    # Insertion Sort
    insertion_time = timeit.timeit(lambda: insertion_sort(data.copy()), number=1)
    print(f"Insertion Sort Time: {insertion_time}")

    # Timsort (Python's built-in sorting)
    timsort_time = timeit.timeit(lambda: sorted(data.copy()), number=1)
    print(f"Timsort Time: {timsort_time}")

    print()
