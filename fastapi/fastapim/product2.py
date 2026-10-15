from fastapi import FastAPI,status,Response
from product import data

app=FastAPI()

@app.get("/")
def home():
    return "this is home page"

@app.get("/users")
def products():
    return data

@app.get("/users_by_id")
def users(id:int):
    for x in data:
        if x.id==id:
            return x
    return{
        "status":False,
        "message":"id was not found"
    }

@app.post("/createdata")
def create_data(title,category,price,stock,brand,response:Response,is_active:bool=True):
    data.append({
        "id":len(data)+1,
        "title":title,
        "category":category,
        "price":price,
        "stock":stock,
        "brand":brand,
        "is_active":is_active
    })
    response.status_code=status.HTTP_201_CREATED
    return{
        "status":True,
        "message":"data created successful"
    }

@app.delete("/deletedata")
def deletedata(id:int):
    for x in data:
        if x.id==id:
            data.remove(x)
            return{
                "status":True,
                "message":"id has removed"
            }

    return{
        "status":False,
        "message":"id was not found"
    }

@app.put("/update_data")
def update_data(id:int,response:Response,title="",category="",price:int|None=None,stock:int|None=None,brand="",is_active:bool=True):
    for x in data:
        if x.id==id:
            if title:x.title=title
            if category:x.category=category
            if price!=None:x.price=price
            if stock!=None:x.stock=stock
            if brand:x.brand=brand
            x.is_active=is_active
            return{
                "status":True,
                "message":"data has updated"
            }
    response.status_code=status.HTTP_404_NOT_FOUND
    return {
        "status":False,
        "message":"id not found"
    }