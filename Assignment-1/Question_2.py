"""
Question-2
You are a product manager and currently leading a team to develop a new product.
Unfortunately, the latest version of your product fails the quality check. Since each
version is developed based on the previous version, all the versions after a bad version
are also bad. Suppose you have n version and you want to find out the first bad one,
which causes all the following ones to be bad. Also, talk about the time complexity of
your code.
"""


def firstBadOne(arr):

    left = 0
    right = len(arr) -1
    result= 0

    while left <= right:

        mid = (left + right) // 2

        if  arr[mid] == 1:
            result = mid
            break

        elif arr[mid] == 0:
            left = mid + 1

        else:
            right = mid - 1

    return result


if __name__ == "__main__":
    arr = [0,0,0,1,1,1,1,1,1]
    ans = firstBadOne(arr)
    print(f"The first bad version is present at index : {ans}")
        