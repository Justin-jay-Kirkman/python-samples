# recursive
# Time complexity: N/2^x = 1 -> N = 2^x -> x = log2N
# Space complexity: N/2^x = 1 -> N = 2^x -> x = log2N

def recusriveBinaryTree(target, sorted_array, left, right):
    if right < left:
        return -1
    middle = (left + right) // 2
    if sorted_array[middle] == target:
        return middle
    if target < sorted_array[middle]:
        return recusriveBinaryTree(target, sorted_array, left, middle - 1)
    elif target > sorted_array[middle]:
        return recusriveBinaryTree(target, sorted_array, left + 1, right)


# Interactive
# Time complexity: N/2^x = 1 -> N = 2^x -> x = log2N
# Space complexity: O(1)
def iterativeBinaryTree(target, sorted_array):
    left = 0
    right = len(sorted_array) - 1
    while left <= right:
        middle = (left + right) // 2 # floor division
        if sorted_array[middle] == target:
            return target
        if target < sorted_array[middle]: # looking left
            # left same
            right = middle - 1
        elif target > sorted_array[middle]:
            left = middle + 1
            # right same
    return -1


