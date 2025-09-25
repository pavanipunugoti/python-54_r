class Product:
    def __init__(self, id,name,price): # to create instant variables..we use init method.
        self.id=id
        self.name=name  # to display the values..
        self.price=price
class Store:
    def __init__(self):
        self.products=[
             Product(1,"iphone",1200000),
             Product(2,"samsung",300000),
             Product(3,"laptop",600000),
             Product(4,"smart watch",40000),
         ]
    
        self.cart=[]
        
    def view_produts(self):  # view Prodcuts..
        for product in self.products:
            print(f"{product.id} . {product.name} - {product.price}")
            
    def add_products(self): # to add the items to cart..
        product_id=int(input("Enter a product id:"))
        for product in self.products:
            if(product.id==product_id):
                self.cart.append(product)
                print("Item added into the cart successfully")
                return # we use here do not print..item not found.
        print("Item not found")
    
    def view_cart(self):
        if(len(self.cart)==0):
            print("Cart is empty.")
            return
        
        total=0  # this is used in add the price in cart..
        for product in self.cart:
            total+=product.price
            print(f"{product.id} . {product.name} - {product.price}")
        print("Total cost: ",total)  #to print the total cost.
        
    def remove_products(self):
        product_id=int(input("Enter a product id for removing product:"))
        for product in self.cart:
            if(product.id== product_id):
                self.cart.remove(product)
                print(" Product removed Successfully..")
                return
        print("item not found.!")
        
    def checkout(self):
        print("Your order is placed successfully...!")
        self.cart.clear()
    
    def run(self):
        while True:
            print("1) view products")
            print("2)  add producs")
            print("3) view products")
            print("4) remove products")
            print("5) checkout")
            print("6) exit")
            option=int(input("enter a number:"))

                  
    
        
            

        
            
            
# store=Store()
# store.view_products() # see the items..
# store.view_cart()#To see the items in cart.
# store.add_products()  # add 
# store.view_cart()  # chudanikii
# store.add_products()
# store.view_cart()# o see the cart details..
# store.remove_products() 
# store.view_cart()
# store.checkout()
# store.view_cart()



        
        
        
        
    
        