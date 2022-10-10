from typing import List
import heapq


def kLargestElement(arr: List[int], k) -> int:
    result = 0
    heap = [-n for n in arr]
    heapq.heapify(heap)

    for i in range(k):
        result = heapq.heappop(heap)

    return -result


if __name__ == "__main__":
    arr = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    result = kLargestElement(arr, k)
    print(f"Kth largest element : {result}")
