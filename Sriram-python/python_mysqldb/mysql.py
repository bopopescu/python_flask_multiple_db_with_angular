from flask import Flask,render_template,redirect,url_for,request
app = Flask(__name__)

@app.route('/')
def connected():
 return render_template('index.html')

@app.route('/getdetails',methods =['get','post'] )
def getdetails():
  username = request.form["email"]
  psw = request.form["psw"]
  pswrepeat = request.form["psw-repeat"]
  print("buser"+username)
  print("bpsw"+psw)
  print("bpswr"+pswrepeat)
  return "got it"


if __name__ == '__main__':
  app.run(debug=True)