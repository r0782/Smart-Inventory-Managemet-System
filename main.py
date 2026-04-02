from inventory import add_product, view_products
from accounting import record_sale, record_purchase, view_profit

def menu():
    while True:
        print("\n=== Inventory & Accounting System ===")
        print("1. Add Product")
        print("2. View Products")
        print("3. Record Sale")
        print("4. Record Purchase")
        print("5. View Profit")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_product()
        elif choice == "2":
            view_products()
        elif choice == "3":
            record_sale()
        elif choice == "4":
            record_purchase()
        elif choice == "5":
            view_profit()
        elif choice == "6":
            break
        else:
            print("Invalid choice")

menu()