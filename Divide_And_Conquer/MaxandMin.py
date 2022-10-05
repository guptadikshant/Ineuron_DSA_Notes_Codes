def findMaxandMin(arr, i, j):

    if i == j:
        maxval,minval = arr[i], arr[i]

    elif i == j-1:

        if arr[i] < arr[j]:
            maxval,minval = arr[j], arr[i]
        else:
            maxval,minval = arr[i], arr[j]

    else:

        mid = i + (j-i) // 2

        max_1,min_1 = findMaxandMin(arr, i, mid)
        max_2,min_2 = findMaxandMin(arr,mid+1,j)


        if max_1 < max_2:
            maxval = max_2

        else:
            maxval = max_1

        if min_1 < min_2:
            minval = min_1
        else:
            minval = min_2

    return maxval, minval



if __name__ == '__main__':

    arr = [20,39,45,65,21,44,89,92]

    i =0 
    j = len(arr) -1

    MaxVal, MinVal = findMaxandMin(arr, i, j)

    print(f"The maximum value is : {MaxVal} and minimum value is : {MinVal}")