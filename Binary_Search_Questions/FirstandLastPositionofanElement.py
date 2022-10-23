from typing import List


def firstandLastOccurence(arr:List[int], target:int):
    result = [None, None]

    def firstOccu(arr, target):

        start = 0
        end = len(arr) - 1

        ans1 = 0

        while start <= end:

            mid = start + (end - start) // 2

            if arr[mid] == target:
                ans1 = mid
                end = mid - 1

            elif arr[mid] < target:
                start = mid + 1

            else:
                end = mid - 1

        return ans1

    def lastOccu(arr, target):

        start = 0
        end = len(arr) - 1

        ans2 = 0

        while start <= end:

            mid = start + (end - start) // 2

            if arr[mid] == target:
                ans2 = mid
                start = mid + 1

            elif arr[mid] < target:
                start = mid + 1

            else:
                end = mid - 1

        return ans2

    result[0], result[1] = firstOccu(arr, target), lastOccu(arr, target)

    return result


if __name__ == "__main__":
    arr = [1, 2, 3, 3, 3, 3, 3, 3, 4, 5]
    target = 3
    ans = firstandLastOccurence(arr, target)
    print(f"First occurence is {ans[0]} and last occurence is {ans[1]}")
