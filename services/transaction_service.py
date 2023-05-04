from services.account_service import AccountService
from models.transaction import Transaction
import random


class TransactionServices:
    def __int__(self):
        self.transactions = []

    def deposit(self, account_id, amount):
        account = self.get_account_by_id(account_id)
        if account:
            transaction = Transaction(random.random(), "UPI", amount, account_id)
            account.balance += amount
            self.transactions.append(transaction)
            return transaction.transaction_id
        else:
            return None

    def withdraw(self, account_id, amount):
        account = self.get_account_by_id(account_id)
        if account:
            transaction = Transaction(random.random(), "Net Banking", amount, account_id)
            account.balance -= amount
            self.transactions.append(transaction)
            return transaction.transaction_id
        else:
            return None

    def get_account_by_id(self, account_id):
        account = AccountService()
        return account.get_account(account_id)

    def get_transaction_by_account_id(self, account_id):
        transactions = [t for t in self.transactions if t.account_id == account_id]
        return transactions
