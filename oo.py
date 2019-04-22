"""
1. Discussion
-------------

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   encapsulation: 
    The internal representation of an object is generally hidden from view outside of the object's definition
    A class is an example of encapsulation as it encapsulates all the data that is member functions,variables
  
   inheritance:

  
   polymorphism:

2. What is a class?
    A class is an object constructor for creating objects. It is like a blueprint for creating objects.

3.What is a method?
 A Method is a function in a class. It is used for an object for which it is called. The method is accessible to data that is contained within the class

4. What is an instance in object orientation?
    An instance is is a specific realization of any object. An instance is made using a class which is a blueprint

5. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

   class attributes are shared among all instances that were created using the class.
   an instance attribute can be specific to the instance and not share with other instances

"""


# 2. Road Class
# #############################################################################

# Create your Road class here
class Road:
    num_lanes = 2
    speed_limit = 25

road_1 =  Road()
road_2 =  Road()

print(road_1.num_lanes)
print(road_2)

road_1.num_lanes = 4
road_1.speed_limit = 60

print(road_1.num_lanes)
print(road_1.speed_limit)



# Instantiate Road objects here


# 3. Update Password
# #############################################################################
class User(object):
    """A user object."""

    def __init__(self, username, password):
        self.username = username
        self.password = password

    # write the update_password method here

    def update_password(self,new_password,current_password):
        if self.password != current_password:
          print(" You entered an invalid password")
        else:
            self.password = new_password



# 4. Build a Library
# #############################################################################
class Book(object):
    """A Book object."""

    def __init__(self, title, author):
        self.title = title
        self.author = author

# Create your Library class here

class Library(object):
    def __init__(self):
        self.books = []

    def add_book(self,title,author):
        self.books.append(Book(title, author))
    
    def find_books_by_author(self, author):
        author_books = []
        for book in self.books:
            if book.author == author:
                author_books.append(book)
        return author_books

lib = Library()
lib.add_book('GOT', 'Usman')
lib.add_book('Node js', 'Usman')

print(lib.find_books_by_author('Usman'))

