class productmodal:
    def __init__(self,id,title,category,price,stock,brand,is_active=True):
        self.id=id
        self.title=title
        self.category=category
        self.price=price
        self.stock=stock
        self.brand=brand
        self.is_active=is_active

    def __repr__(self):
        return f"<{self.id,self.title,self.category,self.price,self.stock,self.brand,self.is_active}"

data=[]

products= [
    {
        "id": 1,
        "title": "Mobile",
        "category": "communication",
        "price": 500,
        "stock": 10,
        "brand": "Apple",
        "is_active": True
    },
    {
        "id": 2,
        "title": "Laptop",
        "category": "electronics",
        "price": 55000,
        "stock": 15,
        "brand": "Dell",
        "is_active": True
    },
    {
        "id": 3,
        "title": "Headphones",
        "category": "audio",
        "price": 1500,
        "stock": 25,
        "brand": "Sony",
        "is_active": True
    },
    {
        "id": 4,
        "title": "Keyboard",
        "category": "accessories",
        "price": 800,
        "stock": 20,
        "brand": "Logitech",
        "is_active": True
    },
    {
        "id": 5,
        "title": "Mouse",
        "category": "accessories",
        "price": 400,
        "stock": 30,
        "brand": "HP",
        "is_active": True
    },
    {
        "id": 6,
        "title": "Smart Watch",
        "category": "wearables",
        "price": 2500,
        "stock": 12,
        "brand": "Samsung",
        "is_active": True
    },
    {
        "id": 7,
        "title": "Tablet",
        "category": "electronics",
        "price": 18000,
        "stock": 8,
        "brand": "Lenovo",
        "is_active": True
    },
    {
        "id": 8,
        "title": "Charger",
        "category": "accessories",
        "price": 600,
        "stock": 40,
        "brand": "OnePlus",
        "is_active": True
    },
    {
        "id": 9,
        "title": "Speaker",
        "category": "audio",
        "price": 2200,
        "stock": 18,
        "brand": "JBL",
        "is_active": True
    },
    {
        "id": 10,
        "title": "Monitor",
        "category": "electronics",
        "price": 12000,
        "stock": 10,
        "brand": "Acer",
        "is_active": True
    }
]

for p in products:
    data.append(productmodal(
        id=p["id"],    
        title=p["title"],
        category=p["category"],
        price=p["price"],
        stock=p["stock"],
        brand=p["brand"]
        ))
# print(data)