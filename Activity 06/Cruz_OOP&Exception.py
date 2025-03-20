#Create an item management application (CRUD application). 
#The Item must consist of the following id, name, description and price.

class Item:
    def __init__(self, id, name, description, price):
        if price < 0:
            raise ValueError("Price cannot be negative.")
        
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        
    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Description: {self.description}, Price: ${self.price:.2f}"

class ItemManagement:
    def __init__(self):
        self.items = {}
        
    def create_items(self, id, name, description, price):
        if id in self.items:
            print("Error: Item ID already exists.")
            return
        
        try:
            item = Item(id, name, description, price)
            self.items[id] = item
            print("Item added successfully.")
        except ValueError as e:
            print("Error:", e)
            
    def read_items(self):
        if not self.items:
            print("Items not available.")
        else:
            for item in self.items.values():
                print(item)
                
    def update_item(self, id, name=None, description=None, price=None):
        if id not in self.items:
            print("Error: Item not found.")
            return
            
        item = self.items[id]
        if name:
            item.name = name
        if description:
            item.description = description
        if price is not None:
            if price < 0:
                print("Error: Price cannot be negative.")
                return
            item.price = price
        print("Item updated successfully.")
        
    def del_items(self, id):
        if id in self.items:
            del self.items[id]
            print("Item deleted successfully.")
        else:
            print("Error: Item not found.")

def main():
    managing = ItemManagement()
    while True:
        print("\nITEM MANAGEMENT MENU:")
        print("[1] - Add Item")
        print("[2] - View Items")
        print("[3] - Update Item")
        print("[4] - Delete Item")
        print("[5] - Exit")
        
        choice = input("\nEnter your choice: ")
        
        if choice == '1':
            try:
                print("\n[1] - ADD ITEM")
                id = input("Enter item ID: ")
                name = input("Enter item name: ")
                description = input("Enter item desciption: ")
                price = float(input("Enter item price: "))
                managing.create_items(id, name, description, price)
            except ValueError:
                print("Error: Invalid input. Please enter a numeric value.")
        elif choice == '2':
            print("\n[2] - VIEW ITEMS")
            managing.read_items()
        elif choice == '3':
            print("\n[3] - UPDATE ITEM")
            id = input("Enter new item ID: ")
            name = input("Enter new name: ")
            description = input("Enter new description: ")
            try:
                price_input = input("Enter new price: ")
                price = float(price_input)
                managing.update_item(id, name, description, price)
            except ValueError:
                print("Error: Invalid input. Please enter a numeric value.")
        elif choice == '4':
            print("\n[4] - DELETE ITEM")
            id = input("Enter item ID to delete: ")
            managing.del_items(id)
        elif choice == '5':
            print("\n[5] - EXIT")
            print("Exiting the program... Goodbye :>")
            break
        else:
            print("Invalid choice. Please select a valid option.")
            
if __name__ == "__main__":
    main()