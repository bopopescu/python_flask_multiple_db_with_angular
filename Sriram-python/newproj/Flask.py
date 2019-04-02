from flask import Flask, flash, redirect, render_template, request, url_for
from werkzeug import secure_filename
import os as os
from datetime import datetime
from flask_mail import Mail, Message
app = Flask(__name__)
up = './UPLOAD_FOLDER'
app.config['UPLOAD_FOLDER'] = up
app.secret_key = 'random string'
mail=Mail(app)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'mytestinga1@gmail.com'
app.config['MAIL_PASSWORD'] = 'Abc@12_xcZ^&'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

@app.route('/upload')
def file_upload():
   return render_template('fileupload.html')

@app.route("/mymail")
def mymail():
   msg = Message('Hello', sender = 'mytestinga1@gmail.com', recipients = ['lachumiraja.u@mnw.co.in'])
   msg.body = "Hello Flask message sent from Flask-Mail"
   mail.send(msg)
   return "Sent"

@app.route('/uploader',methods = ['get','post'])
def file_uploads():
   mycurrentdate = datetime.now()
   f = request.files['file']
   filename = secure_filename(f.filename)
   print(filename)
   print(f)
   f.save(os.path.join(app.config['UPLOAD_FOLDER'],str(mycurrentdate)+filename))   
   return '<html><center><p>This<b style="color:red">'' '+filename+' ' '</b><span>is Successfully uploaded</span></p></center></html>'

@app.route('/')
def index():
   return render_template('flashindex.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
   error = None
   
   if request.method == 'POST':
      if request.form['username'] != 'admin' or \
         request.form['password'] != 'admin': error = 'Invalid username or password. Please try again!'
      else:
         flash('You were successfully logged in')
         return redirect(url_for('index'))
			
   return render_template('flashlogin.html', error = error)

if __name__ == "__main__":
   app.run(debug = True)