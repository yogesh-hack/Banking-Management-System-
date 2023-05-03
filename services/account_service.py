from models.account import Account


# Operation in Account service
# -> create new user Account
# -> get_account if already account is created
# -> Deposit
# -> Withdraw
# -> Transfer

class AccountService:
    def __int__(self):
        self.accounts = {}  # store key-value (user_id : account_id)

    def create_account(self, user_id, initial_balance):
        account_id = len(self.accounts) + 1
        account = Account(account_id, user_id, initial_balance)
        # add account to dictionary
        self.accounts[account_id] = account
        return account_id

    def get_account(self, account_id):
        account = self.accounts.get(account_id)
        if not account:
            raise ValueError("Account is not exits...")
        return account

    def deposit(self, account_id, amount):
        curr_amount = self.accounts.get(account_id)
        curr_amount.balance += amount
        return curr_amount.balance

    def withdraw(self, account_id, amount):
        curr_amount = self.accounts.get(account_id)

        if curr_amount.balance < amount:
            raise ValueError("Insufficient Amount")
        curr_amount.balance -= amount
        return curr_amount.balance

    def transfer(self, sender_id, receiver_id, amount):
        sender = self.accounts.get(sender_id)
        receiver = self.accounts.get(receiver_id)

        if sender.balance < amount:
            raise ValueError("Insufficient Amount for transfer money")

        sender.balance -= amount
        receiver.balance += amount

        return (sender.balance, receiver.balance)
