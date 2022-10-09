## Implementation of Merge Sort
## function definition of merge Procedure
## n1+n2 = N 
## MergeProcedure time complexity = O(N)
def mergeProcedure(arr, i, mid, j):
    ## n1-> number of elements in the left subarray(i, mid)
    n1 = mid - i + 1
    ## n2 -> number of elements in the right subarray(mid+1, j)
    n2 = j - mid
    
    ## intialization of left and right subarray
    leftSubarray = [0] * n1
    rightSubarray = [0] * n2
    
    ## copy the elements from an array to the subarrays
    for m in range(n1):
        leftSubarray[m] = arr[i + m]
    
    for n in range(n2):
        rightSubarray[n] = arr[mid + 1 + n]
    
    p = 0
    q = 0
    k = i
    ## returning a sorted subarray
    while p < n1 and q < n2:
        if leftSubarray[p] <= rightSubarray[q]:
            arr[k] = leftSubarray[p]
            p += 1
        else:
            arr[k] = rightSubarray[q]
            q += 1
        k += 1
    
    ## copy the entire elements from the left subarray
    while p < n1:
        arr[k] = leftSubarray[p]
        p += 1
        k += 1
    
    ## copy the entire elements from the right subarray
    while q < n2:
        arr[k] = rightSubarray[q]
        q += 1
        k += 1

## function definition of merge sort
## Approach -> Divide and Conquer
## Recurrence Relation -> 2T(N/2) + N
## Time complexity -> O(NlogN)
def mergeSort(arr, i, j):
    if i < j:
        ## Divide
        mid = i + (j-i)//2
        ## Conquer
        ## recursive call -> left subtree
        mergeSort(arr, i, mid)
        ## recursive call -> right subtree
        mergeSort(arr, mid+1, j)
        ## Combine -> mergeProcedure(function calling)
        mergeProcedure(arr, i, mid, j)
    return arr


## Driver code
## arr = [0, 1, 2, 3, 4, 5, 6, 7]
arr = [50, 70, 65, 13, 80, 62, 98, 27]
## starting index
i = 0
## ending index
j = len(arr) - 1
## function calling
result = mergeSort(arr, i, j)
print(result)