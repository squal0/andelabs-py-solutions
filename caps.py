class Caps(object):

    def __init__(self, string):
        self.string = str(string)

    def isCapped(self):
        if(self.string == self.string.upper()):
            return "UPPERCASED"
        elif(self.string == self.string.lower()):
            return "LOWERCASED"
        else:
            return "SOME"

    def upper(self):
        new_string = ''

        for index in range(len(self.string)):
            if(str(self.string[index]) == str(self.string[index]).upper()):
                new_string += str(self.string[index])

        return len(new_string)

    def lower(self):
        new_string = ''

        for index in range(len(self.string)):
            if(str(self.string[index]) == str(self.string[index]).lower()):
                new_string += str(self.string[index])

        return len(new_string)

