def fibonnaci(x):
    """Returns a list of numbers from the fibonnaci series, from a given range x"""
    fibonnaci_list = [0,1]
    
    for i in range(0, x):
        fibonnaci_list.append(fibonnaci_list[-1] + fibonnaci_list[-2])
        
    return fibonnaci_list


