from typing import List

"""
Video link : https://www.youtube.com/watch?v=zD2Jg3alZV8&list=PLDzeHZWIZsTryvtXdMr6rPh4IDexB5NIA&index=14
"""


def findPeakElement(nums: List[int]) -> int:
    start = 0
    end = len(nums) - 1

    while start < end:

        mid = start + (end - start) // 2

        if nums[mid] < nums[mid + 1]:  # if element is less than its next adjacent element
            start = mid + 1  # then we can increase start to reach at mid-element

        else:
            end = mid  # mid -1 is not here because it will lead to other side of mountain

    return start  # or return end both will return same result


if __name__ == "__main__":
    nums = [1, 2, 1, 3, 5, 6, 4]

    print(f"Peak element's index in an array is : {findPeakElement(nums)}")
