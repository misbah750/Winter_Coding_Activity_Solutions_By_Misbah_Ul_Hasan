def remove_invalid_parentheses(expr):
    result = set()
    
    # Figure out how many parens we need to remove
    left_remove = right_remove = 0
    for ch in expr:
        if ch == '(':
            left_remove += 1
        elif ch == ')':
            if left_remove > 0:
                left_remove -= 1
            else:
                right_remove += 1
    
    # Try all possible valid combinations using backtracking
    def dfs(index, path, open_count, l_rem, r_rem):
        # We have gone through the whole string
        if index == len(expr):
            if open_count == 0 and l_rem == 0 and r_rem == 0:
                result.add(path)
            return
        
        ch = expr[index]
        
        # Skip this '(' if we still need to remove some
        if ch == '(' and l_rem > 0:
            dfs(index + 1, path, open_count, l_rem - 1, r_rem)
        
        # Skip this ')' if we still need to remove some
        if ch == ')' and r_rem > 0:
            dfs(index + 1, path, open_count, l_rem, r_rem - 1)
        
        # Keep the current character
        if ch not in '()':
            dfs(index + 1, path + ch, open_count, l_rem, r_rem)
        elif ch == '(':
            dfs(index + 1, path + ch, open_count + 1, l_rem, r_rem)
        elif ch == ')' and open_count > 0:
            dfs(index + 1, path + ch, open_count - 1, l_rem, r_rem)
    
    dfs(0, "", 0, left_remove, right_remove)
    return list(result)

# Test case 1
expr = "(a)())()"
print(f"Test 1 - Expression: {expr}")
print(f"Result: {remove_invalid_parentheses(expr)}")

# Test case 2
expr = "()())()"
print(f"\nTest 2 - Expression: {expr}")
print(f"Result: {remove_invalid_parentheses(expr)}")

# Test case 3
expr = "((()"
print(f"\nTest 3 - Expression: {expr}")
print(f"Result: {remove_invalid_parentheses(expr)}")

