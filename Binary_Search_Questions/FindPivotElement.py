def getPivot(arr):

    start = 0
    end = len(arr) - 1

    while start < end:

        mid = start + (end - start) // 2

        if arr[mid] >= arr[0]:
            start = mid + 1

        else:
            end = mid


    return start


if __name__ == '__main__':
    arr = [8, 10, 17, 1, 3]

    result = getPivot(arr)

    print(f"Pivot element's index is : {result}")