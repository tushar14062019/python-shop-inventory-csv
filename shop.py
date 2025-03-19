# Program
import csv
import logging
from tabulate import tabulate

logging.basicConfig(
    filename='shop_system.log',
    level=logging.INFO,  # Adjust the log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class Product:
    def __init__(self, Pid, Pname, price, Quantity):
        self.Pid = Pid
        self.Pname = Pname
        self.price = price
        self.Quantity = Quantity

class Inventory:
    def __init__(self, filePname='inventory.csv'):
        self.filePname = filePname
        self.products = self.load_inventory()

    def load_inventory(self):
        products = {}
        try:
            with open(self.filePname, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    products[int(row['Pid'])] = Product(
                        int(row['Pid']),
                        row['Pname'],
                        float(row['price']),
                        int(row['Quantity'])
                    )
            logging.info("Inventory loaded successfully.")
        except FileNotFoundError:
            logging.error("Inventory file not found.")
        return products

    def save_inventory(self):
        with open(self.filePname, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Pid', 'Pname', 'price', 'Quantity'])
            for product in self.products.values():
                writer.writerow([product.Pid, product.Pname, product.price, product.Quantity])
        logging.info("Inventory saved successfully.")

    def add_product(self, product):
        self.products[product.Pid] = product
        self.save_inventory()
        logging.info(f"Product added: {product.Pname} (PID: {product.Pid})")

    def update_product_Quantity(self, Pid, Quantity):
        if Pid in self.products:
            self.products[Pid].Quantity -= Quantity
            self.save_inventory()
            logging.info(f"Updated stock for {self.products[Pid].Pname} (PID: {Pid}) by {Quantity} units.")
        else:
            logging.warning(f"Attempted to update quantity for non-existent product (PID: {Pid}).")

    def view_inventory(self):
        table = [[p.Pid, p.Pname, p.price, p.Quantity] for p in self.products.values()]
        print(tabulate(table, headers=["ID", "Pname", "Price", "Quantity"], tablefmt="grid"))

class Sale:
    def __init__(self, sale_id, Pid, Pname, Quantity_sold, total_price):
        self.sale_id = sale_id
        self.Pid = Pid
        self.Pname = Pname
        self.Quantity_sold = Quantity_sold
        self.total_price = total_price

class SalesManager:
    def __init__(self, filePname='sales.csv'):
        self.filePname = filePname
        self.sales = self.load_sales()

    def load_sales(self):
        sales = []
        try:
            with open(self.filePname, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    sales.append(Sale(
                        int(row['sale_id']),
                        int(row['Pid']),
                        row['Pname'],
                        int(row['Quantity_sold']),
                        float(row['total_price'])
                    ))
            logging.info("Sales records loaded successfully.")
        except FileNotFoundError:
            logging.error("Sales file not found. Starting with no sales records.")
        return sales

    def save_sales(self):
        with open(self.filePname, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['sale_id', 'Pid', 'Pname', 'Quantity_sold', 'total_price'])
            for sale in self.sales:
                writer.writerow([sale.sale_id, sale.Pid, sale.Pname, sale.Quantity_sold, sale.total_price])
        logging.info("Sales records saved successfully.")

    def record_sale(self, sale):
        self.sales.append(sale)
        self.save_sales()
        logging.info(f"Sale recorded: {sale.Pname} (PID: {sale.Pid}), Quantity: {sale.Quantity_sold}, Total: {sale.total_price}")

    def view_sales_report(self):
        table = [[s.sale_id, s.Pid, s.Pname, s.Quantity_sold, s.total_price] for s in self.sales]
        print(tabulate(table, headers=["Sale ID", "Product ID", "Pname", "Quantity Sold", "Total Price"], tablefmt="grid"))

class ShopSystem:
    def __init__(self):
        self.inventory = Inventory()
        self.sales_manager = SalesManager()

    def menu(self):
        while True:
            print("\n--- Small Shop Management System ---")
            print("1. View Inventory")
            print("2. Add Product to Inventory")
            print("3. Process a Sale")
            print("4. View Sales Report")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.inventory.view_inventory()
            elif choice == '2':
                self.add_product()
            elif choice == '3':
                self.process_sale()
            elif choice == '4':
                self.sales_manager.view_sales_report()
            elif choice == '5':
                print("Exiting... Goodbye!")
                logging.info("System exit.")
                break
            else:
                logging.warning("Invalid menu choice entered.")
                print("Invalid choice. Please try again.")

    def add_product(self):
        Pid = int(input("Enter PID: "))
        Pname = input("Enter Pname: ")
        price = float(input("Enter Product Price: "))
        Quantity = int(input("Enter Product Quantity: "))
        product = Product(Pid, Pname, price, Quantity)
        self.inventory.add_product(product)
        logging.info(f"Product added through menu: {Pname} (PID: {Pid}, Price: {price}, Quantity: {Quantity})")

    def process_sale(self):
        sale_id = int(input("Enter Sale ID: "))
        while True:
            Pid = input("Enter PID to sell (or 'done' to finish): ")
            if Pid.lower() == 'done':
                break

            Pid = int(Pid)
            if Pid not in self.inventory.products:
                logging.warning(f"Attempted sale for non-existent product (PID: {Pid}).")
                print("Product not found!")
                continue

            product = self.inventory.products[Pid]
            Quantity = int(input(f"Enter Quantity for {product.Pname}: "))
            if Quantity > product.Quantity:
                logging.warning(f"Attempted sale with insufficient stock (PID: {Pid}).")
                print("Insufficient stock!")
                continue

            total_price = product.price * Quantity
            self.inventory.update_product_Quantity(Pid, Quantity)
            sale = Sale(sale_id, Pid, product.Pname, Quantity, total_price)
            self.sales_manager.record_sale(sale)
            logging.info(f"Sale {sale_id} processed: {product.Pname} (PID: {Pid}), Quantity: {Quantity}, Total: {total_price}")

if __name__ == "__main__":
    shop_system = ShopSystem()
    shop_system.menu()
