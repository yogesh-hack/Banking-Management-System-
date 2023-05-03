# main.py
from models.account import Account
from models.transaction import Transaction
from models.user import User
from services.account_service import AccountService


def main():
    # create some accounts
    # acc1 = Account(1, 8328698, 3000)
    # acc2 = Account(2, 645657, 40000)
    # ram = User(1,"Ram",20,"dehli",9015901148)
    #
    # # create a transaction
    # transaction1 = Transaction(67423, "NEFT", 50000, 308277537263)
    #
    # # print the objects
    # print(acc1)
    # print(acc2)
    # print(ram)
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


if __name__ == '__main__':
    main()
