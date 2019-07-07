def caffeineBuzz(num):
    script = "Script"
    java = "Java"
    coffee = "Coffee"
    miss = "mocha_missing"

    if(isEven(num) and((num % 3 == 0)) and(num % 4 == 0)):
        return coffee + script
    elif((num % 3 == 0) and (num % 4 == 0)):
        return coffee
    elif(isEven(num) and (num % 3 == 0)):
        return java + script
    elif(num % 3 == 0):
        return java
    else:
        return miss

def isEven(n):
    if(n % 2 == 0):
        return True
    return False

    
