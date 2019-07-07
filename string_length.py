def string_length(string):
  length = []
  counter = 0
  
  if type(string) is str:
    length.append(len(string))
    return length

  if type(string) is list:
    for index in range(len(string)):
      length.append(len(string[index]))
      index += counter
                    
  return length
