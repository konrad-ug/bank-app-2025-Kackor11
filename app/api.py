from flask import Flask, request, jsonify
from src.account_registry import Account_Registry
from src.customer_account import Customer_Account

app = Flask(__name__)
registry = Account_Registry()

@app.route("/api/accounts", methods=['POST'])
def create_account():
    data = request.get_json()
    print(f"Request data: {data}")
    
    new_account = Customer_Account(
        data["name"],
        data["surname"],
        data["pesel"],
        data.get("promo_code", None)
    )
    
    registry.add_account(new_account)
    
    return jsonify({"message": "Account created", "pesel": new_account.pesel}), 201


@app.route("/api/accounts", methods=['GET'])
def get_all_accounts():
    print("Get all accounts request received")
    accounts = registry.return_all_accounts()

    accounts_data=[
        {
            "name": acc.first_name, 
            "surname": acc.last_name, 
            "pesel": acc.pesel, 
            "balance": acc.balance
        }
        for acc in accounts
    ]
    
    return jsonify(accounts_data), 200


@app.route("/api/accounts/<pesel>", methods=['GET'])
def get_account_by_pesel(pesel):
    account = registry.search_by_pesel(pesel)
    
    if account:
        return jsonify({
            "name": account.first_name,
            "surname": account.last_name,
            "pesel": account.pesel,
            "balance": account.balance
        }), 200
    else:
        return jsonify({"message": "Account not found"}), 404
    
    
@app.route("/api/accounts/count", methods=['GET'])
def get_accounts_count():
    count = registry.return_registry_length()
    return jsonify({"count": count}), 200


@app.route("/api/accounts/<pesel>", methods=['PATCH'])
def update_account(pesel):
    account = registry.search_by_pesel(pesel)
    
    if not account:
        return jsonify({"message": "Account not found"}), 404
    
    data = request.get_json()
    
    if "name" in data:
        account.first_name = data["name"]
    
    if "surname" in data:
        account.last_name = data["surname"]
        
    return jsonify({"message": "Account updated"}), 200
    

@app.route("/api/accounts/<pesel>", methods=['DELETE'])
def delete_account(pesel):
    account = registry.search_by_pesel(pesel)
    
    if not account:
        return jsonify({"message": "Account not found"}), 404
    
    registry.accounts.remove(account)
    
    return jsonify({"message": "Account deleted"}), 200

