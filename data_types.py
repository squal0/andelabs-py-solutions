def data_type(args):
  if args is str(args):
    return len(args)
  if args == None:
    return "no value"
  if args == True or args == False:
    return args
  if type(args) is int:
    if args < 100:
      return "less than 100"
    elif args > 100:
      return "more than 100"
    else:
      return "equal to 100"
  
  if type(args) is list:
    try:
      if args[2] not in args:
        return None
      return args[2]
    except IndexError:
      pass
