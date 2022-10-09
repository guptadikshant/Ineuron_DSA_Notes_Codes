def partition(arr, p, q):
    # Declaraing first element as pivot element
    pivot = arr[p]
    i = p

    for j in range(i+1, q+1):

        # The ith index will increment only when the element present at jth index is less than pivot element
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    # this swap will make sure the pivot element present exacatly at the middle position of array
    arr[i], arr[p] = arr[p], arr[i]

    return i



def quickSort(arr,p,q):

    if p < q:
        # Give the middle value index of the array
        mid = partition(arr, p, q)
        # Recursive call to the left of the array just upto one index short of mid
        quickSort(arr, p, mid-1)
        # Recursive call to the right of the array after one index increment of mid
        quickSort(arr, mid+1, q)

    return arr


if __name__ == "__main__":

    arr = [50,70,10,30,25,88]
    p = 0
    q = len(arr) - 1

    sortedArr = quickSort(arr, p ,q)

    print(f"sorted array is : {sortedArr}")