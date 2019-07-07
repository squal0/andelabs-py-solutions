def primes(n):
        """prints a given list of prime numbers based on a range given n"""
        primes_list = []
        for num in range(1, n):
                if is_prime(num) == True:
                        primes_list.append(num)
        return primes_list

def is_prime(x):
    """Function to determine whether a given number x is a prime number """
    x = abs(x) #ensures that x is an absolute number
    if x < 2:
        return False
    elif x == 2:
        return True
    for n in range (2, x):
        if x % n == 0:
            return False
    return True
