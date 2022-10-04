"""
Question-1
Given an integer array nums of length n and an integer target, find three integers in nums
such that the sum is closest to the target.[Amazon]
You need to return the sum of three integers.
For example:arr = [-1, 2, 1, -4], target = 1
Output: 2
Explanation: [-1+2+1] = 2 (The sum that is closest to the target is 2)
"""
from typing import List

"""
The time complexity of this solution is O(n2). 
As there are 2 loops (one for loop and one while loop) which are 
going the whole array
"""

def threeSumClosest(arr:List[int],target:int) ->int:

    
    diff = float("inf")
    arr.sort() # Sort the array so that we can find the closest difference early at the starting of the array
    ans = 0
    for i in range(len(arr)):

        first = arr[i]  # intialize first element of array
        start = i+1     # Next adjacent element of the first element of array
        end = len(arr) - 1 # Last element of the array

        while start < end:
            currentSum = first + arr[start] + arr[end]
            # If the 3 elements of the current Sum is equal to target then we can find the directly return the target
            if currentSum == target:
                return target

            # We need to minimize the difference between the sum of 3 elements and target and when we find 
            # minimum difference then we can return the sum of those 3 elements for which the difference is minimum
            elif abs(currentSum - target) < diff:
                diff = abs(currentSum - target)
                ans = currentSum
            
            # If we overshoot the target that means the difference becomes larger
            # then we decrement the end index
            if currentSum > target:
                end -= 1
            # If we differecne becomes much smaller than target then we increment the start index
            else:
                start +=1

    return ans


    
if __name__ == '__main__':

    arr = [-1, 2, 1, -4]
    target = 1

    print(threeSumClosest(arr,target))



