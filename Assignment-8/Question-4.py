"""
Given array nums of size n, return the majority element present in the array.
Assume that the majority element always exists in an array.
For example:
Nums = [2, 2, 1, 1, 1, 2, ,2]
Output: 2
"""

"""
Approach of the solution:
    First count the number of times each value occurs in the
    Then sort the counter in descending order. 
    The find the maximum value of key,value pair for which element count is highest.
    
Total time complexity is : O(N log N)
"""

from collections import Counter
from typing import List


def majorityElement(arr:List[int])->int:

    majority = Counter(arr) # time complexity is O(N)

    majority = dict(sorted(majority.items(),key=lambda x :x[1],reverse=True)) # time complexity is O(N log N)

    majority_element = max(zip(majority.values(),majority.keys()))[1] # time complexity is O(c)

    return majority_element

if __name__ == "__main__":
    Nums = [2, 2, 1, 1, 1, 2, 2]
    result = majorityElement(Nums)
    print(f"Majority Element in array is : {result}")