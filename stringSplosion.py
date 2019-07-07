class StringSplosion(object):
    def __init__(self, string):
        self.string = string

    def manipulate(self):
        word = ''
        for s in range(0, len(self.string) + 1):
            word += self.string[:s]
            
        return word
