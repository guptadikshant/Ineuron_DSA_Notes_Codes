def insertionSort(arr):
    # Iterating to whole array 
    for i in range(len(arr)):
        # Storing the current element in the array
        key = arr[i]
        # Decrement the value of i and store in j
        j = i -1

        # Now checking if j is greater than or equal to 0 and 
        # value of key is less than the previous element of array

        while j>=0 and key < arr[j]:

            # If that is true than the shift the previous element to one place to right
            arr[j + 1] = arr[j] 

            # And decrement the value of j
            j -= 1
        
        # After the while loop is completed we placed the value of key at it its correct place
        # which is after shifting all the elements to right which are greater than key 
        arr[j+1] = key

    return arr


if __name__ == '__main__':
    print(insertionSort([43,32,62,19,56]))