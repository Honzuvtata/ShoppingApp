myList = [1, 2, 3]

x = []

y = [x.append(item + 1) for item in myList]
print(x)

users = [
    {"name": "Honza", "email": "honza@email.com"},
    {"name": "Kuba", "email": "kuba@email.com"},
]

print(users)

name = "Kuba"
z = [name == user["name"] for user in users]
print(z)


b = "b"
a = {}
a[b] = {}
print(a)
