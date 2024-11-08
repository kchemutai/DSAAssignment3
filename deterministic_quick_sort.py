def deterministic_quicksort(arr, low, high):
    if low < high:
        pivot_index = median_of_three_partition(arr, low, high)
        deterministic_quicksort(arr, low, pivot_index - 1)
        deterministic_quicksort(arr, pivot_index + 1, high)

def median_of_three_partition(arr, low, high):
    # Select median of the first, middle, and last elements as pivot
    mid = (low + high) // 2
    pivot_candidates = [(arr[low], low), (arr[mid], mid), (arr[high], high)]
    pivot_candidates.sort()  # Sort to find the median
    pivot_value, pivot_index = pivot_candidates[1]  # Choose the median value as pivot
    arr[high], arr[pivot_index] = arr[pivot_index], arr[high]  # Move pivot to end
    return partition(arr, low, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
