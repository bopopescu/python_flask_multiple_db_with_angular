from flask import Flask,flash,redirect,url_for,request,render_template,abort
import requests as req
import json as json

app = Flask(__name__)

@app.route('/')
def hello_world():    
    return render_template('login.html')

@app.route('/regint/<int:regint>')
def regint(regint):    
   # return "hai"
    return render_template('registration.html',regint = regint)
    


@app.route('/register/<registerpara>')
def register(registerpara):    
    return render_template('registration.html',user = registerpara)


@app.route('/ram')
def sri():
    return 'hai123'

@app.route('/hello/<sriram>')
def hello_name(sriram):      
   return 'Hello hello %s!'%sriram

@app.route('/sucess/<name>')
def sucess(name):
   return 'welcome sucess %s' % name         

# @app.route('/result')
# def result():
#    dict = {'phy':50,'che':60,'maths':70}
#    return render_template('result.html',result = dict)

@app.route('/result')
def result():
   dict1 = {'phy':50,'che':60,'maths':70}
   
   return render_template('result.html', result = dict1)

@app.route('/cookie')
def index():
   return render_template('index.html') 

@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
   if request.method == 'POST':
    user = request.form['nm']   
   #  resp = make_response(render_template('readcookie.html'))
    resp = make_response()
    resp.set_cookie('userID', user)
    print(resp)
   
   return resp
@app.route('/testurl')
def testurl():
   r = req.get('https://zh6a1mbc0msy.runkit.sh/')
   print(r.text)
   return r.text
   
@app.route('/myget')
def mygetnodejs():
   g = req.get('http://localhost:4000/')
   print(g.text)
   return g.text

@app.route('/mypost')
def mypostnodejs():
      # headers = {'content-type': 'application/json'}
   mydata ={"name":"lachumiraja"}
   p = req.post('http://localhost:4000/json',mydata)
   print(p.text)
   return p.text

   # p = req.post('http://localhost:4000/json',{"name":"testname"})

# @app.route('/testurl')
# def testurl():
#    r = req.get('https://zh6a1mbc0msy.runkit.sh/')
#    print(r.text)
#    return r.text
   
# @app.route('/myget')
# def mygetnodejs():
#    g = req.get('http://localhost:4000/')
#    print(g.text)
#    return g.text

# @app.route('/mypost')
# def mypostnodejs():
#       # headers = {'content-type': 'application/json'}
#    mydata ={"name":"testname"}
#    p = req.post('http://localhost:4000/json',mydata)
#    print(p.text)
#    return p.text

#    # p = req.post('http://localhost:4000/json',{"name":"testname"})
   
@app.route('/getcookie')
def getcookie():
   name = request.cookies.get('userID')
   return '<h1>welcome '+name+'</h1>'

@app.route('/login',methods = ['post'])
def login():    
    n = request.form["nm"]   
    if n =="abort":
     abort(401)

    if n == "ram":
     flash('You were successfully logged in')
     return redirect(url_for('sucess',name = n))
    if n == "*":  
      return render_template('lkraja.html')
    if n == "10":       
     return redirect(url_for('regint',regint = n))
    if n != "ram":       
     return redirect(url_for('register',registerpara = n))
   
     
    
    #  return redirect(url_for('hello_name',sriram = n))
    #  return redirect(url_for('html'))
   #   return render_template('lkraja.html')

@app.route('/blog/<int:postID>')
def show_blog(postID):
   return 'Blog Number %d' % postID

@app.route('/rev/<float:revNo>')
def revision(revNo):
   return 'Revision Number %f' % revNo

@app.route('/html')
def html():
    return '<html><body><div><center><p style="font-size:16pt;"><b>lkraja page</b></p></center></div></body></html>'

@app.route('/python/')
def hello_python():
   return 'Hello Python'

def hello_world():
   return 'hello world by checking'
app.add_url_rule('/appurl', 'hello', hello_world)

@app.route('/admin')
def hello_admin():
   return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
   return 'Hello %s as Guest' % guest

@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest',guest = "thala"))

if __name__ =='__main__':
    
    app.run(debug=True)