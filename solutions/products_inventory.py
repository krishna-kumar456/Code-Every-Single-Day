"""
**Product Inventory Project** - Create an application which manages an inventory of products. Create a product cla\
ss which has a price, id, and quantity on hand. Then create an *inventory* class which keeps track of various prod\
ucts and can sum up the inventory value.
"""


class Product:
    def __init__(self, price, _id, quantity):
        price = price
        _id = _id
        quantity = quantity

    def get_product_details(self):
        return price, _id, quantity



class Inventory():
    
    product_inventory = {}
    

    def add_product_to_inventory(self, product_id, quantity):

        product_inventory[product_id] = quantity
        

    def get_inventory(self):

        return product_inventory
                
        
    
    def sum_of_inventory(self):

        inventory_count = 0
        
        for k,v in product_inventory.items():
            inventory_count += v

        return inventory_count



if __name__ == '__main__':

    conti = true
    print("Product-Inventory Application")
    print("-"*50)
    print(" ")

    while not conti:
        price = input('Please enter price for the product ')
        _id = input('Please enter product id ')
        quantity = input('Please enter the quantity of the product ')

        product = Product(price, _id, quantity)
        
        inventory = Inventory()
        inventory.add_product_to_inventory()
