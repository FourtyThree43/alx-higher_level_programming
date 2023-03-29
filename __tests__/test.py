class User:
    id = 89
    name = "no name"
    __password = None

    def __init__(self, new_name=None):
        self.is_new = True
        if new_name is not None:
            self.name = new_name

u = User("John")
u.name
print("Name:", u.name)
print("ID:",u.id)
print("IsName:",u.is_new)
print("___")

u = User()
u.is_new
print("Name:", u.name)
print("ID:",u.id)
print("IsName:",u.is_new)
print("___")
