def prime(num):
    prime_nums = []

    for n in range(num + 1):
        if (isPrime(n) is True):
            prime_nums.append(n)

    return prime_nums

def isPrime(n):
    n = abs(n)
    
    if(n < 2):
        return False
    elif (n == 2):
        return True

    for x in range(2, n):
        if(n % x == 0):
            return False

    return True
