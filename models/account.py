# models/account.py

class Account:
    def __init__(self, a_id, user_id, balance):
        self.a_id = a_id
        self.user_id = user_id
        self.balance = balance

    def __str__(self):
        return f"Account(id={self.a_id}, user_id={self.user_id}, balance={self.balance})"
