# USING ITERATIVE APPROACH

def BinarySearch(arr,ele):
    left = 0
    right = len(arr) -1
    mid = 0

    while left<=right:
        mid = (left + right) // 2   # Iteratively updating the value of the mid
        
        if arr[mid] == ele:
            return mid
        elif arr[mid] < ele: # If the element present in the left direction of the mid
            left = mid + 1
        else:                # If the element present in the right direction of the mid
            right = mid - 1

    return -1

if __name__ == '__main__':
    print(BinarySearch(arr=[1,2,3,4,5,6,7,8,9,10],ele=11))


#USING RECURSIVE APPROACH
def BinarySearch(arr,left,right,ele):
    
    mid = 0

    while left<=right:
        mid = (left + right) // 2   # Iteratively updating the value of the mid
        
        if arr[mid] == ele:
            return mid
        elif arr[mid] < ele: # If the element present in the left direction of the mid
            return BinarySearch(arr,mid+1,right,ele) # Then update the left value to mid+1 in the recursive call
        else:                # If the element present in the right direction of the mid
            return BinarySearch(arr,left,mid-1,ele) # Then update the right value to mid+1 in the recursive call

    return -1

if __name__ == '__main__':
    arr =[1,2,3,4,5,6,7,8,9,10]
    left = 0
    right = len(arr) -1
    print(BinarySearch(arr,left,right,ele=7))
