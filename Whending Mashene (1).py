# Maryam's Vending Machine Program

# Welcome 
# ██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗    ████████╗ ██████╗                                             
# ██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝    ╚══██╔══╝██╔═══██╗                                            
# ██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗         ██║   ██║   ██║                                            
# ██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝         ██║   ██║   ██║                                            
# ╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗       ██║   ╚██████╔╝                                            
#  ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝       ╚═╝    ╚═════╝                                             
#                                                                                                                                
# ███╗   ███╗ █████╗ ██████╗ ██╗   ██╗ █████╗ ███╗   ███╗███████╗    ██╗   ██╗███████╗███╗   ██╗██████╗ ██╗███╗   ██╗ ██████╗     
# ████╗ ████║██╔══██╗██╔══██╗╚██╗ ██╔╝██╔══██╗████╗ ████║██╔════╝    ██║   ██║██╔════╝████╗  ██║██╔══██╗██║████╗  ██║██╔════╝     
# ██╔████╔██║███████║██████╔╝ ╚████╔╝ ███████║██╔████╔██║███████╗    ██║   ██║█████╗  ██╔██╗ ██║██║  ██║██║██╔██╗ ██║██║  ███╗    
# ██║╚██╔╝██║██╔══██║██╔══██╗  ╚██╔╝  ██╔══██║██║╚██╔╝██║╚════██║    ╚██╗ ██╔╝██╔══╝  ██║╚██╗██║██║  ██║██║██║╚██╗██║██║   ██║    
# ██║ ╚═╝ ██║██║  ██║██║  ██║   ██║   ██║  ██║██║ ╚═╝ ██║███████║     ╚████╔╝ ███████╗██║ ╚████║██████╔╝██║██║ ╚████║╚██████╔╝    
# ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝      ╚═══╝  ╚══════╝╚═╝  ╚═══╝╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝     
#                                                                                                                                
# ███╗   ███╗ █████╗  ██████╗██╗  ██╗██╗███╗   ██╗███████╗                                                                        
# ████╗ ████║██╔══██╗██╔════╝██║  ██║██║████╗  ██║██╔════╝                                                                        
# ██╔████╔██║███████║██║     ███████║██║██╔██╗ ██║█████╗                                                                          
# ██║╚██╔╝██║██╔══██║██║     ██╔══██║██║██║╚██╗██║██╔══╝                                                                          
# ██║ ╚═╝ ██║██║  ██║╚██████╗██║  ██║██║██║ ╚████║███████╗                                                                        
# ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝                                                                        
#                                                                                                                                

# The vending machine code is below this:-


class VendingMachine:
    def __init__(self):
        self.items = {
            '1': {'name': 'Coke', 'price': 1.50, 'stock': 10},
            '2': {'name': 'Pepsi', 'price': 1.50, 'stock': 10},
            '3': {'name': 'Water', 'price': 1.00, 'stock': 10},
            '4': {'name': 'Chips', 'price': 1.25, 'stock': 10},
            '5': {'name': 'Chocolate', 'price': 1.75, 'stock': 10}
        }
        self.balance = 0.0

    def display_menu(self):
        print("\n" + "="*30)
        print("  💐💖 Welcome to Maryam's Vending Machine 😂😂😂😂😂😂😂")
        print("="*30)
        print("Available items 🏬:")
        for code, item in self.items.items():
            print(f"{code}: {item['name']} - ${item['price']:.2f} (Stock: {item['stock']})")
        print("="*30)

    def select_item(self):
        item_code = input("Select an item by code: ")
        return item_code

    def insert_money(self):
        amount = float(input("Insert money 💸 (or type 0 to exit): "))
        return amount

    def process_selection(self, code):
        if code in self.items:
            item = self.items[code]
            if item['stock'] > 0:
                if self.balance >= item['price']:
                    item_cost = item['price']
                    self.balance -= item_cost
                    item['stock'] -= 1
                    print(f"\nDispensed: {item['name']}.")
                    self.return_change()
                else:
                    print("\nInsufficient balance❌. Please insert more money💸.")
            else:
                print("\nSorry, this item is out of stock.")
        else:
            print("\nInvalid selection❌. Please choose a valid item code😊.")

    def return_change(self):
        if self.balance > 0:
            print(f"Change returned: ${self.balance:.2f}.")
        else:
            print("No change to return.")
        self.balance = 0.0  # Reset the balance after returning the change

    def run(self):
        while True:
            self.display_menu()
            item_code = self.select_item()
            if item_code == '0':
                print("Thank you for using Maryam's Vending Machine 😍💐")
                break
            self.balance += self.insert_money()
            self.process_selection(item_code)

# Run the vending machine
if __name__ == "__main__":
    machine = VendingMachine()
    machine.run()