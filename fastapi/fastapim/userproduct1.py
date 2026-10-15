from fastapi import FastAPI,status,Response
from userproduct import userdata,productdata,orderdata
from userproduct import productmodel,users,order

app=FastAPI()

@app.get("/readproduct")
def readproduct():
    return productdata

@app.get("/productbyid")
def productbyid(id:int,resp:Response):
    for x in productdata:
        if x.id==id:
            resp.status_code=status.HTTP_302_FOUND
            return x

    return {
        "status":False,
        "message":"product id not found"
    }

@app.post("/createproduct")
def createproduct(title,category,price,brand,stock,resp:Response,is_true:bool=True):
    productdata.append(productmodel(
    id=len(productdata)+1,
    title=title,
    category=category,
    price=price,
    brand=brand,
    stock=stock,
    is_true=is_true
    ))
    resp.status_code=status.HTTP_201_CREATED
    return{
        "status":True,
        "message":"your id has created"
    }

@app.delete("/deleteproduct")
def deleteproduct(id:int,resp:Response):
    for x in productdata:
        if x.id==id:
            productdata.remove(x)
            resp.status_code=status.HTTP_200_OK
            return{
                "status":True,
                "message":"data has deleted"
            }
    resp.status_code=status.HTTP_404_NOT_FOUND
    return {
        "status":False,
        "message":"id not found"
    }

@app.put("/updateproduct")
def updateproduct(id:int,resp:Response,title:str|None=None,category:str|None=None, price:int|None=None, brand:str|None=None,stock:int|None=None,is_true:bool=True):
    for x in productdata:
        if x.id==id:
            if title !=None:x.title=title           
            if category !=None:x.category=category
            if price !=None:x.price=price
            if brand !=None:x.brand=brand
            if stock !=None:x.stock=stock
            x.is_true=is_true
            resp.status_code=status.HTTP_200_OK
            return{
                "status":True,
                "message":f"{id} has updated"
            }
    resp.status_code=status.HTTP_404_NOT_FOUND
    return{
        "status":False,
        "message":"id not found"
    }

@app.get("/readusers")
def usersdata():
    return userdata

@app.get("/usersbyid")
def usersbyid(id:int,resp:Response):
    for x in userdata:
        if x.id==id:
            return x
    resp.status_code=status.HTTP_404_NOT_FOUND
    return{
        "status":False,
        "message":"id not found"
    }

@app.post("/createuser")
def createuser(name,email,phone,city,resp:Response):
    userdata.append(users(
        id=len(userdata)+1,
        name=name,
        email=email,
        phone=phone,
        city=city
        ))
    resp.status_code=status.HTTP_201_CREATED
    return{
        "status":True,
        "message":"your id has created"
    }

@app.delete("/deleteusers")
def deleteusers(id:int,resp:Response):
    for x in userdata:
        if x.id==id:
            userdata.remove(x)
            resp.status_code=status.HTTP_200_OK
            return{
                "status":True,
                "message":"data has deleted"
            }
    resp.status_code=status.HTTP_404_NOT_FOUND
    return {
        "status":False,
        "message":"id not found"
    }

@app.put("/updateusers")
def updateusers(id:int,resp:Response,name:str|None=None,email:str|None=None,phone:int|None=None,city:str|None=None):
    for x in userdata:
        if x.id==id:
            if name != None: x.name=name
            if email != None: x.email=email
            if phone != None: x.phone=phone
            if city != None: x.city=city
            resp.status_code=status.HTTP_200_OK
            return {
                "status":True,
                "message":f"{id} has updated"
            }
    resp.status_code=status.HTTP_404_NOT_FOUND
    return{
        "status":False,
        "message":"id not found"
    }

@app.get("/ordersdata")
def ordersdata():
    return orderdata

@app.get("/orderdatabyid")
def ordersdata(id:int,resp:Response):
    for x in orderdata:
        if x.id==id:
            return x
    resp.status_code=status.HTTP_404_NOT_FOUND
    return{
        "status":False,
        "message":"id not found"
    }

@app.get("/orderdata/paymentgetway")
def ordersdata(paymentmode:str):
    paymentgetway=[]
    for x in orderdata:
        if x.paymentmode  == paymentmode:
            paymentgetway.append(x)
    return paymentgetway