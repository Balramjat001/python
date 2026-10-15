from fastapi import FastAPI

crud=FastAPI()

data = [
    {
        "id": 1,
        "name": "Aarav Sharma",
        "email": "aarav@gmail.com",
        "phone": "9876543210",
        "city": "Jaipur"
    },
    {
        "id": 2,
        "name": "Priya Verma",
        "email": "priya@gmail.com",
        "phone": "9876543211",
        "city": "Delhi"
    },
    {
        "id": 3,
        "name": "Rahul Singh",
        "email": "rahul@gmail.com",
        "phone": "9876543212",
        "city": "Jodhpur"
    },
    {
        "id": 4,
        "name": "Sneha Gupta",
        "email": "sneha@gmail.com",
        "phone": "9876543213",
        "city": "Mumbai"
    },
    {
        "id": 5,
        "name": "Vikas Kumar",
        "email": "vikas@gmail.com",
        "phone": "9876543214",
        "city": "Lucknow"
    },
    {
        "id": 6,
        "name": "Anjali Meena",
        "email": "anjali@gmail.com",
        "phone": "9876543215",
        "city": "Ajmer"
    },
    {
        "id": 7,
        "name": "Rohit Yadav",
        "email": "rohit@gmail.com",
        "phone": "9876543216",
        "city": "Gurugram"
    },
    {
        "id": 8,
        "name": "Neha Jain",
        "email": "neha@gmail.com",
        "phone": "9876543217",
        "city": "Indore"
    },
    {
        "id": 9,
        "name": "Amit Sharma",
        "email": "amit@gmail.com",
        "phone": "9876543218",
        "city": "Kota"
    },
    {
        "id": 10,
        "name": "Pooja Singh",
        "email": "pooja@gmail.com",
        "phone": "9876543219",
        "city": "Bhopal"
    },
    {
        "id": 11,
        "name": "Karan Patel",
        "email": "karan@gmail.com",
        "phone": "9876543220",
        "city": "Ahmedabad"
    },
    {
        "id": 12,
        "name": "Simran Kaur",
        "email": "simran@gmail.com",
        "phone": "9876543221",
        "city": "Chandigarh"
    },
    {
        "id": 13,
        "name": "Deepak Joshi",
        "email": "deepak@gmail.com",
        "phone": "9876543222",
        "city": "Udaipur"
    },
    {
        "id": 14,
        "name": "Riya Agarwal",
        "email": "riya@gmail.com",
        "phone": "9876543223",
        "city": "Agra"
    },
    {
        "id": 15,
        "name": "Manish Gupta",
        "email": "manish@gmail.com",
        "phone": "9876543224",
        "city": "Kanpur"
    },
    {
        "id": 16,
        "name": "Kavita Sharma",
        "email": "kavita@gmail.com",
        "phone": "9876543225",
        "city": "Pune"
    },
    {
        "id": 17,
        "name": "Suresh Meena",
        "email": "suresh@gmail.com",
        "phone": "9876543226",
        "city": "Bikaner"
    },
    {
        "id": 18,
        "name": "Tanya Verma",
        "email": "tanya@gmail.com",
        "phone": "9876543227",
        "city": "Noida"
    },
    {
        "id": 19,
        "name": "Mohit Choudhary",
        "email": "mohit@gmail.com",
        "phone": "9876543228",
        "city": "Alwar"
    },
    {
        "id": 20,
        "name": "Nisha Kumari",
        "email": "nisha@gmail.com",
        "phone": "9876543229",
        "city": "Patna"
    }
]

@crud.get("/users")
def users():
    return data

@crud.get("/createusers")
def createusers(name,email,phone,city):
    data.append({
        "id":len(data)+1,
        "name":name,
        "email":email,
        "phone":phone,
        "city":city
    })
    return {
        "status":True,
        "message":"new user has created"
    }

@crud.delete("/deletedata")
def deletedata(id:int):
    for x in data:
        if x["id"]==id:
            data.remove(x)
            return {
                "status":True,
                "message":"data has deleted"
            }
    return {
        "status":False,
        "message":"id not found"
    }

@crud.put("/updatedata")
def updatedata(id:int,name="",email="",phone="",city=""):
    for x in data:
        if x["id"]==id:
            if name:x["name"]=name
            if email:x["email"]=email
            if phone:x["phone"]=phone
            if city:x["city"]=city
            return {
                "Status":True,
                "message":"data has updated"
            }
    return {
        "status":False,
        "message":"Data not found"
    }
