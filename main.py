import math


# Function to check if x is power of 4
def isPowerOfFour(n):
    if (n != 0 and n == pow(4, (math.log(n) / math.log(4)))):
        print(pow(4, (math.log(n) / math.log(4))))
        return True
    print(pow(4, (math.log(n) / math.log(4))))
    return False


def isPowerOfFour2(n):
    if (n == 0):
        return False
    while (n != 1):
        if (n % 4 != 0):
            return False
        n = n // 4

    return True


test_no = 8
if (isPowerOfFour2(test_no)):
    print(test_no, ' is a power of 4')
else:
    print(test_no, ' is not a power of 4')
