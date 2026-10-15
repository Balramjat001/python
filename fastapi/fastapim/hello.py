from fastapi import FastAPI

abc=FastAPI()

data=[
        {
            "id": 1,
            "name": "Aarav Sharma",
            "email": "aarav.sharma@student.in",
            "phone": "+91 98765 43210",
            "city": "New Delhi",
            "state": "Delhi"
        },
        {
            "id": 2,
            "name": "Priya Patel",
            "email": "priya.patel@student.in",
            "phone": "+91 98234 56781",
            "city": "Ahmedabad",
            "state": "Gujarat"
        },
        {
            "id": 3,
            "name": "Rohan Mehta",
            "email": "rohan.mehta@student.in",
            "phone": "+91 97654 32109",
            "city": "Mumbai",
            "state": "Maharashtra"
        },
        {
            "id": 4,
            "name": "Ananya Iyer",
            "email": "ananya.iyer@student.in",
            "phone": "+91 98456 78901",
            "city": "Chennai",
            "state": "Tamil Nadu"
        },
        {
            "id": 5,
            "name": "Vikram Singh",
            "email": "vikram.singh@student.in",
            "phone": "+91 98123 45670",
            "city": "Jaipur",
            "state": "Rajasthan"
        },
        {
            "id": 6,
            "name": "Sneha Reddy",
            "email": "sneha.reddy@student.in",
            "phone": "+91 99087 65432",
            "city": "Hyderabad",
            "state": "Telangana"
        },
        {
            "id": 7,
            "name": "Arjun Nair",
            "email": "arjun.nair@student.in",
            "phone": "+91 97432 10987",
            "city": "Kochi",
            "state": "Kerala"
        },
        {
            "id": 8,
            "name": "Kavya Desai",
            "email": "kavya.desai@student.in",
            "phone": "+91 98321 09876",
            "city": "Pune",
            "state": "Maharashtra"
        },
        {
            "id": 9,
            "name": "Rahul Gupta",
            "email": "rahul.gupta@student.in",
            "phone": "+91 96543 21098",
            "city": "Lucknow",
            "state": "Uttar Pradesh"
        },
        {
            "id": 10,
            "name": "Ishita Banerjee",
            "email": "ishita.banerjee@student.in",
            "phone": "+91 93321 87654",
            "city": "Kolkata",
            "state": "West Bengal"
        }
    ]

# for x in data:
#     print(x["name"])

# # print(data[-1]["name"])

# @abc.get("/")
# def test():
#     return("hello")

# @abc.get("/about")
# def test():
#     return("about")

# @abc.get("/support")
# def test():
#     return{"data":"support"}

# @abc.get("/get_student")
# def allstudent():
#     return data

# @abc.get("/namedata")
# def student_name():
#     counter=[]
#     for x in data:
#         counter.append(x["name"]) 
#     return counter

# # @abc.get("/{key}")
# # def filter(key):
# #     counter=[]    
# #     for x in data:
# #         counter.append(x[key])
# #     return counter
    
# @abc.get("/{main}")
# def filter(main):
#     return (main)

# @abc.get("/{main:path}")                         #(normal dynamic routing m / nhi lag skta lekin path btake / ka use kr skte h)
# def filter(main):
#     return (main)

# @abc.get("/{name}/{city}")                #(kitne bhi dynamic variable pass kr skte h / se seprate kr ke)
# def about(name,city):
#     return {f"{name} welcome in {city}"}

# @abc.get("/get_by_id/{id}")
# def get_student_by_id(id):
#     for x in data:
#         id=int(id)
#         if x["id"]==id:
#             return x
#     return {
#         "status":False,
#         "message":"id not found"
#     }


# @abc.get("/get_by_id/{id:int}")
# def get_student_by_id(id):
#     for x in data:
#         if x["id"]==id:
#             return x
#     return {
#         "status":False,
#         "message":"id not found"
#     }

# @abc.get("/createusers")
# def createusers(name, email, phone, city, state):
#     data.append({
#         "id":len(data)+1,
#         "name":name,
#         "email":email,
#         "phone":phone,
#         "city":city,
#         "state":state
#     })
#     return {
#         "status":True,
#         "message":"add your data"
#     }

# @abc.get("/showdata")
# def showdata():
#     return data

# @abc.delete("/deletedata/{id}")
# def deletedata(id:int):
#     for x in data:
#         if x["id"]==id:
#             data.remove(x)
#             break
#         return{
#             "status":False,
#             "message":"data not found"
#         }


# @abc.get("/showdata")
# def showdata():
#     return data

# @abc.delete("/deletedata")
# def deletedata(id:int):
#     for x in data:
#         if x["id"]==id:
#             data.remove(x)
#             break
#         return{
#             "status":False,
#             "message":"data not found"
#         }


# @abc.get("/showdata")
# def showdata():
#     return data


@abc.get("/updatedata")
def updatedata(
    id: int,
    name: str = None,
    email: str = None,
    phone: str = None,
    city: str = None,
    state: str = None
):
    for x in data:
        if x["id"] == id:
            if name is not None:
                x["name"] = name
            if email is not None:
                x["email"] = email
            if phone is not None:
                x["phone"] = phone
            if city is not None:
                x["city"] = city
            if state is not None:
                x["state"] = state

            return {
                "status": True,
                "message": f"{id} has been updated",
                "data": x
            }

    return {
        "status": False,
        "message": f"{id} not found"
    }

@abc.get("/showdata")
def showdata():
    return data

