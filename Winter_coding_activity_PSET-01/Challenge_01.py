def product_except_self(contributions):
    # Takes O(n) time since we're just doing two passes
    
    # Uses O(n) space for the result, but only O(1) extra
    n = len(contributions)
    result = [0] * n
    
    leftProduct = 1
    for i in range(n):
        result[i] = leftProduct
        leftProduct = leftProduct * contributions[i]
    
    rightProduct = 1
    for i in range(n - 1, -1, -1):
        result[i] = result[i] * rightProduct
        rightProduct = rightProduct * contributions[i]
    
    return result

# Test case 1
contributions = [2, 3, 4, 5]
result = product_except_self(contributions)
print(f"Contributions: {contributions}")
print(f"Result: {result}")

# Test case 2
contributions = [1, 2, 3, 4]
result = product_except_self(contributions)
print(f"Contributions: {contributions}")
print(f"Result: {result}")

# Test case 3
contributions = [5, 10, 2, 8]
result = product_except_self(contributions)
print(f"Contributions: {contributions}")
print(f"Result: {result}")