from flask import Flask,redirect,url_for,render_template,request
import jwt
# import request as request
# from flask_jwt import JWT, jwt_required, current_identity
import flask_sijax  as simpleajax
import sqlite3 as sql
app = Flask(__name__)
# app.config['SECRET_KEY'] = 'super-secret'
@app.route('/createtable/<tablename>')
def createtable(tablename):
    conn = sql.connect('database.db')
    print("Opened database successfully")

    conn.execute('CREATE TABLE '+tablename+' (name TEXT, addr TEXT, city TEXT, pin TEXT)')
    print("Table created successfully")
    conn.close()
    return "Table created successfully"

@app.route('/list')
def list1():
   con = sql.connect("database.db")
   con.row_factory = sql.Row   
   cur = con.cursor()
   cur.execute("select * from students")   
   rows = cur.fetchall(); 
   print(str(rows))
   return str(rows)
#    return render_template("list.html",rows = rows)

@app.route('/jwt')
def myjwt(username,password):
  print("myother page username"+username)
  print("myother page password"+password)
  a = {
       "username":username,
       "password":password
      }
  encoded_jwt = jwt.encode(a, 'srirampassword')
  print(encoded_jwt)
  try:
      decoded_jwt = jwt.decode(encoded_jwt, 'srirampassword')
      print(str(decoded_jwt))
  except:
           return "Error on jwt password matching"      
  finally:          
           return '<html><body><div style="align:rigth; margin-left:10%"><p><br><span style="font-size:14pt;color:red"><b>Your JWT DECODED</b></span></b>&nbsp;&nbsp;&nbsp;:'+str(decoded_jwt)+'<br><span style="font-size:14pt;color:#0078d7 !important"><b>Your JWT ECODECD</b></span>&nbsp;&nbsp;&nbsp;:'+str(encoded_jwt)+'</p></div></body></html>'         
     #   encoded_jwt = jwt.encode({'name': 'payload'}, 'srirampassword', algorithm='HS256')
#   print(encoded_jwt)
#   decoded_jwt = jwt.decode(encoded_jwt, 'srirampassword', algorithms=['HS256'])
#   print(str(decoded_jwt))

#     return('<html><body><h1>Your JWT Token:'+str(encoded_jwt)+'</h1></br></body></html>')
#   return str(decoded_jwt)

@app.route('/')
def firstroute():
#  return 'success'
 return render_template('index.html')

@simpleajax.route(app,'/myajax')
def myajax():
    def myajax(obj_response):
        obj_response.alert("hi there")

@app.route('/show',methods = ['get','post'])
def show():
    email = request.form['email']
    pwd = request.form['pwd']
    a = {
       "username":email,
       "password":pwd
      }
    encoded_jwt = jwt.encode(a, 'srirampassword')
#      print(encoded_jwt)
    try:
       decoded_jwt = jwt.decode(encoded_jwt, 'srirampassword312')
       print(str(decoded_jwt))
    except:
        return "Error on jwt password matching"      
    finally:          
       return '<html><body><div style="align:rigth; margin-left:10%"><p><br><span style="font-size:14pt;color:red"><b>Your JWT DECODED</b></span></b>&nbsp;&nbsp;&nbsp;:'+str(decoded_jwt)+'<br><span style="font-size:14pt;color:#0078d7 !important"><b>Your JWT ECODECD</b></span>&nbsp;&nbsp;&nbsp;:'+str(encoded_jwt)+'</p></div></body></html>'         
#     a = email +pwd
#     print(email+" "+pwd)
#     myjwt( email, pwd)
#     return redirect(url_for('myjwt',data =a))

#     redirect(url_for('myjwt',username=email,password=pwd))
#     return "sucess"
# @app.route("/",)
# def index():
#     return("<html>....Ha`i...</html>")

@app.route("/hello/")
def hello():
    return("<html>....Hai...</html>")

@app.route("/onearg/<firstname>")
def arg(firstname):
    return 'hello hey you %s hai' % firstname

@app.route('/secarg/<int:num>')
def secarg(num):
    return "your int value is %d" % num

@app.route('/thirdarg/<float:dec>')
def thirdarg(dec):
    return "your float value is %f" % dec
    
@app.route('/admin/<username>')    
def admin(username):
    return "Hello_admin %s" % username

@app.route('/guest')    
def guest():
    return "Hello_guest"

@app.route('/user/<username>')    
def selectuser(username):
    if username =="admin":
        return redirect(url_for('admin',username = username))
    else :
        return redirect(url_for('guest'))

if __name__ == '__main__':
 app.run(debug=True)
