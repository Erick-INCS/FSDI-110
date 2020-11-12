""" Main module """

import pickle
from menu import cls, header, menu
from product import Product

# gloval vars
CATALOG = []
NEXT_ID = 1


def serialize_data():
    """ Save the catalog in a file called warehouse.data """
    try:
        writer = open('warehouse.data', 'wb')  # wb = write binary
        pickle.dump(CATALOG, writer)
        writer.close()
        print("** Data serialized!")
    except Exception:
        print('*** Error tring to save the data')


def deserialize_data():
    """ Read the catalog from file warehouse.data """
    global NEXT_ID

    try:
        reader = open('warehouse.data', 'rb')  # rb = read binary
        temp_list = pickle.load(reader)
        reader.close()

        for prod in temp_list:
            CATALOG.append(prod)

        # get the last id
        last = CATALOG[-1]
        NEXT_ID = last.id + 1

        how_many = len(CATALOG)
        print('** Read: ', how_many, 'products')
    except Exception:
        print('** Error, no data file found')


def total_stock_value():
    """ Calc the total stock value """

    header('Total Stock value')
    total = 0
    for prod in CATALOG:
        total += prod.Price * prod.Stock

    print('Total stock value: $', total)
    input("Press Enter to continue . . .")


def delete_product():
    """ Delete a prodcut """
    display_catalog(False)

    try:
        pr_id = int(input('ID of the item to delete: '))
        for elm in CATALOG:
            if elm.id == pr_id:
                CATALOG.remove(elm)
                print('Product removed')
                input('Press Enter to continue ...')
                return
        print("That product does not exist")
    except Exception:
        print('*** Invalid id')

    input('Press Enter to continue ...')


def register_product():
    """ Register product """
    global NEXT_ID
    cls()
    header("Register")
    title = input("Provide the title: ")
    category = input("Provide the category: ")

    try:
        stock = int(input("Provide the stock: "))
        price = float(input("Provide the price: "))

        product = Product(NEXT_ID, title, category, stock, price)
        NEXT_ID += 1
        CATALOG.append(product)
    except Exception:
        print('*** Unexpected format :/\n')
        input('Press Enter to continue ...')


def display_catalog(wait=True):
    """ Display catalog in screen """
    cls()
    header("Cataglog")
    for p in CATALOG:
        product_info(p)

    if wait:
        input("Press Enter to continue...")


def display_out_of_stock():
    """ Display out of catalog """
    cls()
    header("Out of stock")
    for p in CATALOG:
        if p.Stock == 0:
            product_info(p)
    input("Press Enter to continue...")


def product_info(product):
    """ Display product info """
    header(product.Title)
    print("Id:", product.id)
    print("Category:", product.Category)
    print("Stock:", product.Stock)
    print("Price:", product.Price, '\n')


def cheapest_product():
    """ Display the cheapest product """
    bg = 0
    prd = []
    vals = []
    for p in CATALOG:
        tmp = p.Stock * p.Price
        vals.append(tmp)
        if tmp > bg:
            bg = tmp
            prd = p

    product_info(prd)
    input("Press Enter to continue...")


def update_price():
    """ Update a product price """
    display_catalog(False)
    try:
        p_id = int(input('\nID of product to update: '))
        new_price = float(input('New price: '))

        print()
        for i, item in enumerate(CATALOG):
            if item.id == p_id:
                CATALOG[i].Price = new_price
                print('Price updated.')
                input('Press Enter to continue')
                return

        print(p_id, 'is not a valid ID')
        input('Press Enter to continue')
    except Exception:
        print('*** Error: Invalid input')


def update_stock():
    """ Update a product stock """
    display_catalog(False)
    try:
        p_id = int(input('\nID of product to update: '))
        new = float(input('New stock: '))

        print()
        for i, item in enumerate(CATALOG):
            if item.id == p_id:
                CATALOG[i].Stock = new
                print('Stock updated.')
                input('Press Enter to continue')
                return

        print(p_id, 'is not a valid ID')
        input('Press Enter to continue')

    except Exception:
        print('*** Error: Invalid input')


def save():
    """ Save the catalog """
    serialize_data()
    print('Data saved.')
    input('Press Enter to continue ...')


deserialize_data()
while True:
    menu()
    opt = input("Select a option: ")
    if opt == "x":
        break

    print()
    print()

    if opt == "1":
        register_product()
        serialize_data()

    elif opt == "2":
        display_catalog()

    elif opt == "3":
        display_out_of_stock()

    elif opt == "4":
        total_stock_value()

    elif opt == "5":
        cheapest_product()

    elif opt == "6":
        delete_product()

    elif opt == "7":
        update_price()

    elif opt == "8":
        update_stock()

    elif opt == "s":
        save()
