import csv
import os
import locale


products = []           #lista

def format_currency(value):
    return locale.currency(value,grouping=True)


def load_data(filename): 
    with open(filename, 'r') as file:       #öppnar en fil med read-rättighet
        reader = csv.DictReader(file)
        for row in reader:
            id = int(row['id'])
            name = row['name']
            desc = row['desc']
            price = float(row['price'])
            quantity = int(row['quantity'])
            
            products.append(
                {                   
                    "id": id,       
                    "name": name,
                    "desc": desc,
                    "price": price,
                    "quantity": quantity
                }
            )
    return products


def product_list(products):
    number = 1
    for product in products:
        name = product["name"]
        price = product["price"]
        quantity = product["quantity"]
        
        print(f"{number}. {name} - {price} ({quantity} st)")
        number += 1
    
    
def get_id(products, product_id):
    for product in products:
        if product["id"] == product_id:
            return product
    return None

def remove_id(products, product_id):
    for product in products:
        if product["id"] == product_id:
            products.remove(product)
            return True
    return False

def add_product(products):
    id = int(input("Välj ID: "))
    name = input("Namn")
    desc = input("Beskrivning")
    price = float(input("Pris"))
    quantity = int(input("Kvantitet"))
    
    products.append(
        {
            "id": id,
            "name": name,
            "desc": desc,
            "price": price,
            "quantity": quantity
        }
    )

def update_qty(products):
    product_id = int(input("Produktens id vars kvantitet du vill ändra: "))
    products = get_id(products, product_id)
    if product:
        new_qty = int(input(f"Ny kvantitet för {product["name"]}: "))
        product["quantity"] = new_qty
        print("Kvantitet uppdaterad")
    else: 
        print("Produkten finns inte")
        
def update_product(products):
    product_id = int(input("Ange produktens id för att uppdatera: "))
    product = get_id(products, product_id)
    if product:
        product["name"] = input(f"Nytt namn ({product["name"]}): ") or product["name"]
        product["desc"] = input(f"Ny beskrivning ({product["desc"]}): ") or product["desc"]
        
        try:
            price_input = input(f"Nytt pris({product["price"]}):")
            if price_input:
                product["price"] = float(price_input)
        except ValueError:
            pass
        
        try:
            qty_input = input(f"Ny kvantitet({product["quantity"]}): ")
            if qty_input:
                product["quantity"] = int(qty_input)
        except ValueError:
            pass
        print("Produkt uppdaterad")
    else:
        print("Produkten finns inte")
        
def menu(produts):
    while True:
        print("1. Visa produkter")
        print("2. Lägg till produkt")
        print("3. Ta bort produkt")
        print("4. Uppdatera kvantitet")
        print("5. Ändra produkt")
        
        choice = int(input())
        
        if choice == 1:
            product_list(products)
        elif choice == 2:
            add_product(products)
        elif choice == 3:
            prod_id = int(input("Ange id på produkt som ska tas bort: "))
            if remove_id(products, prod_id):
                print("Produkt borttagen")
            else: 
                print("Produkt finns inte")
                


#TODO: hur gör man så funktionen load_data returnerar products istället?
#TODO: gör så man kan se en numrerad lista som börjar på 1.
#TODO: skriv en funktion som returnerar en specifik produkt med hjälp av id
#TODO: skriv en funktion som tar bort en specifik produkt med hjälp av id


locale.setlocale(locale.LC_ALL, 'sv_SE.UTF-8')  
os.system('cls')

products = load_data('db_products.csv')

product_list(products)

search_id = int(input("Ange produktens id: ")) - 1
product = get_id(products, search_id)

if product:
    print(f"Hittade: {product['name']} - {format_currency(product['price'])}")
else:
    print("Produkten finns inte")


product_list(products)

id = int(input("Ange id på produkt som du vill ta bort: ")) -1
removed = remove_id(products, id)

if removed:
    print("Produkten togs bort\n")
    product_list(products)
else: print("Produkten finns inte")





