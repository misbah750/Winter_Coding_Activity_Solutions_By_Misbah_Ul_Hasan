from collections import Counter

def password_recovery_window(log: str, pattern: str) -> str:
    if not pattern or not log:
        return ""
    
    # Figure out what characters we need and how many
    pattern_count = Counter(pattern)
    
    
    window_count = Counter()
    
    formed, required = 0, len(pattern_count)
    result_range = [-1, -1]
    min_window_len = float("inf")
    left_ptr = 0
    
    for right_ptr in range(len(log)):
        char = log[right_ptr]
        window_count[char] += 1
        
        # Did we just meet the requirement for this character?
        if char in pattern_count and window_count[char] == pattern_count[char]:
            formed += 1
        
        # Try to make the window smaller while it still works
        while formed == required:
            if (right_ptr - left_ptr + 1) < min_window_len:
                result_range = [left_ptr, right_ptr]
                min_window_len = right_ptr - left_ptr + 1
            
            left_char = log[left_ptr]
            window_count[left_char] -= 1
            
            if left_char in pattern_count and window_count[left_char] < pattern_count[left_char]:
                formed -= 1
            
            left_ptr += 1
    
    l, r = result_range
    return log[l:r+1] if min_window_len != float("inf") else ""

# Test case 1
log = "ADOBECODEBANC"
pattern = "ABC"
print(f"Log: {log}, Pattern: {pattern}")
print(f"Result: {password_recovery_window(log, pattern)}")

# Test case 2
log = "XYZBACXYZABC"
pattern = "ABC"
print(f"\nLog: {log}, Pattern: {pattern}")
print(f"Result: {password_recovery_window(log, pattern)}")

# Test case 3
log = "HELLO"
pattern = "LO"
print(f"\nLog: {log}, Pattern: {pattern}")
print(f"Result: {password_recovery_window(log, pattern)}")