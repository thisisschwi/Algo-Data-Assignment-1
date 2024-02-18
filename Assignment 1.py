# 100878918
# Kelvin Wong
import time
products = []  # start an empty list
newtime = 0

def load_product_data():
    global products
    file = open('product_data.txt', 'r') # open the file as file
    for line in file:
        product_info = line.strip().split(',') # remove white space and split by ,
        product = {'ID': int(product_info[0]),'Name': product_info[1],'Price': float(product_info[2]),
                   'Category': product_info[3]} # turn the list into a list of dictionaries
        products.append(product) # append to the empty list
    return products

def sort_list(products):
    global newtime
    n = len(products)
    start_time = time.time()
    for i in range(n):
        for j in range(0, n - i - 1):
            if products[j]['Price'] > products[j + 1]['Price']:
                products[j], products[j + 1] = products[j + 1], products[j]
    time.sleep(1)
    end_time = time.time()
    newtime = end_time - start_time
    newtime -=1
    return products

def time_taken():
    sort_list(products)
    store_product_data(products)
    print(f'Time taken to sort is {newtime} seconds')

def insert_item(ID,Name,Price,Category):
    global products
    new_product = {'ID': ID, 'Name': Name, 'Price': Price, 'Category': Category}
    products.append(new_product)
    store_product_data(products)
    return products

def store_product_data(products):
    save = open('save.txt', 'w')
    for product in products:
        save.write(f"{product['ID']},{product['Name']},{product['Price']},{product['Category']}\n")
    save.close()

def search_product(products, key, value):
    error = 'Item not found'
    if isinstance(value, str):
        normalized_value = value.strip().lower()
    elif isinstance(value, (int, float)):
        normalized_value = value
    else:
        return error
    for product in products:
        if isinstance(product[key], str):
            normalized_product_value = product[key].strip().lower()
        elif isinstance(product[key], (int, float)):
            normalized_product_value = product[key]
        else:
            continue
        if normalized_product_value == normalized_value:
            return product
    return error

def search_function():
    error = "invalid input"
    see = input('What would you like to search by?:')
    see = see.lower()
    if see == 'id':
        see = int(input('Enter ID:'))
        return search_product(products, 'ID', see)
    if see == 'name':
        see = input('Enter Name:')
        return search_product(products, 'Name', see)
    if see == 'price':
        see = float(input('Enter Price:'))
        return search_product(products, 'Price', see)
    if see == 'category':
        see = input('Enter Category:')
        return search_product(products, 'Category', see)
    return error

def main():
    print('Data Loading......\n')
    products = load_product_data()
    while True:
        print('-'*80)
        op = input('Enter 1 to input, 2 to update, 3 to delete, 4 to search, 5 to sort, 6 to print, 7 to stop:')
        if op == '1':
            ID = int(input('What ID?:'))
            Name = input('What Name?:')
            Price = float(input('What Price?:'))
            Category = input('What Category?:')
            insert_item(ID, Name, Price, Category)
            time_taken()
        if op == '2':
            output = search_function()
            if output == 'invalid input':
                continue
            if output == 'Item not found':
                continue
            else:
                print(f'current item: {output}')
                ID = int(input('What ID?:'))
                Name = input('What Name?:')
                Price = float(input('What Price?:'))
                Category = input('What Category?:')
                updated_att = {'ID': ID, 'Name': Name, 'Price': Price, 'Category': Category}
                for product in products:
                    if output == product:
                        product.update(updated_att)
                time_taken()
        if op == '3':
            output = search_function()
            if output == 'invalid input':
                continue
            if output == 'Item not found':
                continue
            else:
                output_id = int(output['ID'])
                for product in products:
                    if product['ID'] == output_id:
                        products.remove(product)
                        print(f'Item deleted')
                        time_taken()

        if op == '4':
            output = search_function()
            print(output)
        if op == '5':
            time_taken()
        if op == '6':
            for i in products:
                print(i)
        if op == '7':
            break
        else:
            continue


main()