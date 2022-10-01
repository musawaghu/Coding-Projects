library = {}


def add_book():
    add_book_title = input("Enter a book title to add: ")
    if add_book_title not in library:
        library[add_book_title] = 1
    else:
        library[add_book_title] += 1


def find_book():
    find_book_title = input("Enter a book title to find: ")
    if find_book_title in library:
        print("There are ", library[find_book_title], " copies of this book")
    else:
        print("The given book is not in stock.")


def remove_book():
    remove_book_title = input("Enter a book title to remove: ")
    if remove_book_title in library:
        if library[remove_book_title] == 0:
            print("There are 0 copies of the book, the program will delete the book from the library")
            del library[remove_book_title]
        else:
            library[remove_book_title] -= 1


def main():
    user_input = 0
    while user_input != 'q':
        user_input = input("Enter 1 to add book, 2 to find a book, and 3 to remove book, and q to quit: ")
        if user_input.isdigit() and int(user_input) == 1:
            add_book()
        elif user_input.isdigit() and int(user_input) == 2:
            find_book()
        elif user_input.isdigit() and int(user_input) == 3:
            remove_book()
        if user_input == 'q':
            with open("data//library_inventory.txt", "a") as file:
                inventory = str(library)
                file.write(inventory)


main()
