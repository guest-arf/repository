#note this was made by ChatGPT
class VendingMachine:
    def __init__(self):
        self.items = {
            '1': {'name': 'Cupcake', 'price': 1.50},
            '2': {'name': 'Donut', 'price': 1.75},
            '3': {'name': 'Lollipop', 'price': 1.25},
            '4': {'name': 'Chocolate Bar', 'price': 2.00},
            '5': {'name': 'Gummy Bear', 'price': 0.75},
        }
    
    def display_items(self):
        print("Welcome to Two's Vending Machine!")
        print("Here are the available items:")
        for key, item in self.items.items():
            print(f"{key}. {item['name']} - ${item['price']:.2f}")
    
    def vend_item(self, item_number, amount_inserted):
        if item_number in self.items:
            item = self.items[item_number]
            if amount_inserted >= item['price']:
                change = amount_inserted - item['price']
                print(f"Vending {item['name']}...")
                if change > 0:
                    print(f"Your change: ${change:.2f}")
            else:
                print("Insufficient funds. Please insert more money.")
        else:
            print("Invalid item selection. Please choose a valid item number.")

def main():
    machine = VendingMachine()
    machine.display_items()
    
    item_number = input("Select an item number: ")
    amount_inserted = float(input("Insert amount of money: $"))
    
    machine.vend_item(item_number, amount_inserted)

if __name__ == "__main__":
    main()
