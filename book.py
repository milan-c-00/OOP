class Book:
    def __init__(self, name, copies):
        self.name = name
        self.copies = copies

    def increase_copies(self, how_much):
        self.copies += how_much

    def decrease_copies(self, how_much):
        self.copies -= how_much


the_art_of_computer_programming = Book('The Art Of Programming', 100)
learning_python = Book('Learning Python in 100 Steps', 100)
learning_restful_services = Book('Learning Restful Services', 100)

# the_art_of_computer_programming.name = 'The Art Of Programming'
# learning_python.name = 'Learning Python in 100 Steps'
# learning_restful_services.name = 'Learning Restful Services'

print(the_art_of_computer_programming.name)
print(learning_python.name)
print(learning_restful_services.name)

learning_python.increase_copies(25)

learning_python.decrease_copies(15)

print(learning_python.copies)