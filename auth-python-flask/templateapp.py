from flask import Flask,request,url_for,redirect,render_template
app = Flask(__name__)
from pymongo import MongoClient
client = MongoClient()
client = MongoClient('mongodb://localhost:27017')
db = client.auth
posts = db.users

@app.route('/')
def general():
    return render_template('index.html')

@app.route('/login',methods=['get','post'])
def login():
 try:   
  name = request.form['um']
  password = request.form['ps']
  print(name,password)
  resultfindone = posts.find_one({"username":name,"password":password})
  print('One select: {0}'.format(resultfindone))
  print('One select: {0}'.format(resultfindone['username']))
  if resultfindone['username'] == name and resultfindone['password'] == password :
      return "<h1>User Authendicated</h1>"
 except:
     return "<h1>Not Authendicated</h1>"
 

@app.route('/createuser',methods=['post'])
def createuser():
 cname = request.form['cum']
 cpassword = request.form['cps']
 createuser = {
   'username':cname,
   'password':cpassword
 }
 print(createuser)
 resultinsert = posts.insert_one(createuser)
 print('User created: {0}'.format(resultinsert.inserted_id))
 return "createuser"


if __name__ == '__main__':
  app.run(debug=True)