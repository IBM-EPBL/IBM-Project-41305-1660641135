from flask import Flask,render_template, request, redirect, url_for, session
import ibm_db
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=fbd88901-ebdb-4a4f-a32e-9822b9fb237b.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=32731;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=yys87370;PWD=J35NHAilIxej1m1d",'','')

app = Flask(__name__)

@app.route("/")
def log():
    return render_template('login.html')

@app.route('/home')
def home():
  return render_template('home.html')

@app.route('/register',methods = ['POST', 'GET'])
def register():
  if request.method == 'POST':

    name = request.form['username']
    email = request.form['email']
    phone = request.form['phone']
    age = request.form['age']
    bloodgroup = request.form['bloodgroup']
    address = request.form['place']
    password = request.form['password']
 
    sql = "SELECT * FROM register WHERE email =?"
    stmt = ibm_db.prepare(conn, sql)
    ibm_db.bind_param(stmt,1,email)
    ibm_db.execute(stmt)
    account = ibm_db.fetch_assoc(stmt)

    if account:
      return render_template('login.html', msg="You are already a member, please login using your details")
    else:
      insert_sql = "INSERT INTO register VALUES (?,?,?,?,?,?,?)"
      prep_stmt = ibm_db.prepare(conn, insert_sql)
      ibm_db.bind_param(prep_stmt, 1, name)
      ibm_db.bind_param(prep_stmt, 2, email)
      ibm_db.bind_param(prep_stmt, 3, phone)
      ibm_db.bind_param(prep_stmt, 4, age)
      ibm_db.bind_param(prep_stmt, 5, bloodgroup)
      ibm_db.bind_param(prep_stmt, 6, address)
      ibm_db.bind_param(prep_stmt, 7, password)
      ibm_db.execute(prep_stmt)
    
    return render_template('login.html', msg="Data saved successfuly..Please login using your details")

@app.route('/login',methods=['POST'])
def login():
  
    email = request.form['email']
    password = request.form['password']

    sql = "SELECT * FROM register WHERE email =? AND password=?"
    stmt = ibm_db.prepare(conn, sql)
    ibm_db.bind_param(stmt,1,email)
    ibm_db.bind_param(stmt,2,password)
    ibm_db.execute(stmt)
    account = ibm_db.fetch_assoc(stmt)
    if account:
            return render_template('home.html') 
    else:
        return render_template('login.html', msg="Login unsuccessful. Incorrect username / password !") 
