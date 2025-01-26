from flask import Flask, request, jsonify
from models import db, User, Account, Transaction

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///prepaid.db'
db.init_app(app)

@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    # ...existing code...
    return jsonify({"message": "User registered successfully"}), 201

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    # ...existing code...
    return jsonify({"message": "User logged in successfully"}), 200

@app.route('/api/account', methods=['GET'])
def get_account():
    # ...existing code...
    return jsonify(account_data), 200

@app.route('/api/account/load', methods=['POST'])
def load_funds():
    data = request.get_json()
    # ...existing code...
    return jsonify({"message": "Funds loaded successfully"}), 200

@app.route('/api/account/transactions', methods=['GET'])
def get_transactions():
    # ...existing code...
    return jsonify(transactions), 200

@app.route('/api/transaction', methods=['POST'])
def make_transaction():
    data = request.get_json()
    # ...existing code...
    return jsonify({"message": "Transaction successful"}), 200

if __name__ == '__main__':
    app.run(debug=True)
