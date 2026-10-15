from fastapi import FastAPI

abcd=FastAPI()

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

@abcd.delete("/deletedata")
def deletedata(id:int):
    for x in data:
        if x["id"]==id:
            data.remove(x)
            break
            return {
                "status":True,
                "message":"id not found"
            }

@abcd.put("/updatedata")
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
    
    
@abcd.get("/users")
def users():
    return data