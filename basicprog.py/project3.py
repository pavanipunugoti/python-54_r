class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

class Store:
    def __init__(self):
        self.products = [
            Product(1, "iPhone", 12000),
            Product(2, "Samsung", 30000),
            Product(3, "Laptop", 60000),
            Product(4, "Smart Watch", 4000)
        ]
        self.cart = []

    def view_products(self):
        print("Available Products:")
        for product in self.products:
            print(f"{product.id}. {product.name} - ₹{product.price}")

    def add_product(self):
        product_id = int(input("Enter a product id to add: "))
        for product in self.products:
            if product.id == product_id:
                self.cart.append(product)
                print("Item added to cart successfully!")
                return
        print("Item not found.")

    def view_cart(self):
        if not self.cart:
            print("Cart is empty.")
            return
        total = 0
        print("Your Cart:")
        for product in self.cart:
            print(f"{product.id}. {product.name} - ₹{product.price}")
            total += product.price
        print("Total cost:", total)

    def remove_product(self):
        product_id = int(input("Enter a product id to remove: "))
        for product in self.cart:
            if product.id == product_id:
                self.cart.remove(product)
                print("Product removed successfully!")
                return
        print("Item not found in cart.")

    def checkout(self):
        if not self.cart:
            print("Cart is empty. Add products before checkout.")
            return
        print("Your order is placed. Thank you for shopping!")


store = Store()
while True:
    print("\n1. View Products\n2. Add Product to Cart\n3. View Cart\n4. Remove Product from Cart\n5. Checkout\n6. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        store.view_products()
    elif choice == '2':
        store.add_product()
    elif choice == '3':
        store.view_cart()
    elif choice == '4':
        store.remove_product()
    elif choice == '5':
        store.checkout()
    elif choice == '6':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")