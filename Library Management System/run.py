from database_handler import *
import os


# Function to add a new book
def add_new_book():
    name = input("\nEnter book name: ")
    author = input("Enter author name: ")
    genre = input("Enter book genre: ")
    name = name.lower()
    author = author.lower()
    genre = genre.lower()
    add_record(name, author, genre)
    print("\n\tBook added successfully.")
    input("\n\n\tPress any key to continue...")


# Function to delete a book
def delete_book():
    name = input("\nEnter book name to delete: ")
    name = name.lower()
    book = show_one(name, 1)
    if book:
        delete_record(name)
        print("\n\tBook deleted successfully.")
    else:
        print("\n\tBook not found.")
    input("\n\n\tPress any key to continue...")


# Function to show all books
def show_books():
    books = show_all()
    if books:
        for book in books:
            print(f"\n•\tName: {book[0].capitalize()}, Author: {book[1].capitalize()}, Genre: {book[2].capitalize()}")
    else:
        print("\n\tNo books found.")
    input("\n\n\tPress any key to continue...")


# Function to show a specific book
def show_book():
    print("\nEnter mode of book:\n1.To find according to book name\n2.To find by author\n3.To find by genre\n")
    mode = int(input("Choice: "))
    if mode == 1:
        word = input("\nEnter book name to show: ")
    elif mode == 2:
        word = input("\nEnter author name to show: ")
    elif mode == 3:
        word = input("\nEnter book genre to show: ")
    else:
        print("\n\twrong input!")
        return
    word = word.lower()

    book = show_one(word, mode)
    if book:
        for x in book:
            print(
                f"\n•\tName: {book[book.index(x)][0].capitalize()}, Author: {book[book.index(x)][1].capitalize()}, Genre: {book[book.index(x)][2].capitalize()}\n")
    else:
        print("\n\tBook not found.")
    input("\n\n\tPress any key to continue...")


# Main program loop
while True:
    os.system('cls')
    print("\nChoose an option:")
    print("1. Add new book")
    print("2. Delete book")
    print("3. Show all books")
    print("4. Show a specific book")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_new_book()
    elif choice == 2:
        delete_book()
    elif choice == 3:
        show_books()
    elif choice == 4:
        show_book()
    elif choice == 5:
        exit()
    else:
        print("Invalid choice. Please try again.")
