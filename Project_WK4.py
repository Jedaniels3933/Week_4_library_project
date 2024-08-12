class Book():                         #Establish Book Class
    def __init__(self, title, author,  genre,  pub_date, status = "Available"): 
        self.title = title
        self.author = author
        self.genre = genre
        self.pub_date = pub_date
        self.status = status



class User():
    def __init__(self, name, email, phone, address, check_outs):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.check_outs = check_outs

class Author():
    def __init__(self, name, age, hometown):
        self.name = name
        self.age = age
        self.hometown = hometown

def main():
    print("Welcome to the Library! Main menu,please select and option")
    print("1. Book Operations ")
    print("2. User Operations")
    print("3. Author Operations")
    print("4. Quit")
    choice = input("Please enter a number: ")
    if choice == "1":   
        book_operations()    
    elif choice == "2":
        user_operations()      
    elif choice == "3":
        author_operations() 
    elif choice == "4":
        quit() 
                  
    else:
        print("Invalid selection, please try again")

def book_operations():
    print("Welcome to the Book Operations Menu")
    print("1. Add a book")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Search for a book")
    print("5. Display all books")
    choice = input("Please enter a number: ")
    if choice == "1":
        add_book()
        
    elif choice == "2":
        borrow_book()
    elif choice == "3":
        return_book()
    elif choice == "4":
        search_book()
    elif choice == "5":
        display_books()    #Need Help
        pass
    else:
        print("Invalid selection, please try again")
    
def user_operations():
    print("Welcome to the User Operations Manu")
    print("1. Add a user")
    print("2. View User details")
    print("3. Display all users")
    choice = input("Please enter a number: ")
    if choice == "1":
        add_user()
        
    elif choice == "2":
        view_user()
        
    elif choice == "3":
        display_users()
        
    else:
        print("Invalid selection, please try again")
def author_operations():
    print("Welcome to the Author Operations Menu")
    print("1. Add a new author")
    print("2. View author details")
    print("3. Display all authors")
    choice = input("Please enter a number: ")
    if choice == "1":
            #add_author()
        pass
    elif choice == "2":
            #view_author()
        pass
    elif choice == "3":
            #display_authors()
        pass
    else:
        print("Invalid selection, please try again")
def quit():
    print("Thank you for using the Library, Goodbye")
    exit()  

def add_book():
    title = input("Please enter the title of the book: ")
    author = input("Please enter the author of the book: ")
    genre = input("Please enter the genre of the book: ")
    pub_date = input("Please enter the publication date of the book: ")
    status = "Available"
    new_book = Book(title, author, genre, pub_date, status)
    print("Book added successfully!")

def borrow_book():
    title = input("Please enter the title of the book you want to borrow: ")
    author = input("Please enter the author of the book you want to borrow: ")
    genre = input("Please enter the genre of the book you want to borrow: ")
    pub_date = input("Please enter the publication date of the book you want to borrow: ")
    status = "Checked Out"
    new_book = Book(title, author, genre, pub_date, status)
    print("Book borrowed successfully!")
def return_book():
    title = input("Please enter the title of the book you want to return: ")
    author = input("Please enter the author of the book you want to return: ")
    genre = input("Please enter the genre of the book you want to return: ")
    pub_date = input("Please enter the publication date of the book you want to return: ")
    status = "Available"
    new_book = Book(title, author, genre, pub_date, status)
    print("Book returned successfully!")
def search_book():
    title = input("Please enter the title of the book you want to search for: ")
    author = input("Please enter the author of the book you want to search for: ")
    genre = input("Please enter the genre of the book you want to search for: ")
    pub_date = input("Please enter the publication date of the book you want to search for: ")
    status = "Available"
    new_book = Book(title, author, genre, pub_date, status)
    print("Book found!")
    if title == new_book.title:
        print("Title: ", new_book.title)
        print("Author: ", new_book.author)
        print("Genre: ", new_book.genre)
        print("Publication Date: ", new_book.pub_date)
        print("Status: ", new_book.status)
    else:
        print("Book not found")
 
#def display_books(self):   Cant get this to work at all


def add_user():
    name = input("Please enter the name of the user: ")
    email = input("Please enter the email of the user: ")
    phone = input("Please enter the phone number of the user: ")
    address = input("Please enter the address of the user: ")
    check_outs = 0
    new_user = User(name, email, phone, address, check_outs)
    print("User added successfully!")

def view_user(self):  
    print(f" User: {self.name} {self.email} {self.phone} {self.address} {self.check_outs}")
    

    
    
#def get_user_list():
    #user_list = []
    #user_list.append(new_user)
    #return user_list
#def display_users():
    #print(user_list)

#def set_username(self, name):
    #self.name = name    
    #return
#def get_username(self):
    #return self.name
#def set_email(self, email):
    #self.email
    #return
#def get_email(self):
    #return self.email

#def user_list(self):
        #print(self.name)


  


    
        



    
   
   

    

    
    




   



  

       

   

    
    


    




if __name__ == "__main__":

        
    main()  

   
