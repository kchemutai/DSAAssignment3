import time
import random
import string

class HashTable:
    def __init__(self, size=1000):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        for item in self.table[index]:
            if item[0] == key:
                item[1] = value
                return
        self.table[index].append([key, value])

    def search(self, key):
        index = self.hash_function(key)
        for item in self.table[index]:
            if item[0] == key:
                return item[1]
        return None

    def delete(self, key):
        index = self.hash_function(key)
        for i, item in enumerate(self.table[index]):
            if item[0] == key:
                self.table[index].pop(i)
                return True
        return False

# Helper function to generate random keys
def generate_random_string(length=8):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

# Function to run time tests for hash table operations
def run_hash_table_tests():
    hash_table = HashTable(size=1000)
    
    # Generate test data: 10,000 random key-value pairs
    num_elements = 10000
    test_data = [(generate_random_string(), random.randint(1, 1000)) for _ in range(num_elements)]
    
    # Measure Insert Time
    start_time = time.time()
    for key, value in test_data:
        hash_table.insert(key, value)
    insert_time = time.time() - start_time
    print(f"Insert operation time for {num_elements} elements: {insert_time:.6f} seconds")

    # Measure Search Time
    start_time = time.time()
    for key, _ in test_data:
        hash_table.search(key)
    search_time = time.time() - start_time
    print(f"Search operation time for {num_elements} elements: {search_time:.6f} seconds")
    
    # Measure Delete Time
    start_time = time.time()
    for key, _ in test_data:
        hash_table.delete(key)
    delete_time = time.time() - start_time
    print(f"Delete operation time for {num_elements} elements: {delete_time:.6f} seconds")

    # Display a summary
    print("\nSummary of Hash Table Performance:")
    print(f"Insertion time for {num_elements} elements: {insert_time:.6f} seconds")
    print(f"Search time for {num_elements} elements: {search_time:.6f} seconds")
    print(f"Deletion time for {num_elements} elements: {delete_time:.6f} seconds")

# Run tests
if __name__ == "__main__":
    run_hash_table_tests()
