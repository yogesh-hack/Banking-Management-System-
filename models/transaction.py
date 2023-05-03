import datetime


class Transaction:
    def __init__(self, transaction_id, transaction_type, amount, account):
        self.transaction_id = transaction_id
        self.transaction_type = transaction_type
        self.amount = amount
        self.date = datetime.datetime.now()
        self.account = account

    def __str__(self):
        return f"Transaction(transaction_id = {self.transaction_id}, transaction_type = {self.transaction_type}, amount = {self.amount}, account = {self.account})"
