# https://dxnpxrk.medium.com/the-most-important-sorting-algorithms-to-know-for-coding-interviews-merge-sort-and-quick-sort-c33555496edf

"""
merge sort
"""

def merge_sort(nums):
    # Base case: A single (or zero) element array is already sorted
    if len(nums) <= 1:
        return nums

    # Split the array into two halves (Divide)
    middle = len(nums) // 2
    left_half = nums[:middle]
    right_half = nums[middle:]

    # Recursively sort both halves (Conquer)
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_sorted, right_sorted)


def merge(left, right):
    result = []
    left_pointer, right_pointer = 0, 0

    # Traverse through both left and right arrays
    while left_pointer < len(left) and right_pointer < len(right):
        # If the left value is lower, add it to the result
        if left[left_pointer] < right[right_pointer]:
            result.append(left[left_pointer])
            left_pointer += 1
        # Otherwise, add the right value
        else:
            result.append(right[right_pointer])
            right_pointer += 1

    # Append any leftover items from left or right if they exist
    # One will always be empty
    result.extend(left[left_pointer:])
    result.extend(right[right_pointer:])

    return result
nums = [5, 4, 3, 2, 1, 45, 45,23,1]
result = merge_sort(nums)
print(result)