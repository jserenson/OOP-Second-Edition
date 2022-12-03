#
# Now lets see come code.
# We start by defining the Note class as it seems simpilist
#The following example presents Note in its entirety.
# Docstrings within the example explain how it fits together
# 

import datetime

# 
# store the next available id for all new notes
last_id = 0

class Note:
    '''
    Represent a note in the notebook.
    Match against a string in searches.
    And store tags for each note.
    '''
    # 
    # Initialize the class
    # we meed to pass a memo and any optional tags
    def __init__(self, memo, tags=''):
        '''
        initialize a note with a memo and optional space 
        seperated tags.
        Automatically set the notes creation date and a unique
        id.
        '''
        self.memo = memo 
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id
        
    def __repr__(self):
        return f'id = {self.id}\nmemo = {self.memo}\ntags = {self.tags}'

        
    def match(self, filter):
        '''
        Determine if this note matches the filter text.
        Return True if it matches False otherwise.
        Search is case sensitive and matches both text 
        and tags.
        '''
        return filter in self.memo or filter in self.tags
        
        
    
'''
	Lets create our notebook next.
'''

class Notebook:
    '''
    Represent a collection of notes that can be taggged,
    modified, and searched.
    '''
    
    def __init__(self):
        '''
        Initialize a notebook with an empty list.
        '''
        self.notes = []
    
    def new_note(self, memo, tags=''):
        '''
        Create a new note and add it to the list
        '''
        self.notes.append(Note(memo, tags))
        
    def _find_note(self, note_id):
        '''
        Locate the note with the given id.
        '''
        print(f'find_note note_id = {note_id}')
        for note in self.notes:
            print(note)
            print(f'note_id = {note_id}')
            print(f'note.id = {note,id}')
            if str(note.id) == str(note_id):
                return note
        # 
        # Note not found 
        print("note not found")
        return None
               
    def modify_memo(self, note_id, memo):
        '''
        Find the note with the given ID and change its
        memo to the given value
        '''
        print("Entering modify_memo")
        note = self._find_note(note_id)
        print(f'note found = {note}')
        if (note != None):
            note.memo = memo
        
    def modify_tags(self, note_id, tags):
        '''
        Find the note with the given ID and change its
        tags to the given value
        '''
        print("Entering modify_tags")
        note = self._find_note(note_id)
        if (note != None):
            print(f'note found = {note}')
            note.tags = tags
            
    def search(self, filter):
        '''
        Find all notes that match the given filter string
        '''
        return [note for note in self.notes 
                if note.match(filter)]
    
'''
Now lets have a look at the menu interface.
The interface simply needs to present a menu and allow the user to input choices.
Heres our first try:_
'''

import sys
# 
# Because the code is here we dont need this
# from notebook import Notebook, Note

class Menu:
    '''
    Display a menu and respond to choices when run.
    choices is a dictionary of id's and function to execute
    when the user makes a choice, we retrieve the object from 
    the dictionary.
    The action variable actually refers to a specific method,
    and is called by appending empty brackets (since none of the
    methods require parameters) to the variable.
    '
    '''
    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
            "1": self.show_notes,
            "2": self.search_notes,
            "3": self.add_note,
            "4": self.modify_note,
            "5": self.quit
        }
        
    def display_menu(self):
        print(''' 
        Notebook Menu
        1. Show all Notes
        2. Search Notes
        3. Add Note
        4. Modify Note
        5. Quit
        ''')
        
    def run(self):
        last_id = 0
        '''
        Display the menu and respond to choices
        '''
        print("Entering Menu.run")
        while True:
            self.display_menu()
            choice =  input("Enter an option:")
            # 
            # set action to the method to call
            action = self.choices.get(choice)
            if action:
                # 
                # call the method
                action()
            else:
                print("{0} is not a valid choice".format(choice))
                
    def show_notes(self, notes=None):
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print("{0}:{1}\n{2}".format(note.id, note.tags, note.memo))

    def search_notes(self):
        filter = input("Search for: ")
        notes = self.notebook.search(filter)
        self.show_notes(notes)
        
    def add_note(self):
        memo = input("Enter a memo: ")
        self.notebook.new_note(memo)
        print("Your note has been added")
        
    def modify_note(self):
        id = input("Enter a note id: ")
        memo = input("Enter a memo: ")
        tags = input("Enter tabs: ")
        if memo:
            self.notebook.modify_memo(id, memo)
        if tags:
            self.notebook.modify_tags(id, tags)
            
    def quit(self):
        print("Thank you for using your notebook today.")
        sys.exit(0)
        
Menu().run()

if __name__ == '__main__':
    Menu().run
	