""" this module provides useful functions for cli """
import os


def menu():
    """ prints a menu of options """
    cls()

    print("- " * 20)
    print("    Welcome to warehouse PyControl")
    print("- " * 20)

    print("[1] Add product")
    print("[2] Display catalog")
    print("[3] Display products out of stock")
    print("[4] Total stock value")
    print("[5] Cheapest Product")
    print("[6] Delete product")
    print("[7] Update product price")
    print("[8] Update product Stock\n")

    print("[s] Save")
    print("[x] Exit")


def cls():
    """ Clear the console """
    return os.system('/usr/bin/clear')


def header(text):
    """ Display a header """
    print("- " * 20)
    print(text)
    print("- " * 20)
