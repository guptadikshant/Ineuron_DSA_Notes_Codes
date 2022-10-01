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