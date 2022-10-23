def pow(x, n):

    if n < 0:
        n = -n
        x = 1 / x

    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        mid = n // 2
        temp = pow(x, mid)

    result = temp * temp

    if n % 2 == 0:
        return result
    else:
        return result * x


if __name__ == '__main__':
    x = 2
    n = -2
    result = pow(x, n)
    print(f"Power of {x} raise to {n} is : {result}")