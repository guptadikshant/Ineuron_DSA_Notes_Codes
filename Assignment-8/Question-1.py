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

"""
Approach of the solution : 
    1) First sort the array in ascending order
    2) Running loop K times so that we can pop out the elements that many number of times
        and will give the kth smallest element
"""

"""
Total time complexity of this solution is O(k+N log N)
"""


from typing import List
import heapq


def kSmallestElement(arr: List[int], k) -> int:

    min_heap = sorted(arr) # time complexity O(N logN)
    result :int = 0

    for i in range(k): # time complexity O(k)
        result = heapq.heappop(min_heap)

    return result

if __name__ == "__main__":
    arr = [40, 25, 68, 79, 52, 66, 89, 97]
    k = 2
    result = kSmallestElement(arr, k)
    print(f"Kth smallest element is : {result}")
