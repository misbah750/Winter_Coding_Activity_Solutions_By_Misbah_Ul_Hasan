def median_of_two_arrays(scoresA, scoresB):
    m, n = len(scoresA), len(scoresB)
    total = m + n
    
    
    steps_needed = total // 2 + 1
    
    i = j = 0
    prev = curr = 0
    
    # Walk through both arrays together picking the smaller value each time
    for step in range(steps_needed):
        prev = curr
        
        
        if i < m and (j >= n or scoresA[i] <= scoresB[j]):
            curr = scoresA[i]
            i += 1
        else:
            curr = scoresB[j]
            j += 1
    
    # Odd length
    if total % 2 == 1:
        return float(curr)
    # Even length
    else:
        return (prev + curr) / 2.0

# Test case 1
scoresA = [1, 3, 5]
scoresB = [2, 4, 6]
print(f"Test 1 - scoresA: {scoresA}, scoresB: {scoresB}")
print(f"Median: {median_of_two_arrays(scoresA, scoresB)}")

# Test case 2
scoresA = [1, 2]
scoresB = [3, 4]
print(f"\nTest 2 - scoresA: {scoresA}, scoresB: {scoresB}")
print(f"Median: {median_of_two_arrays(scoresA, scoresB)}")

# Test case 3
scoresA = [1, 3]
scoresB = [2]
print(f"\nTest 3 - scoresA: {scoresA}, scoresB: {scoresB}")
print(f"Median: {median_of_two_arrays(scoresA, scoresB)}")