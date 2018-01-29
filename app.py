#core dependencies
import os
from flask import Flask, abort, flash, redirect, render_template, request,session, make_response, jsonify
from flask_cors import CORS
from flask_restful import Api


#models and libs
from models.CustomerModel import CustomerModel
from models.User import User
from models.Stock import Stock
from models.Products import Products
from datetime import datetime

#blueprints
from apps.sampleBlueprint import sample

# all resources
from resources.Customer import CustomerRegister, CustomerData
from resources.User import UserRegister
from resources.Products import Registerproducts
from resources.stocks import UpdateStocks
from resources.Products import getprice

app = Flask(__name__)
dbname   = 'mysql+pymysql://root:admin@127.0.0.1/2_clear'

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
    customers = CustomerModel.query.all()
    products = Products.query.all()
    session['logged_in'] = True 
    return render_template('transactions.html',products=products,customers=customers)

@app.route("/registrations")
def registrations():
    return render_template('adduser.html')

@app.route("/admin")
def admin():
    return render_template('adminpanel.html')


@app.route("/reports")
def reports():

    stocks = Stock.query.all()
    return render_template('reports.html', stocks=stocks)

@app.route("/aproduct")
def adminproduct():
    
    return render_template('adminproducts.html')

@app.route("/aadd")
def aadd(): 

    return render_template('adminadduser.html')

@app.route("/amanage")
def amanage(): 
    
    return render_template('adminaccounts.html')

@app.route("/aastock")
def astock():

    products = Products.query.all()

    return render_template('adminstockin.html', products=products)

@app.route("/products")
def products():
    stocks = Stock.query.all()
    products = Products.query.all()
    return render_template('products.html',stocks=stocks, products=products )


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
    POST_ROLE = str(request.form['role'])

    new_user = User(
        username = POST_USERNAME,
        password = POST_PASS,
        name = POST_NAME,
        role = POST_ROLE
    )
    try:
        new_user.insert()
        return render_template('adduser.html', customers=customers,users=users)
    except:
        return 'error'

@app.route('/Registerproduct', methods=['POST'])
def Registerproduct():     

    POST_PRODNAME = str(request.form['productname'])
    POST_PRODPRICE = str(request.form['sp'])
    POST_PRODQUANTITY = str(request.form['quantity'])
    POST_PRODTYPE = str(request.form['type'])
    new_product = Product(
        pname = POST_PRODNAME,
        pprice = POST_PRODPRICE,
        quantity = POST_PRODQUANTITY,
        ptype = POST_PRODTYPE
    )
    try:
        new_user.insert()
        return render_template('adminproducts.html')
    except:
        return 'error'



#api routes
api.add_resource(CustomerRegister, '/Customer/add')
api.add_resource(UserRegister, '/User/add')
api.add_resource(Registerproducts, '/Products/add')
api.add_resource(UpdateStocks, '/update/stocks')
api.add_resource(CustomerData, '/customer/<int:_id>')
api.add_resource(getprice, '/price/<int:_id>')


#register blueprints here
app.register_blueprint(sample, url_prefix='/sample')

if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(port=4000)
