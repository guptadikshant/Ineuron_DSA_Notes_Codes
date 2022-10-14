"""
Given an integer array nums and an integer k, return the kth largest element present in
an array.
For example:
arr = [40, 25, 68, 79, 52, 66, 89, 97]
k = 2
result = 89
"""

"""
Approach of the problem:
  1) We can use max heap in this case. First sort the array in descending order
  2) Then we can create Max heap from it.
  3) Then we can use for loop for K number of times and pop out the element. 
        The reason to use loop k number of times is so that we can pop out Kth element from max heap
"""

"""
Total time complexity is : O(k+N+N log(N))
"""
from typing import List
import heapq


def kLargestElement(arr: List[int], k) -> int:
    result = 0
    heap = [-n for n in arr] # time complexity is O(N)
    heapq.heapify(heap) # time complexity is O(N log N)

    for i in range(k): # time complexity is O(k)
        result = heapq.heappop(heap)

    return -result


if __name__ == "__main__":
    arr = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    result = kLargestElement(arr, k)
    print(f"Kth largest element : {result}")
