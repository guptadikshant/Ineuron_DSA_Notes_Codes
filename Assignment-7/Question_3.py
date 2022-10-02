"""
Question-3
An e-commerce site tracks the purchases made each day. The product that is purchased
the most one day is the featured product for the following day. If there is a tie for the product
purchased most frequently, those product names are ordered alphabetically ascending and
the last name in the list is chosen.[Amazon]
['yellowShirt', 'redHat', 'blackShirt', 'bluePants', 'redHat','pinkHat', 'blackShirt', 'yellowShirt',
'greenPants', 'greenPants', 'greenPants']
'yellowShirt' - 2
'redHat' - 2
'blackShirt' - 2
'bluePants' - 1
'greenPants' - 3
'pinkHat' - 1
Output - greenPants
"""


from collections import Counter
from typing import List

def featureProduct(products:List[str]) -> str:
    """
    Time complexity of this solution is O(m+n)
    For first loop we iterate through all the values to find the maximum value
    For the second loop we iterate through keys and values to apppend all the elements for maximum value
    """

    max_prod_value = 0 # To compare and find out the value maximum value in the product counts
    result = [] # To store the results

    #Creates a dictionary with prodcut as key and its count as value
    freqCount = Counter(products) 

    # Sort the dictionary in descending order
    productCount = dict(sorted(freqCount.items(), key=lambda x:x[1], reverse=True))

    # This loop will find the maximum value in the product counts
    for product in productCount:
        if max_prod_value < productCount[product]:
            max_prod_value = productCount[product]

    # We will store key of the product count for which we found the maximum value
    for key,value in productCount.items():

        if max_prod_value == value:
            result.append(key)

    # As the result is in the descending order, we return the last index of the result array
    return result[-1]

    



if __name__ == '__main__':

    products = ['yellowShirt', 'redHat', 'blackShirt', 'bluePants', 'redHat','pinkHat', 'blackShirt', 'yellowShirt',
                'greenPants', 'greenPants', 'greenPants']


    print(f"Featured Product is : {featureProduct(products)}")


