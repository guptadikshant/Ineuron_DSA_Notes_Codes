"""
Given a positive integer num, write a program that returns True if num is a perfect
square else return False. Do not use built-in functions like sqrt. Also, talk about the time
complexity of your code.
"""

def isPerfectSquare(num):

    left = 0
    right = num 
    

    while left <= right:

        mid = (left + right) // 2

        if mid * mid == num:
            return True
            break

        elif mid * mid < num:
            left = mid + 1
        
        else:                
            right = mid - 1

    return False


if __name__ == "__main__":

    num = int(input("Enter the number : "))
    print(f"The {num} is perfect square : {isPerfectSquare(num)}")