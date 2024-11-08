import time
import random
import sys
from deterministic_quick_sort import deterministic_quicksort
from randomized_quick_sort import randomized_quicksort

# Temporarily increase recursion limit
sys.setrecursionlimit(2000)

# Function to measure time for sorting
def measure_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr, 0, len(arr) - 1)
    return time.time() - start_time

# Test cases
def run_tests():
    arrays = {
        "Randomly generated": [random.randint(1, 100) for _ in range(1000)],
        "Already sorted": list(range(1000)),
        "Reverse sorted": list(range(1000, 0, -1)),
        "Repeated elements": [5] * 1000 + [3] * 1000 + [7] * 1000
    }

    for description, array in arrays.items():
        # Make copies to avoid in-place sorting issues
        array_copy_for_randomized = array[:]
        array_copy_for_deterministic = array[:]
        
        # Measure time for Randomized Quicksort
        randomized_time = measure_time(randomized_quicksort, array_copy_for_randomized)
        
        # Measure time for Deterministic Quicksort
        deterministic_time = measure_time(deterministic_quicksort, array_copy_for_deterministic)
        
        # Display results
        print(f"{description} array:")
        print(f"  Randomized Quicksort time: {randomized_time:.6f} seconds")
        print(f"  Deterministic Quicksort time: {deterministic_time:.6f} seconds\n")

# Run all test cases
if __name__ == "__main__":
    run_tests()
