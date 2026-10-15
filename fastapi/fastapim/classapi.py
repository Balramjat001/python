class student:
    def __init__(self,id=None,name=None,email=None,phone=None,city=None):
        self.id=id
        self.name=name
        self.email=email
        self.phone=phone
        self.city=city

    def __repr__(self):
        return f"<student(id={self.id},name={self.name},email={self.email},phone={self.phone},city={self.city})"

student_data = [
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

data=[] 

for x in student_data:
    x={
        "id":1,
        "name":"balram",
        "email":"balram@gmail.com",
        "phone":"123456",
        "city":"swm",
    }

    ss=data.append(student( id=x["id"], name=x["name"], email=x["email"], phone=x["phone"], city=x["city"] ))

    print(data)