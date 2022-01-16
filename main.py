from flask import Flask, render_template, request
import db

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/account_data", methods=["POST"])
def get_data():
    account_no = request.form["account_number"]
    account_name = request.form["account_name"]
    account_balance = request.form["account_balance"]
    account_pin = request.form["account_pin"]
    
    if db.insert_data(account_no,account_name,account_balance,account_pin):
        return "Success"
    else:
        return "Exception- contact developer"
    
@app.route("/check_account_details")
def check_account_details():
    return render_template('details.html')

@app.route("/show_account_details", methods=["POST"])
def show_account_details():
    account_no = request.form["account_number"]
    account_pin = request.form["account_pin"]
    
    pin_account = db.get_pin(account_no)
    pin = pin_account[1]
    
    details = db.get_account(account_no)
    
    if pin == int(account_pin):
        return render_template("accounts.html",data=details)
    else:
        return "invalid pin"


@app.route("/check_account_balance")
def check_account_balance():
    return render_template('balance.html')

@app.route("/show_balance", methods=["POST"])
def show_balance():
    account_no = request.form["account_number"]
    account_pin = request.form["account_pin"]
    
    balance = db.get_pin(account_no)
    
    bal = balance[0]
    pin = balance[1]
    
    if pin == int(account_pin):
        return "account balance is {}".format(bal)
    else:
        return "invalid pin"
        

@app.route("/Transfer_amount")   
def Transfer_amount():
    return render_template("transfer.html")   


@app.route("/transfer_balance", methods=["POST"])
def get_transfer():
    account_no = request.form["account_number"]
    account_pin = request.form["account_pin"]
    other_acc_no = request.form["other_account_number"]
    amount = request.form["transfer"]
    
    transfer = db.get_account(account_no)
    number = transfer[0]
    name = transfer[1]
    balance = transfer[2]
    pin = transfer[3]
    
    other_account = db.get_account(other_acc_no)
    other_balance = other_account[2]
    
    if pin == int(account_pin):
        if float(amount) <= balance: 
            balance -= float(amount)
            other_balance += float(amount)
            db.update_balance(account_no, balance)
            db.update_balance(other_acc_no, other_balance)
            return "Transferred amount - {} from account number - {} to account number - {}." .format(amount,account_no,other_acc_no)
        else:
            return "Insufficient account balance"
    else:
        return "Invalid pin"
    
        
app.run()
