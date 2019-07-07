def find_missing(ary1 = [], ary2 = []):

    if((len(ary1) and len(ary2)) == 0):
        return 0
    if(set(ary1) == set(ary2)):
        return 0
    for num1 in ary1:
        for num2 in ary2:
            if(num2 not in ary1):
                return num2
