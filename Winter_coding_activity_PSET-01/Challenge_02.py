def find_smallest_bag(log, pattern):
    # Edge case: if empty, return empty
    if not log or not pattern:
        return ""
    
    # STEP 1: Count what we NEED
    need = {}
    for char in pattern:
        need[char] = need.get(char, 0) + 1
    
    # STEP 2: Setup our variables
    left = 0           # Left hand position
    smallest = ""      # Best answer so far
    have = {}          # What we currently have
    complete = 0       # How many chars are complete
    
    # STEP 3: Move RIGHT hand through the string
    for right in range(len(log)):
        # Pick up the character
        char = log[right]
        have[char] = have.get(char, 0) + 1
        
        # Did we complete this character?
        if char in need and have[char] == need[char]:
            complete += 1
        
        # STEP 4: If we have everything, try to SHRINK
        while complete == len(need):
            # Save if this is better
            window = log[left:right+1]
            if smallest == "" or len(window) < len(smallest):
                smallest = window
            
            # Remove from left
            left_char = log[left]
            have[left_char] -= 1
            
            # Did we break a requirement?
            if left_char in need and have[left_char] < need[left_char]:
                complete -= 1
            
            left += 1
    
    return smallest

# Test it!
log = "ADOBECODEBANC"
pattern = "ABC"
print(find_smallest_bag(log, pattern))  