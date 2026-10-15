class productmodel:
    def __init__(self,id,title,category,price,brand,stock,is_true:bool=True):
        self.id=id
        self.title=title
        self.category=category
        self.price=price
        self.brand=brand
        self.stock=stock
        self.is_true=is_true

    def __repr__(self):
        return f"<{self.id,self.title,self.category,self.price,self.brand,self.stock,self.is_true}"

class users:
    def __init__(self, id, name, email, phone, city):
        self.id=id
        self.name=name
        self.email=email
        self.phone=phone
        self.city=city

    def __repr__(self):
        return f"{self.id,self.name,self.email,self.phone,self.city}"

class order:
    def __init__(self,id,userid,productid,quantity,paymentmode="UPI"):
        self.id=id
        self.userid=userid
        self.productid=productid
        self.quantity=quantity
        self.paymentmode=paymentmode

    def __repr__(self):
        return f"<{self.id,self.userid,self.productid,self.quantity,self.paymentmode}"


productdata=[
    productmodel(1, "Running Shoes", "Footwear", 2500, "Nike", 10, True),
    productmodel(2, "Sports Shoes", "Footwear", 3000, "Adidas", 15, True),
    productmodel(3, "Casual Shoes", "Footwear", 1800, "Puma", 20, True),
    productmodel(4, "Sneakers", "Footwear", 2200, "Nike", 8, False),
    productmodel(5, "Formal Shoes", "Footwear", 3500, "Bata", 12, True)
]

userdata = [
    users(1, "Rahul Sharma", "rahul@gmail.com", "9876543210", "Jaipur"),
    users(2, "Priya Verma", "priya@gmail.com", "9876543211", "Delhi"),
    users(3, "Amit Kumar", "amit@gmail.com", "9876543212", "Kota"),
    users(4, "Neha Singh", "neha@gmail.com", "9876543213", "Jodhpur"),
    users(5, "Rohit Jat", "rohit@gmail.com", "9876543214", "Ajmer")
]

orderdata = [
    order(1, 1, 101, 2),
    order(2, 2, 103, 1, "Cash"),
    order(3, 3, 102, 3, "Card"),
    order(4, 4, 105, 1),
    order(5, 5, 104, 2, "Net Banking")
]