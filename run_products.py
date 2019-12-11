from db_products_oop import *

products_table = NWProducts()


while True:
    print('choose 1 for getting all products')
    print('choose 2 for getting 1 product')

    user_input = input('choose 1, 2 or 3').strip()

    if user_input == '1':
        print('get all products')
        products_table.print_all()

    elif user_input == '2':
        print('getting 1 product')
        id = products_table.set_id()
        product = products_table.read_one(id)
        print(product)

    elif 'bye' in user_input or 'exit' in user_input:
        print('goodbye, thank you!')
        break

    else:
        print('I didnt catch that. please choose an available option')