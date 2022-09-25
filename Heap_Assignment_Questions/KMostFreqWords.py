from collections import Counter
from heapq import heapify, heappop

def kMostFreq(arr,k):
    
    result = []
    frqCount = Counter(arr)
    frqCount = [(-v, k) for k,v in frqCount.items()]  

    print(frqCount)  

    heapify(frqCount)

    print(frqCount)
    
    for _ in range(k):
        result.append(heappop(frqCount)[1])

    return sorted(result)
    

if __name__ == '__main__':
    arr = ["priya", "bhatia", "akshay", "arpit", "priya", "arpit"]
    k = 3
    print(kMostFreq(arr, k))