def arith_geo(numArray):
    
    if ( len(numArray) == 0):
        return 0
    
    diff = numArray[1] - numArray[0]
    ratio = numArray[1] / numArray[0]

    aSeq = True
    gSeq = True
    index = 2

    while ( index < len(numArray) - 1):
        if not (numArray[ index + 1] - numArray[ index] == diff):
            aSeq = False

        index += 1
        
    for i in range(len(numArray) - 2):
        if numArray[i] * numArray[i + 2] != numArray[i + 1] ** 2:
            gSeq = False
    for i in range(len(numArray) - 1):
        if numArray[i] == 0 and numArray[i + 1] != 0:
            gSeq = False

    if aSeq == True:
        return "Arithmetic"

    elif gSeq == True:
        return "Geometric"

    else:
        return -1
