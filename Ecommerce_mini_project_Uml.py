class Product:
    def __init__(self,product_id,name,price,stock,category):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock
        self.category = category
    
    def to_dict(self):
        return vars(self)
    
class Cart:
    def __init__(self,cart_id):
        self.cart_id = cart_id
        self.products = {}
        self.total_amount = 0

    def add_product(self,product):
        if product.stock > 0:
            self.products[product.product_id]=self.products.get(product.product_id,0)+1
            self.total_amount += product.price
            product.stock -= 1
            print(product.name,"added to cart.")
        else:
            print(product.name,"is out of stock")

    def to_dict(self):
        return {"cart_id":self.cart_id,"products":self.products,"total_amount":self.total_amount}
    
class Order:
    def __init__(self,order_id,user,cart):
        self.order_id = order_id
        self.user_id = user.user_id
        self.items = cart.products.copy()
        self.total_price = cart.total_amount
        self.status ="Created"

    def to_dict(self):
        return vars(self)
    
class Payment:
    def __init__(self,payment_id,order,method):
        self.payment_id = payment_id
        self.order_id = order.order_id
        self.method = method
        self.payment_status = "Pending"

    def process_payment(self,order):
        if order.total_price > 0:
            self.payment_status = "Success"
            order.status = "Placed"
            print("Payment successful")
        else:
            self.payment_status = "Failed"
            print("Payment failed")
    def to_dict(self):
        return vars(self)
    
class User:
    def __init__(self,user_id,name,email):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.cart = Cart(user_id)

    def place_order(self,order_id):
        return Order(order_id,self,self.cart)
    
    def to_dict(self):
        return {"user_id":self.user_id,
                  "name": self.name,
                  "email":self.email,
                  "cart":self.cart.to_dict()
                  }

class Admin:
    def __init__(self,admin_id,name,email):
        self.admin_id = admin_id
        self.name = name
        self.email = email

    def add_product(self,db,product):
        db["products"][product.product_id] = product.to_dict()
        print(product.name,"added by admin")

    def remove_product(self,db,product_id):
        if product_id in db["products"]:
            del db["products"][product_id]
            print("Product removed by admin.")


if __name__ == "__main__":

    database = {"products":{},
                "users":{},
                "orders":{},
                "payments":{}}
    
    admin = Admin(1,"Admin","admin@amazon.com")

    p1 = Product(101,"Laptop",50000,5,"Electonics")
    p2 = Product(102,"Mouse",500,10,"Electronics")

    admin.add_product(database,p1)
    admin.add_product(database,p2)

    user = User(1,"Hrishikesh","hrishi@gmail.com")
    database["users"][user.user_id]= user.to_dict()

    user.cart.add_product(p1)
    user.cart.add_product(p2)

    order = user.place_order(1001)
    database["orders"][order.order_id] = order.to_dict()
 
    payment = Payment(501,order,"UPI")
    payment.process_payment(order)
    database["payments"][payment.payment_id] = payment.to_dict()


    print("\n===== FINAL DATABASE STRUCTURE =========\n")
    print(database)
    

