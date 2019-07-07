def reverse_string(string):
  r_string = string[::-1]
  if string == '':
    return None
  elif r_string == string:
    return True
  else:
    return r_string
