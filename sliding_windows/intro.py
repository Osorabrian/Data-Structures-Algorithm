"""
sliding windows 
- This is an algorithm used for strings or arrays
- used to analyze a subset of data using a fixed window or dynamic window
- there are two a fixed window and variable window
"""

#max_sum

def max_sum(arr):
    if len(arr) < 5:
        return "List has a length of less than 5."
    
    left = 0
    right = left+5
    max_sum = 0
    
    while right <= len(arr):
        cur_sum = sum(arr[left:right])
        max_sum = max(max_sum, cur_sum)
        left+=1
        right+=1
        
    return max_sum

print(max_sum([5, 7, 1, 4, 3, 6, 2, 9, 2]))