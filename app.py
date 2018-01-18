#core dependencies
import os
from flask import Flask, abort, flash, redirect, render_template, request,session, make_response, jsonify
from flask_cors import CORS
from flask_restful import Api


#models and libs
from models.CustomerModel import CustomerModel
from models.User import User
from datetime import datetime
from models.Stock import Stock

#blueprints
from apps.sampleBlueprint import sample

# all resources
from resources.Customer import Customer
from resources.User import UserRegister


app = Flask(__name__)
dbname   = 'mysql+pymysql://root:@127.0.0.1/2_clear'

CORS(app, supports_credentials=True, resources={r"*": {"origins": "*"}})


app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', dbname)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.urandom(12)

api = Api(app)

@api.representation('application/json')
def output_json(data, code, headers=None):
    resp = make_response(jsonify(data), code)
    resp.headers.extend(headers or {})
    return resp


@app.route('/')
def home():
    users = User.query.all()    

    customers = CustomerModel.query.all() 
    if session.get('logged_in'):
        return render_template('home.html', customers=customers,users=users)
    else:
        return render_template('login.html', users=users,customers=customers)


    if session.get('logged_in'):
        return render_template('home.html')
    else:
        return render_template('login.html', users=users)
 
@app.route('/login', methods=['POST'])
def do_admin_login():
    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])


    query = User.query.filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]))
    result = query.first()

    if result:
        session['uid'] = result.id
        session['logged_in'] = True
        # redirect to /home
    else:
        flash('wrong password!')
        # redirect to login
    return redirect('/')

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return redirect('/')


@app.route("/transactions")
def transactions():
    session['logged_in'] = True 
    return render_template('transactions.html')

@app.route("/registrations")
def registrations():

    return render_template('adduser.html')

@app.route("/manage")
def manage():
    session['logged_in'] = True 
    return render_template('manageaccounts.html')


@app.route("/products")
def products():


    return render_template('products.html')

@app.route("/recordstockin" , methods=['POST'])
def recordstockin():

    POST_TYPE = "Stock In"
    POST_AMOUNT = request.form['tbstockin']
    POST_DATE = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    container = Stock.query.order_by(Stock.stockid.desc()).first()

    new_stockin = Stock(

        Type = POST_TYPE,
        Amount = POST_AMOUNT,
        Date = POST_DATE,

        Totalcontainers = container.Totalcontainers + int(POST_AMOUNT),
        containersonhand = container.containersonhand + int(POST_AMOUNT)
    )

    container.insert()
    new_stockin.insert()

    return render_template('adminpanel.html') 

@app.route("/recordtransact" , methods=['POST'])
def recordtransact():

    POST_TYPE = "Delivery"
    POST_AMOUNT = request.form['tbAmount']
    POST_DATE = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    container = Stock.query.order_by(Stock.stockid.desc()).first()

    new_stockin = Stock(

        Type = POST_TYPE,
        Amount = POST_AMOUNT,
        Date = POST_DATE,

        Totalcontainers = container.Totalcontainers,
        containersonhand = container.containersonhand - int(POST_AMOUNT)
    )
  
    container.insert()
    new_stockin.insert()


   # customer = Stock.query.order_by(Customer.ContainersOnHand.first()

    new_transaction = CustomerModel(
        
        ContainersOnHand = customer.containersonhand + int(POST_AMOUNT)
    )
  
    container.insert()
    new_transaction.insert()
  
    return render_template('adminpanel.html')     

@app.route("/recordstockout" , methods=['POST'])
def recordstockout():

    POST_TYPE = "Stock Out"
    POST_AMOUNT = request.form['tbstockout']
    POST_DATE = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    container = Stock.query.order_by(Stock.stockid.desc()).first()

    new_stockin = Stock(

        Type = POST_TYPE,
        Amount = POST_AMOUNT,
        Date = POST_DATE,


        Totalcontainers = container.Totalcontainers - int(POST_AMOUNT),
        containersonhand = container.containersonhand - int(POST_AMOUNT)
    )
  
    container.insert()
    new_stockin.insert()
  
    return render_template('adminpanel.html')  

@app.route("/updatestockin/<int:_id>", methods=['POST','GET'])
def updatestockin(_id):
    return _id
    POST_AMOUNT = request.form['tbstockin']
    return container.json()
    container.Totalcontainers = str(container.Totalcontainers) + POST_AMOUNT
    container.insert()

    return render_template('adminpanel.html')


@app.route("/stockout")
def stockout():
 
    return render_template('stockout.html')


@app.route("/Deliver")
def deliver():
    
    customers = CustomerModel.query.all() 
    # base_url = request.url
    return render_template('Deliver.html', customers=customers)


@app.route("/return")
def returnn():
 
    return render_template('return.html')

@app.route("/recordnewcustomer",  methods=['POST'])
def recordnewcustomer():
    users = User.query.all()

    POST_CNAME = request.form['customername']
    POST_CADDRESS = request.form['customeraddress']
    POST_CCONTACT = request.form['customercontact']

    new_customer = CustomerModel(
        name = POST_CNAME,
        address = POST_CADDRESS,
        number = POST_CCONTACT
    )
    new_customer.insert()

    customers = CustomerModel.query.all()

    return render_template('adduser.html', customers=customers,users=users)

@app.route('/recordnewuser', methods=['POST'])
def recordnewuser():     

    POST_USERNAME = str(request.form['username'])
    POST_NAME = str(request.form['user_name'])
    POST_PASS = str(request.form['password'])
    POST_CPASS = str(request.form['confirmpassword'])

    new_user = User(
        username = POST_USERNAME,
        password = POST_PASS,
        name = POST_NAME
    )
    try:
        new_user.insert()
        return render_template('adduser.html', customers=customers,users=users)
    except:
        return 'error'


#api routes
api.add_resource(Customer, '/customer/<int:_id>')
api.add_resource(UserRegister, '/User/add')


#register blueprints here
app.register_blueprint(sample, url_prefix='/sample')

if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(port=4000)