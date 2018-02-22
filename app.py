#core dependencies
import os
from flask import Flask, abort, flash, redirect, render_template, request,session, make_response, jsonify
from flask_cors import CORS
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import update

#models and libs
from models.CustomerModel import CustomerModel
from models.User import User
from models.Stock import Stock
from models.Products import Products
from datetime import datetime
from models.Orders import Orders
from models.Orderlist import Orderlist
from models.Sales import Sales

#blueprints
from apps.sampleBlueprint import sample

# all resources
from resources.Customer import CustomerRegister, CustomerData
from resources.User import UserRegister,UpdateUser
from resources.User import getname,DeleteUser
from resources.Products import Registerproducts
from resources.Products import UpdateProduct
from resources.stocks import UpdateStocks
from resources.stocks import getBydate
from resources.stocks import getBydatex
from resources.Products import getproduct
from resources.Products import getproductname
from resources.Products import UpdateQuantity
from resources.Products import UpdatexQuantity
from resources.Products import deleteproduct
from resources.Orders import registerorder
from resources.Orders import recordorderlist
from resources.Orderlist import getorderlist
from resources.Sales import recordsales
from resources.Orders import salescustomer
from resources.Orders import approveorder
from resources.Orders import orderid
from resources.Products import deliverproduct




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
        session['username'] = result.username
        session['name'] = result.name
        session['role'] =result.role
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

@app.route("/viewcustomers")
def viewcustomers():
    customers = CustomerModel.query.all()
    products = Products.query.all()
    session['logged_in'] = True 
    return render_template('viewcustomers.html',products=products,customers=customers)

@app.route("/registrations")
def registrations():
    return render_template('adduser.html')

@app.route("/admin")
def admin():
 
    return render_template('adminpanel.html')
    

@app.route("/vieworders")
def vieworders():

    orders = Orders.query.all()
    orderlist = Orderlist.query.all()
    return render_template('Orders.html' , orders=orders , orderlist=orderlist)

@app.route("/reports")
def reports():
    stocks= Stock.query.all()
    return render_template('reports.html',stocks=stocks)

@app.route("/reportsout")
def reportsout():
    stocks= Stock.query.all()
    return render_template('reports2.html',stocks=stocks)
   
@app.route("/process",methods=['POST','GET'])
def process():
    sdate = request.form['dateval']
    stocks= Stock.query.all()
    stockings= Stock.query.filter_by(date=sdate)

    return render_template('reports.html',stocks=stocks,stockings=stockings)

#@app.route("/getdata" ,methods=['GET'])
#def getdata():
#    dateval = str(request.form['sdate'])
#    stockings= Stock.query.filter(Stock.date.where(Stock.date==dateval))
#    return render_template('reports.html',stockings=stockings)

#@app.route("/search_by_date")
#def search_by_date():
#    datediss = Stock.query.filter_by(date=valuedate)
#    return datediss
    
     # return render_template('reports.html', filteredstocks=filteredstocks)

@app.route("/aproduct" , methods = ['POST', 'GET','PUT','DELETE'])
def adminproduct():
    products = Products.query.all()
    
    return render_template('adminproducts.html',products=products)

@app.route("/aadd")
def aadd(): 

    return render_template('adminadduser.html')

@app.route("/amanage")
def amanage(): 
    users = User.query.all()
    return render_template('adminaccounts.html', users=users)

@app.route("/aastock")
def astock():
    products = Products.query.all()
    
    return render_template('adminstockin.html', products=products)


#@app.route("/aastock/<int:_id>", methods=['POST','GET'])
#def aastock(_product):
#    return _product
#    POST_AMOUNT = request.form['amount']
#    return products.json()
#    products.quantity = str(products.quantity) + POST_AMOUNT
#    products.insert()
#    return render_template('reports.html')

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

#@app.route("/updateproducts/<int:_id>", methods=['POST','GET'])
#def updateproducts(_id):
#    prrd = Products.id.query.first()
#    prrd2 = Products.ptype.query.first()
#    prrd3 = Products.pprice.query.first()
#    prrd4 = Products.quantity.query.first()
#    POST_ID = request.form['prid']
#    POST_TYPE = request.form['vtype']
#    POST_PRICE = request.form['vprice']
#    POST_QUANTITY = request.form['vquantity']
#    prrd2.ptype = str(prrd2.ptype) + POST_TYPE
#    prrd3.pprice = str(prrd3.pprice) + POST_PRICE
#    prrd4.quantity = str(prrd4.quantity) + POST_QUANTITY
#    prrd.insert()

#    return render_template('home.html')

@app.route('/Registerproduct', methods=['POST'])
def Registerproduct():     

    POST_PRODNAME = str(request.form['productname'])
    POST_PRODPRICE = str(request.form['sp'])
    POST_PRODQUANTITY = str(request.form['quantity'])
    POST_PRODTYPE = str(request.form['type'])
    new_product = Products(
        pname = POST_PRODNAME,
        pprice = POST_PRODPRICE,
        quantity = POST_PRODQUANTITY,
        ptype = POST_PRODTYPE
    )
    try:
        new_product.insert()
        return render_template('adminproducts.html')
    except:
        return 'error'

#api routes
api.add_resource(CustomerRegister, '/Customer/add')
api.add_resource(UserRegister, '/User/add')
api.add_resource(UpdateUser, '/User/update')
api.add_resource(DeleteUser, '/User/delete')
api.add_resource(getname, '/user/<int:_id>')
api.add_resource(Registerproducts, '/Products/add')
api.add_resource(UpdateProduct, '/products/update')
api.add_resource(UpdateStocks, '/update/stocks')
api.add_resource(CustomerData, '/customer/<int:_id>')
api.add_resource(getproduct, '/product/<int:_id>')
api.add_resource(getproductname, '/product/<string:_name>')
api.add_resource(deleteproduct, '/deleteproduct')
api.add_resource(getorderlist, '/orderid/<int:_id>')
api.add_resource(registerorder, '/registerorder')
api.add_resource(recordorderlist, '/recordorderlist')
api.add_resource(getBydate,'/dateid/<string:_date>')
api.add_resource(getBydatex,'/dateidx/<string:_date>')

api.add_resource(recordsales,'/recordsales')
api.add_resource(salescustomer,'/salescustomer/<int:_id>')
api.add_resource(UpdateQuantity, '/update/quantity')
api.add_resource(UpdatexQuantity, '/update/xquantity')
api.add_resource(approveorder,'/approveorder')
api.add_resource(orderid,'/getorderid/<int:_orderid>')
api.add_resource(deliverproduct,'/deliverproduct')


#register blueprints here
app.register_blueprint(sample, url_prefix='/sample')

if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(port=4000)
