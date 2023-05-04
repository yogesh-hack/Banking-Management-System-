import csv
from models.user import User


class UserServices:
    def __init__(self, user_file_path):
        self.users = {}
        self.load_users(user_file_path)

    # def load_users(self, user_file_path):
    #     with open(user_file_path, "r") as f:
    #         reader = csv.DictReader(f)
    #         for row in reader:
    #             user_id = int(row["user_id"])
    #             account_id = int(row["account_id"])
    #             name = row["name"]
    #             age = int(row["age"])
    #             address = row["address"]
    #             contact = int(row["contact"]
    #             user = User(user_id, account_id, name, age, address, contact)
    #             self.users[user_id] = user
    def load_users(self, user_file_path):
        self.users = []
        with open(user_file_path, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                user_id = int(row.get("user_id", 0))
                account_id = int(row.get("account_id", 0))
                name = row.get("name", "")
                age = int(row.get("age", 0))
                address = row.get("address", "")
                contact = row.get("contact", "")
                user = User(user_id, account_id, name, age, address, contact)
                self.users.append(user)

    def get_user_by_id(self, user_id):
        user = self.users.get(user_id)
        if user is None:
            raise ValueError("User not found")
        return user

    def get_all_users(self):
        return list(self.users.values())

    def create_user(self, account_id, name, age, address, contact):
        user_id = max(self.users.keys()) + 1 if len(self.users) > 0 else 1
        user = User(user_id, account_id, name, age, address, contact)
        self.users[user_id] = user
        return user_id

