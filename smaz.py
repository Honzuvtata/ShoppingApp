

items = [
    {"itemId": "id-WAPWXFSXVO", "name": "apple", "count": 1},
    {"itemId": "id-RLS2HWA52E", "name": "banana", "count": 2},
]


def greeter(name):
    print("Hellos: ", name)

greeter("Kuba")

def doubleIt(a = 0, x=2):
    print(x*2)
    return x*x


doubleIt()
doubleIt(x=3)

x = {}
a, b ,c = "numbreList", "name", "Honza"
y = {a: {b: c}}


x[list] = y

print("print x", x)


for item in x:
    print("item: ",item)


users = {"user": {"name": "Honza"}}

print(users)
for item in users.items():
    print(item)