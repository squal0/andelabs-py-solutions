class PrimeChecker(object):
    def __init__(self, number = None):
        number = int(number) if number else None
        self.number = number

    def is_prime(self): 
        if self.number < 2:
            return False
        elif self.number == 2:
            return True
        for num in range (2, self.number):
            if self.number % num == 0:
                return False
        return True
