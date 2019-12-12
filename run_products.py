from db_products_oop import *
from employees_oop import *

products_table = NWProducts()
employees_table = NWEmployee()


while True:
    print('_________________________________________')
    print('choose 1 for getting all products')
    print('choose 2 for getting 1 product')
    print('choose 3 for top 10 products by price')
    print('choose 4 for bottom 10 products by price')
    print('choose 5 to search for product by name ')
    print('_________________________________________')

    user_input = input('chose a number listed in the options').strip()

    if user_input == '1':
        print('get all products')
        products_table.print_all()

    elif user_input == '2':
        print('getting 1 product')
        id = products_table.set_id()
        product = products_table.read_one(id)
        print(product)

    elif user_input == '3':
        print('Getting top 10 products by price')
        products = products_table.top_10_by_price()
        print(products)

    elif user_input == '4':
        print('Getting bottom 10 products by price')
        products = products_table.bottom_10_by_price()
        print(products)

    elif user_input == '5':
        print('Search for a product by name ')
        search = products_table.search_product_name()
        print(search)



    elif 'bye' in user_input or 'exit' in user_input:
        print('goodbye, thank you!')
        break

    else:
        print('I didnt catch that. please choose an available option')