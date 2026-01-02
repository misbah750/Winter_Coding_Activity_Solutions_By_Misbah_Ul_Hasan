def toh(num, first, middle, last):
    assert num > 0
    
    # just one disk left move it directly
    if num == 1:
        print("Move disk from", first, "to", last)
        return
    
    # Move n-1 disks from first to middle 
    toh(num-1, first, last, middle)
    
    # Move the largest disk from first to last
    toh(1, first, middle, last)
    
    # Move n-1 disks from middle to last 
    toh(num-1, middle, first, last)

# Test case 1
print("Test 1 - Moving 3 disks:")
toh(3, "A", "B", "C")

# Test case 2
print("\nTest 2 - Moving 2 disks:")
toh(2, "A", "B", "C")

# Test case 3
print("\nTest 3 - Moving 4 disks:")
toh(4, "A", "B", "C")