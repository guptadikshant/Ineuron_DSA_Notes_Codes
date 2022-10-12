"""
The peak element is the element that is strictly greater than its neighbors. If an array
contains multiple peak elements, return the index of any of the peak elements.
For example: [1,2,3,1]
Output: 2
"""

"""
Approach of the solution:
    1) First we can find the middle element
    2) Then we can check if the middle element if greater than its left element and right element
        If this is true then it is our mid element 
    3) If mid element is greater than its right element then peak element exists in right side 
        as it is already smaller than its left element.
    4) If mid element is greater than its left element then peak element exists in left side 
        as it is already smaller than its right element.     
"""

"""
Time complexity of this solution is O(log n)
"""

from typing import List


def peakElement(nums: List[int]) -> int:
    left = 0
    right = len(nums) - 1

    while left < right:

        mid = left + (right - left) // 2

        if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
            return mid

        elif nums[mid] > nums[mid + 1]:
            right = mid - 1

        else:
            left = mid + 1

    if nums[left] > nums[right]:
        return left
    else:
        return right


if __name__ == "__main__":
    nums = [1, 2, 3, 1]

    result = peakElement(nums)

    print(f"Peak Element in the array is : {result}")
