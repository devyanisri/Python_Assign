li=[
    {"pid":"101","name":"hp elitebook","cost":"40000","rating":"5","discount":"30","category":"Laptop"},
    {"pid":"102","name":"wireless mouse","cost":"1000","rating":"3","discount":"10","category":"Mouse"},
    {"pid":"103","name":"macbook","cost":"10000","rating":"5","discount":"50","category":"Laptop"},
    {"pid":"104","name":"Mi note pro 6","cost":"13000","rating":"4","discount":"20","category":"Mobile"},
    {"pid":"105","name":"One plus 7 pro","cost":"57000","rating":"5","discount":"10","category":"Mobile"},
    {"pid":"106","name":"Asus zenphone max","cost":"11000","rating":"2","discount":"5","category":"Mobile"} ,
    {"pid":"107","name":"Sony headphones","cost":"800","rating":"3","discount":"10","category":"Headphones"},
    {"pid":"108","name":"Boat headphones","cost":"1500","rating":"5","discount":"50","category":"Headphones"}
]



choice= str(input())
li.sort(key=lambda el: float(el[dict[choice][0]]), reverse=dict[choice][1])

newobj = filter(lambda el: el["discount"] == "10", li)
for i in newobj:
    print("{name}:{brand}".format(**i))
newobj1 = filter(lambda el: el["rating"] == "5", li)
for j in newobj1:
    print("{name}:{brand}".format(**j))
newobj2 = filter(lambda el: el["category"] == "Headphones", li)
for f in newobj2:
    print("{name}:{brand}".format(**f))