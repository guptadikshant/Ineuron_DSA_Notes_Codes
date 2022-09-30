def heapify(arr,n,i):

    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] < arr[smallest]:
        smallest = left
    
    if right < n and arr[right] < arr[smallest]:
        smallest = right

    if smallest != i:
        arr[i],arr[smallest] = arr[smallest],arr[i]
        heapify(arr,n,smallest)


def buildHeap(arr,n):

    startIdx = n//2 - 1

    for i in range(startIdx,-1,-1):

       heapify(arr,n,i)


if __name__ == '__main__':

    arr = [1, 3, 7, 9, 12, 10, 8, 16, 18, 22, 27]
    # arr = [3,9,2,1,4,5]
    n = len(arr)

    buildHeap(arr,n)

    print(f"Array after building Min Heap is : {arr}")

