import heapq

def kthSmallest(matrix, k):
    n = len(matrix)
    min_heap = []
    
    # Start by adding the first element from each row
    for row in range(n):
        heapq.heappush(min_heap, (matrix[row][0], row, 0))
    
    # pick the smallest element k times
    for _ in range(k):
        value, row, col = heapq.heappop(min_heap)
        
        # Add the next element from the same row if there is one
        if col + 1 < n:
            heapq.heappush(min_heap, (matrix[row][col + 1], row, col + 1))
    
    return value

# Test case 1
matrix = [
    [1, 5, 9],
    [10, 11, 13],
    [12, 13, 15]
]
k = 8
print(f"Test 1 - k={k}")
print(f"Result: {kthSmallest(matrix, k)}")

# Test case 2
matrix = [
    [1, 2],
    [3, 4]
]
k = 3
print(f"\nTest 2 - k={k}")
print(f"Result: {kthSmallest(matrix, k)}")

# Test case 3
matrix = [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]
k = 5
print(f"\nTest 3 - k={k}")
print(f"Result: {kthSmallest(matrix, k)}")

# Test case 4
matrix = [
    [-5, -3],
    [-2, 0]
]
k = 2
print(f"\nTest 4 - k={k}")
print(f"Result: {kthSmallest(matrix, k)}")