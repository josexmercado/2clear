import os
from flask import Flask, abort, flash, redirect, render_template, request,session
from models.Customer import Customer
from models.User import User
from datetime import datetime
from models.Stock import Stock

# all models
app = Flask(__name__)
dbname   = 'mysql+pymysql://root:admin@127.0.0.1/2clear_inventory'
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', dbname)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.urandom(12)

@app.route('/')
def home():
    users = User.query.all()    

    customers = Customer.query.all() 
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

@app.route("/reportviewer")
def reportviewer():
    customers = Customer.query.all() 
    users = User.query.all() 
    session['logged_in'] = True 
    return render_template('Reports.html', customers=customers,users=users)

@app.route("/adminpanel")
def adminpanel():

    customers = Customer.query.all() 
    users = User.query.all() 
    return render_template('adminpanel.html', customers=customers,users=users)

@app.route("/AddCustomer")
def AddCustomer():

    customers = Customer.query.all() 
    return render_template('addcustomer.html',customers=customers)

@app.route("/Adduser")
def Adduser():

    customers = Customer.query.all() 
    return render_template('adduser.html',customers=customers)


@app.route("/stockin")
def stockin():


    return render_template('stockin.html')

@app.route("/recordstockin" , methods=['POST'])
def recordstockin():

    POST_TYPE = "Stock In"
    POST_AMOUNT = request.form['tbstockin']
    POST_DATE = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    new_stockin = Stock(

        Type = POST_TYPE,
        Amount = POST_AMOUNT,
        Date = POST_DATE,
        Totalcontainers = POST_AMOUNT,

        containersonhand = container.Totalcontainers + POST_AMOUNT
    )
    new_stockin.insert()
  
    return render_template('adminpanel.html')   

@app.route("/updatestockin", methods=['POST','GET'])
def updatestockin():

    POST_AMOUNT = request.form['tbstockin']

    container = Stock.query.filter_by.first()
    container.Totalcontainers = str(container.Totalcontainers) + POST_AMOUNT
    container.insert()

    return render_template('adminpanel.html')


@app.route("/stockout")
def stockout():
 
    return render_template('stockout.html')

@app.route("/recordnewcustomer",  methods=['POST'])
def recordnewcustomer():
    users = User.query.all()

    POST_CNAME = request.form['tbName']
    POST_CADDRESS = request.form['tbAddress']
    POST_CCONTACT = request.form['tbContact']

    new_customer = Customer(
        CustomerName = POST_CNAME,
        CustomerAddress = POST_CADDRESS,
        CustomerNumber = POST_CCONTACT
    )
    new_customer.insert()

    customers = Customer.query.all()

    return render_template('adminpanel.html', customers=customers,users=users)

@app.route('/adduser', methods=['POST'])
def adduser():     

    POST_USERNAME = str(request.form['tbUser'])
    POST_NAME = str(request.form['tbName'])
    POST_ADDRESS = str(request.form['address'])
    POST_PASS = str(request.form['pass'])
    POST_CPASS = str(request.form['cpass'])

    new_user = User(
        username = POST_USERNAME,
        password = POST_PASS,
        name = POST_NAME
    )
    try:
        new_user.insert()
        return 'success'
    except:
        return 'error'

if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(port=4000)