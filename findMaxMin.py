def find_max_min(num_list):
  largest = 0
  smallest = 0
  large_small = []

  for num in num_list:
      smallest = num
      for small in num_list:
          if(small < smallest):
              smallest = small
              
  for num in num_list:
      if(num > largest):
          largest = num
              
  if( largest == smallest):
    large_small.append(len(num_list))
    return large_small
    
  large_small.append(smallest)
  large_small.append(largest)
  
  return large_small


##def find_max_min(num_list):
##  largest = max(num_list)
##  smallest = min(num_list)
##  large_small = []
##              
##  if( largest == smallest):
##    large_small.append(len(num_list))
##    return large_small
##    
##  large_small.append(smallest)
##  large_small.append(largest)
##  
##  return large_small
  
