from typing import List
import heapq


def kLargestElement(arr: List[int], k) -> int:
    # # this is to make sure we can get rid of the duplicates
    # arr = list(set(arr))
    # # it gives the first k largest elements in the array
    # ans = heapq.nlargest(k, arr)
    # # as the indexes of array start from 0 there we are taking one less values of k
    # return ans[k - 1]
    res = 0
    heap = [-n for n in arr]
    heapq.heapify(heap)
    print(heap)
    for i in range(k):
        res = heapq.heappop(heap)
    print(res)
    return -res


if __name__ == "__main__":
    arr = [3,2,3,1,2,4,5,5,6]
    k = 4
    result = kLargestElement(arr, k)
    print(f"Kth largest element : {result}")