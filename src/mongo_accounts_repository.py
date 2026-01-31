from pymongo import MongoClient
from src.customer_account import Customer_Account
from src.firm_account import Firm_Account
import os

class MongoAccountsRepository:
    def __init__(self):
        host = os.environ.get("MONGO_HOST", "localhost")
        self.client = MongoClient(f'mongodb://{host}:27017/')
        self.db = self.client['bank_db']
        self.collection = self.db['accounts']

    def save_all(self, accounts):
        self.collection.delete_many({})
        
        for account in accounts:
            if hasattr(account, "pesel"):
                ident = account.pesel
                key = "pesel"
            else:
                ident = account.nip
                key = "nip"

            self.collection.update_one(
                {key: ident},
                {"$set": account.to_dict()},
                upsert=True
            )

    def load_all(self):
        accounts = []
        for doc in self.collection.find():
            if doc.get("type") == "customer":
                acc = Customer_Account(doc["name"], doc["surname"], doc["pesel"], promo_code=None)
                acc.balance = doc["balance"]
                acc.transaction_history = doc["transaction_history"]
                accounts.append(acc)
                
            elif doc.get("type") == "firm":
                acc = Firm_Account.__new__(Firm_Account)
                acc.company_name = doc["company_name"]
                acc.nip = doc["nip"]
                acc.balance = doc["balance"]
                acc.transaction_history = doc["transaction_history"]
                accounts.append(acc)
                
        return accounts