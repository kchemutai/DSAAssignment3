# DSAAssignment3

uCumberlands DSA

Assignment 3: Understanding Algorithm Efficiency and Scalability
Part 1: Randomized Quicksort Analysis

1. Implementation

- Implement the Randomized Quicksort algorithm where the pivot element is chosen uniformly at random from the subarray being partitioned.
- Ensure that your implementation is efficient and handles various edge cases, such as arrays with repeated elements, empty arrays, and already sorted arrays.

2. Analysis

- Provide a rigorous analysis of the average-case time complexity of Randomized Quicksort.
- Clearly explain why the average-case time complexity is \(O(n \log n)\).
- Use concepts such as indicator random variables or recurrence relations in your analysis to demonstrate your understanding.

3. Comparison
   ![alt text](image.png)

- Empirically compare the running time of Randomized Quicksort with Deterministic Quicksort (using the first element as the pivot) on different input sizes and distributions:
  - Randomly generated arrays
  - Already sorted arrays
  - Reverse-sorted arrays
  - Arrays with repeated elements
- Discuss the observed differences in running time and relate them to your theoretical analysis. Explain any discrepancies between the empirical results and the expected theoretical performance.
  Part 2: Hashing with Chaining

1. Implementation
   Here is the GitHub implementation of the Hash Table:

2. Analysis

Summary

1. Expected Operation Times: With a low load factor and simple uniform hashing, hash table operations (insert, search, and delete) generally take O (1) time on average. This is because each slot has a short chain, keeping operations efficient.
2. Impact of Load Factor: The load factor (ratio of elements to slots) directly affects performance. A high load factor leads to longer chains, slowing down operations and potentially degrading performance to O(n). Keeping the load factor low (typically below 0.7) helps maintain efficient operations.
3. Strategies to Maintain Efficiency:
   o Dynamic Resizing: Increase the table size when the load factor grows, and rehash elements to evenly distribute them across the table, reducing chain length.
   o Effective Hash Function: Use a well-distributed hash function to minimize collisions and ensure even key distribution.
   o Alternative Collision Handling: Consider advanced techniques like open addressing or cuckoo hashing to handle collisions efficiently.
   By managing the load factor and using effective hashing techniques, a hash table can maintain close to constant-time performance for insertions, searches, and deletions, even as it grows.
