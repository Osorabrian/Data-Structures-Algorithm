"""
    Binary search is an algorithm that efficiently finds a target element in a sorted list.
    It repeatedly divides the list in half and compares the target element with the middle element.
    If the the target is equal to the middle element it returns the middle element.
    If the target is less than the middle element, it searches in the left half of the list.
    If the target is greater than the middle element, it searches in right half of the list.
    Binary search algorithm returns the index of the target element if found, or -1 if the target is not found.
    The process continues until the target is found or the list is exhausted.
    The time complexity of binary search is O(log n), where n is the number of elements in the list.
    Binary search is an efficient algorithm for searching a sorted list, especially when the list is large.
    It is widely used in computer science and data structures.
"""
 
arr = [1,5,9,10,12,45,60,96,104, 120]
 
def binary_search(arr, target):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left+right)//2
        mid_element = arr[mid]
        if mid_element == target:
            return mid
        elif mid_element < target:
            left = mid+1
        else:
            right = mid-1
    return -1

print(binary_search(arr, 104))

def count_occurence(nums, target, search):
    # search space is nums[left…right]
    (left, right) = (0, len(nums) - 1)
 
    # initialize the result by -1
    result = -1
 
    # loop till the search space is exhausted
    while left <= right:
 
        # find the mid-value in the search space and compares it with the target
        mid = (left + right) // 2
 
        # if the target is found, update the result
        if target == nums[mid]:
            result = mid
 
            # go on searching towards the left (lower indices)
            if search:
                right = mid - 1
            # go on searching towards the right (higher indices)
            else:
                left = mid + 1
 
        # if the target is less than the middle element, discard the right half
        elif target < nums[mid]:
            right = mid - 1
        # if the target is more than the middle element, discard the left half
        else:
            left = mid + 1
 
    # return the found index or -1 if the element is not found
    return result

nums = [2, 5, 5, 5, 6, 6, 8, 9, 9, 9]
first = count_occurence(nums,5, True)
last = count_occurence(nums,5,False)
print(last-first+1)