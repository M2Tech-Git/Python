from database_handler import *
import os

running = True


def accept_input(is_int: bool = False, limits=[]):
    verified = False
    while not verified:
        user_i = input()
        if not user_i:
            print("Please enter a value")
            continue

        if is_int:
            if user_i.isnumeric():
                if limits[0] <= int(user_i) <= limits[1]:
                    verified = True
                    return user_i
                else:
                    print("Please enter a value between", limits[0], "and", limits[1])
                    continue
            else:
                print("You can only enter integers")
                continue
        else:
            if user_i.isnumeric():
                print("Can't contain only numbers")
                continue
            verified = True
            return user_i.lower()


def clear():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')


clear()


def initiate():
    global running
    print("~", "Library Management System".center(100, "="), "~")
    print("\nEnter an appropriate choice (1-5)")
    print("\t1. Add a new book")
    print("\t2. Show all books")
    print("\t3. Remove a specific book")
    print("\t4. Retrieve a specific book")
    print("\t5. Exit")
    print("Choice: ", end="")
    user_input = accept_input(is_int=True, limits=[1, 5])

    if user_input == "1":
        add_new_book()
    elif user_input == "2":
        show_all_books()
    elif user_input == "3":
        remove_book()
    elif user_input == "4":
        retrieve_book()
    elif user_input == "5":
        running = False
        return


def add_new_book():
    clear()
    user_input = []
    print("Enter book name: ", end="")
    user_input.append(accept_input(False))
    print("Enter book author", end="")
    user_input.append(accept_input(False))
    print("Enter book genre", end="")
    user_input.append(accept_input(False))

    add_record(user_input[0], user_input[1], user_input[2])
    clear()
    print("Added the book: '{}', with author: '{}' and genre:  '{}'\n\n".format(user_input[0].capitalize(),
                                                                                user_input[1].capitalize(),
                                                                                user_input[2].capitalize()))


def show_all_books():
    clear()
    if show_all():
        for book in show_all():
            print("Name: '{}', Author: '{}', Genre: '{}'".format(book[0].capitalize(), book[1].capitalize(),
                                                                 book[2].capitalize()))
        input("\n\nPress Enter to continue")
        clear()
    else:
        print("There are no books")


def remove_book():
    clear()
    print("Enter the name of the book you want to Remove: ", end='')
    user_input = accept_input(False)
    if show_one(user_input, 1):
        delete_record(user_input)
        clear()
        print("Removed the book '{}'\n\n".format(user_input.capitalize()))
    else:
        print("'{}' does not exist\n\n".format(user_input.capitalize()))


def retrieve_book():
    clear()
    print("Choose an appropriate option (1-3)")
    print("\t1. Retrieve by name")
    print("\t2. Retrieve by author")
    print("\t3. Retrieve by genre")
    print("Choice: ", end="")

    mode = accept_input(is_int=True, limits=[1, 3])
    print("Enter '{}' of the book: ".format('name' if mode == "1" else 'author' if mode == "2" else 'genre'), end="")
    user_input = accept_input(is_int=False)
    print("\n\n")
    for x in show_one(user_input, int(mode)):
        print("Name: '{}', Author: '{}', Genre: '{}'\n".format(x[0].capitalize(), x[1].capitalize(), x[2].capitalize()))
    input("\n\n")


while running:
    initiate()
