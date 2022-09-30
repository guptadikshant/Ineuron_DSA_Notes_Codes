"""
Question-1
Compute and return the square root of x, where x is guaranteed to be a non-negative
integer. And since the return type is an integer, the decimal digits are truncated and only
the integer part of the result is returned. Also, talk about the time complexity of your
code.
"""
def calculateSqRoot(num):

    left=0
    right=num
    result=0

    while left <= right:

        mid=(left+right) // 2

        if mid * mid == num:
            result = mid
            break

        elif mid * mid < num:
            left = mid + 1
            result = mid
        else:
            right = mid - 1


    return result


if __name__ == '__main__':
    num = int(input("Enter the number : "))
    print(f"the square root of {num} is : {calculateSqRoot(num)}")
        
