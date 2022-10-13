"""
Given array nums with n objects colored red, white, or blue, sort them in place so that
the objects of the same color are adjacent, with the colors in the order red, white, and
blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue
respectively.
Solve this question without using the library sort function.
For example:
Nums = [2,0,2,1,1,0]
Result = [0,0,1,1,2,2]
"""

"""
Approach of the solution : We can use Quick Sort for this problem as it has O(N log(N)) time complexity
"""

from typing import List

def sortColors(nums: List[int]) -> List[int]:
    p = 0
    q = len(nums) - 1
    def partition(nums, p, q):

        pivot = nums[p]
        i = p

        for j in range(i + 1, q+1):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i], nums[p] = nums[p], nums[i]

        return i

    def quickSort(nums, p, q):

        if p < q:
            mid = partition(nums, p, q)
            quickSort(nums, p, mid-1)
            quickSort(nums, mid+1, q)

        return nums

    sorted_nums = quickSort(nums,p,q)

    return sorted_nums


if __name__ == "__main__":
    nums = [2, 0, 2, 1, 1, 0]

    print(sortColors(nums))
