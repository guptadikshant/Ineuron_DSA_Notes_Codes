def FindPowerOfElement(num,power):
    
    if power == 0:
        return 1
    elif power == 1:
        return num

    else:
        mid = power // 2
        temp = FindPowerOfElement(num,mid)

    result = temp * temp 

    if power % 2 == 0:
        return result
    else:
        return result  * num


if __name__ == "__main__":
    num = 2
    power = 17

    result = FindPowerOfElement(num, power)

    print(f"The result is : {result}")



# Second Approach
def pow(a,b):

    if b == 0:
        return 1

    if b % 2 ==0:
        return pow(a, b//2) * pow(a, b//2)

    else:
        return a * pow(a, b//2) * pow(a, b//2)



def myPow(a , b):

    x = pow(a,b)

    if b < 0:
        print(1/x)
    else:
        print(x)

myPow(2,-2)