from typing import List

# Time complexity: O(log n)
def binary_search(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2 # floor division
        if nums[mid] == target:
            return mid 
        elif target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1

if __name__ == '__main__':
    assert binary_search([1,2,3,4,5], 3) == 2
    assert binary_search([1,2,3], 4) == -1
