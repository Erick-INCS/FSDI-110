""" this module provides useful functions for cli """
import os
import datetime

CH_LEN = 60
CHAR = "·"

def menu():
    """ prints a menu of options """
    curr_date = datetime.datetime.now()
    cls()
    print(CHAR * CH_LEN)
    print("    Welcome to warehouse PyControl     ", curr_date.strftime('%x %H:%M'))
    print(CHAR * CH_LEN)

    print("[1] Add product")
    print("[2] Display catalog")
    print("[3] Display products out of stock")
    print("[4] Total stock value")
    print("[5] Cheapest Product")
    print("[6] Delete product")
    print("[7] Update product price")
    print("[8] Update product Stock")
    print("[9] 3 most expensive products")
    print("[10] Distinct categories\n")

    print("[s] Save")
    print("[x] Exit")


def cls():
    """ Clear the console """
    return os.system('/usr/bin/clear') # i'm using linux sorry for the error


def header(text):
    """ Display a header """
    print(CHAR * CH_LEN)
    print(text)
    print(CHAR * CH_LEN)


def product_info(product):
    """ Display product info """
    print("{} | {} | {} | {} | {}".format(
        str(product.id).rjust(3),
        ('[' + product.Title + ']').ljust(20),
        str(product.Category).ljust(12),
        str(product.Stock).rjust(3),
        str(product.Price).rjust(7)
    ))