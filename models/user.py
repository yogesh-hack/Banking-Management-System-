class User:
    def __init__(self, u_id, account_id,name, age, address, contact):
        self.u_id = u_id
        self.account_id = account_id
        self.name = name
        self.age = age
        self.address = address
        self.contact = contact

    def __str__(self):
        return f"User(id = {self.u_id}, account_id = {self.account_id}, name = {self.name}, age = {self.age}, address = {self.address}, contact = {self.contact})"
