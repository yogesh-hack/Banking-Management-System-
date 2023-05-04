# main.py
# from models.account import Account
# from models.transaction import Transaction
from models.user import User
# from services.transaction_service import TransactionServices
from services.account_service import AccountService
from services.user_service import UserServices
import csv

def main():
    # create some accounts
    # acc1 = Account(1, 8328698, 3000)
    # acc2 = Account(2, 645657, 40000)
    ram = User(1,287348,"Ram",20,"dehli",9015901148)
    #
    # # create a transaction
    # transaction1 = Transaction(67423, "NEFT", 50000, 308277537263)
    #
    # # print the objects
    # print(acc1)
    # print(acc2)
    print(ram)
    # print(transaction1)

    account_service = AccountService()

    account_service.accounts = {}

    # create some accounts
    account1_id = account_service.create_account(1, 1000)
    account2_id = account_service.create_account(2, 500)

    print("Account details initially : ")
    account1 = account_service.get_account(account1_id)
    account2 = account_service.get_account(account2_id)

    print(f"Account {account1.a_id} balance: {account1.balance}")
    print(f"Account {account2.a_id} balance: {account2.balance}")

    # deposit to an account
    account_service.deposit(account1_id, 250)

    # withdraw from an account
    account_service.withdraw(account1_id, 100)

    print("After deposit Account Details : ")
    account1 = account_service.get_account(account1_id)
    account2 = account_service.get_account(account2_id)

    print(f"Account {account1.a_id} balance: {account1.balance}")
    print(f"Account {account2.a_id} balance: {account2.balance}")

    # transfer between accounts
    account_service.transfer(account1_id, account2_id, 300)

    # print the account balances
    print("After Transfer Account Details : ")
    account1 = account_service.get_account(account1_id)
    account2 = account_service.get_account(account2_id)

    print(f"Account {account1.a_id} balance: {account1.balance}")
    print(f"Account {account2.a_id} balance: {account2.balance}")

    # transaction_service = TransactionServices()
    # transaction_service.transactions = []
    #
    # transaction1_id = transaction_service.deposit(account1_id, 500)
    # transaction2_id = transaction_service.withdraw(account1_id, 250)
    # transaction3_id = transaction_service.deposit(account2_id, 100)
    #
    # transactions = transaction_service.get_transaction_by_account_id(account1_id)
    # for transaction in transactions:
    #     print(transaction)

    user_service = UserServices('data/user.csv')
    user_service.users = {}

    # create a new user
    user_id = user_service.create_user(165762,"joe",20,"toronto",5578768717)
    print("User created with ID:", user_id)

    user_id = user_service.create_user(7634, "peach", 26, "america", 2375646634)
    print("User created with ID:", user_id)

    # get all users
    all_users = user_service.get_all_users()
    print("All users:")
    # print(all_users)
    for user in all_users:
        print(user)


if __name__ == '__main__':
    main()
    # with open('data/user.csv', newline='') as csvfile:
    #     reader = csv.reader(csvfile)
    #     for row in reader:
    #         print(row[0])
