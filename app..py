import os
import sys

from colorama import Fore, Style
from pyfiglet import figlet_format

from utils import database

WELCOME_MESSAGE = figlet_format('Bookstore')
USER_MENU = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit
    
Select an option: """


def green(text):
    return Fore.GREEN + Style.DIM + text + Style.RESET_ALL


def red(text):
    return Fore.RED + Style.DIM + text + Style.RESET_ALL


def blue(text):
    return Fore.BLUE + Style.DIM + text + Style.RESET_ALL


def magenta(text):
    return Fore.MAGENTA + Style.DIM + text + Style.RESET_ALL


def prompt_add_book():
    print('\n====== Add Book ======')
    name = input('Enter the new book name: ')
    author = input('Enter the new book author: ')
    database.add_new_book(name, author)
    print('======================\n')


def list_books():
    books = database.get_all_books()
    print('\n====== All Books =====')
    for book in books:
        read = green('YES') if book['read'] else red('NO')
        print(f"{magenta(book['name'])} by {blue(book['author'])}, read: {read}")
    print('======================\n')


def prompt_read_book():
    print('\n====== Mark Read =====')
    name = input('Enter the name of the book you just finished reading: ')
    database.mark_as_read(name)
    print('======================\n')


def prompt_delete_book():
    print('\n====== Delete Book =====')
    name = input('Enter the name of the book you wish to delete: ')
    database.delete_book(name)
    print('======================\n')


def menu():
    database.create_books_table()
    print(WELCOME_MESSAGE)
    option = input(USER_MENU)
    operations = {
        'a': prompt_add_book,
        'l': list_books,
        'r': prompt_read_book,
        'd': prompt_delete_book
    }
    while option != 'q':
        try:
            operations[option]()
        except KeyError:
            print(f'Invalid option {option}, select a valid option.')
        except Exception as ex:
            print(red(f'An error has occurred: {ex}'))
        finally:
            input('press enter to continue...')
            sys.stdout.flush()
            os.system('clear')
            option = input(USER_MENU)


menu()