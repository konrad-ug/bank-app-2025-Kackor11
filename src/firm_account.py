from src.account import Account
import requests
import os
from datetime import datetime

class Firm_Account(Account):
    def __init__(self, company_name, nip):
        self.company_name = company_name
        self.balance = 0.00
        self.transaction_history = []
        
        if len(nip) != 10:
            self.nip = "INVALID"
        else:
            if self.verify_nip_in_gov(nip):
                self.nip = nip
            else:
                raise ValueError("Company not registered!!")
        
    def take_loan(self, amount):
        if self.balance >= amount * 2 and -1775 in self.transaction_history:
            self.balance += amount
            return True
        return False

    def verify_nip_in_gov(self, nip):
        base_url = os.environ.get("BANK_APP_MF_URL", "https://wl-test.mf.gov.pl/")
        date = datetime.now().strftime("%Y-%m-%d")
        
        full_url = f"{base_url}api/search/nip/{nip}?date={date}"
        
        print(f"Sending request to: {full_url}")
        
        try:
            response = requests.get(full_url)
            print(f"Response: {response.text}")
            
            if response.status_code == 200:
                data = response.json()
                subject = data.get("result", {}).get("subject", {})
                if subject and subject.get("statusVat") == "Czynny":
                    return True
            return False
        except requests.exceptions.RequestException:
            return False
    
    def to_dict(self):
        return {
            "type": "firm",
            "company_name": self.company_name,
            "nip": self.nip,
            "balance": self.balance,
            "transaction_history": self.transaction_history
        }