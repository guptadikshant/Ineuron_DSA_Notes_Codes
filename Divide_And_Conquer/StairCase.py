def countWays(stairs):

    if stairs == 1:
        return 1

    elif stairs == 2:
        return 2

    else:
        return countWays(stairs - 1) + countWays(stairs - 2)


if __name__ == '__main__':

    stairs = 10

    print(f"Number of ways are : {countWays(stairs)}")