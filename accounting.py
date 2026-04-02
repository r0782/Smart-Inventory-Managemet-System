from data import load, save #--> Importing the load and save functions from the data module, which are used to read and write JSON files.

PRODUCT_FILE = "data/products.json" #--> Path to the product JSON file, which contains the inventory data. This file is used to load the current inventory and update it when sales or purchases are recorded.
LEDGER_FILE = "data/ledger.json" #--> Path to the ledger JSON file, which contains the financial data (revenue and expenses). This file is used to load the current financial data and update it when sales or purchases are recorded.

def record_sale():
    products = load(PRODUCT_FILE)
    ledger = load(LEDGER_FILE)

    pid = input("Enter product ID: ")
    qty = int(input("Enter quantity sold: "))

    if pid in products and products[pid]["quantity"] >= qty:#--> Checking if the product ID exists in the products dictionary and if the available quantity is greater than or equal to the quantity sold. If both conditions are true, we proceed to calculate the total revenue from the sale. If the product ID does not exist or if there is not enough stock, we print a message indicating that there is not enough stock.
        total = qty * products[pid]["price"]

        products[pid]["quantity"] -= qty #--> Reducing the quantity of the product in the inventory by the quantity sold. This updates the inventory to reflect the sale.
        ledger["revenue"] = ledger.get("revenue", 0) + total #--> Updating the revenue in the ledger by adding the total revenue from the sale. The get method is used to retrieve the current revenue, and if it does not exist, it defaults to 0.

        save(PRODUCT_FILE, products)
        save(LEDGER_FILE, ledger)

        print("Sale recorded!")
    else:
        print(" Not enough stock")

def record_purchase():
    products = load(PRODUCT_FILE)
    ledger = load(LEDGER_FILE)

    pid = input("Enter product ID: ")
    qty = int(input("Enter quantity purchased: "))
    cost = float(input("Enter total cost: "))

    if pid in products: #--> Checking if the product ID exists in the products dictionary. If it exists, we proceed to update the quantity of the product in the inventory by adding the quantity purchased. If the product ID does not exist, we print a message indicating that the product was not found and return from the function.
        products[pid]["quantity"] += qty
    else:
        print("Product not found")
        return

    ledger["expenses"] = ledger.get("expenses", 0) + cost #--> Updating the expenses in the ledger by adding the total cost of the purchase. The get method is used to retrieve the current expenses, and if it does not exist, it defaults to 0.

    save(PRODUCT_FILE, products)
    save(LEDGER_FILE, ledger)

    print("Purchase recorded!")

def view_profit():
    ledger = load(LEDGER_FILE)

    revenue = ledger.get("revenue", 0)
    expenses = ledger.get("expenses", 0)

    print("Revenue:", revenue)
    print("Expenses:", expenses)
    print("Profit:", revenue - expenses)