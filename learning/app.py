from flask import Flask,render_template,url_for,request
app=Flask(__name__)

@app.route('/')
def hello():
    print("sairamamama")
    return render_template('123.html')

@app.route('/result')
def hello1():
    return render_template('index.html')
@app.route('/in',methods=['POST'])
def result():
    print(request.form['Physics'])
    return "sucesss"

if __name__ == '__main__':

   app.run(debug=True)