from flask import Flask,request,url_for,redirect,render_template,jsonify
from pymongo import MongoClient
from flask_cors import CORS,cross_origin
import json
app = Flask(__name__)

client = MongoClient()
client = MongoClient('mongodb://localhost:27017')
db = client.auth
posts = db.users

cors = CORS(app)
@app.after_request
def add_headers(response):
  response.headers.add('Content-Type', 'application/json')
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Methods', 'PUT, GET, POST, DELETE, OPTIONS')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Expose-Headers', 'Content-Type,Content-Length,Authorization,X-Pagination')
  return response

@app.route('/',methods =['get'])
def general():
    return "connected"

@app.route('/login',methods=['get','post'])
def login():
  try:
      reqdata = request.json
      username = reqdata['username']  
      password = reqdata['password']
      print("requesting data",username,password)    
      resultfindone = posts.find_one({"username":username,"password":password})
      print(resultfindone)  
      print(resultfindone['username'])  
      if resultfindone['username'] == username and resultfindone['password'] == password :
         return "<h1>User Authendicated</h1>" 
  except:    
         return "<h1>Not Authendicated</h1>"


@app.route('/createuser',methods=['post'])
def createuser():
  try:
      reqdata = request.json
      cusername = reqdata['username']  
      cpassword = reqdata['password']
      resultfindone = posts.find_one({"username":cusername,"password":cpassword})      
      if resultfindone['username'] == cusername and resultfindone['password'] == cpassword :
         return "<h1>User Authendicated Already</h1>" 
  except:    
         
         resultinsertone = posts.insert_one({"username":cusername,"password":cpassword})        
         return "<h1>User Created successfully</h1>"



if __name__ == '__main__':
  app.run(debug=True)