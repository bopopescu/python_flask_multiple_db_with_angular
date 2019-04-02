from flask import Flask,render_template,redirect,url_for,request

app = Flask(__name__)

@app.route('/')
def connectindex():
 return render_template('index.html')

@app.route('/getdetails',methods=["post"])
def getdetails():
    email = request.form["email"]
    psw = request.form["psw"]
    pswrepeat = request.form["pswrepeat"]
    print("bemail"+email)
    print("bpsw"+psw)
    print("bpswrepeat"+pswrepeat)
    return "got it"

if __name__ == '__main__':
    app.run(debug=True)