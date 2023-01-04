from flask import Flask, request, jsonify, redirect
from flask_cors import CORS
from APIController import connection
from Transactions import simple_txn

# defining the flask app and setting up cors
app = Flask(__name__)
cors = CORS(app, resources={
    r"/*": {"origin": "*"}
})

# Setting up connection with algorand client
algod_client = connection.algo_conn()


# home page
@app.route('/')
def home_page():
    return redirect("https://www.evident.capital", code=302)


# 404 error handling
@app.errorhandler(404)
def page_not_found(e):
    return f"<title>Page Not Found</title><h1>404 Not Found</h1><p>{e}</p>", 404


# Payment Transaction
@app.route('/blockchain/payment', methods=['POST'])
def payment_transaction():

    try:
        # Get details of the user
        txn_details = request.get_json()
        sender = txn_details['sender_address']
        receiver = txn_details['receiver_address']
        amt = int(txn_details['amount'])
        note = txn_details['transaction_note']
    except Exception as error:
        return jsonify({'message': f'Payload Error! Key Missing: {error}'}), 500

    try:
        # pass the details to the algorand blockchain
        txn_id = simple_txn.payment(algod_client, sender, receiver, amt, note)
        return jsonify({'message': txn_id}), 200
    except Exception as error:
        return jsonify({'message': str(error)}), 400


# running the API
if __name__ == "__main__":
    app.run(debug=True, port=9000)
