"""
Question-1
Kth smallest element [Amazon]
Given an array of n-elements and an integer k, find the kth smallest element present in
an array.
For example:
arr = [40, 25, 68, 79, 52, 66, 89, 97]
k = 2
result = 40
"""

from typing import List
import heapq


def kSmallestElement(arr: List[int], k) -> int:
    # this is to make sure we can get rid of the duplicates
    arr = list(set(arr))
    # it gives the first k smallest elements in the array
    ans = heapq.nsmallest(k, arr)
    # as the indexes of array start from 0 there we are taking one less values of k
    return ans[k - 1]


if __name__ == "__main__":
    arr = [40, 25, 68, 79, 52, 66, 89, 97, 26, 26, 27]
    k = 2
    result = kSmallestElement(arr, k)
    print(f"Kth smallest element is : {result}")
