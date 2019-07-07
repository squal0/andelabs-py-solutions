class NotesApplication(object):
    
    
    def __init__(self, author):
        self.author = author
        self.notes = []

    def create(self, note_content):
        self.notes.append(note_content)

    def lists(self):
        list_var = 0
        for var in self.notes:
            print "Note ID: " + str(list_var)
            print self.notes[list_var]
            list_var += 1
        print "By Author " + self.author
        
