from flask import Flask,render_template,redirect,url_for,request
import json
import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__) 
db = pymysql.connect(host="localhost",  # your host 
                     user="root",       # username
                     passwd="password",     # password
                     db="ram")   # name of the database
cur = db.cursor() 

@app.route('/')
def indexpage():
 return render_template('index.html')

@app.route('/insert',methods=['post'])
def process():
 email = request.form['email']    
 psw = request.form['psw']    
 pswrepeat = request.form['pswrepeat']    
 print(email,psw,pswrepeat)
 sql= "insert into register(email,password1,password2) values(%s,%s,%s)"
 val=(email,psw,pswrepeat)
 cur.execute(sql,val)
 db.commit()
 return "gotit"

@app.route('/select',methods=['get']) 
def select():
    sql="select * from register"
    cur.execute(sql)
    resultdata= cur.fetchall()
    a=""
    b=""
    c=""
    d=""
    for i in resultdata:
        print(i[1])
        a=i[1]
        b=i[2]
        c=i[3]
        d=i[4]
    h = cur.description    
    x1 = {
        h[1][0]:a,
        h[2][0]:b,
        h[3][0]:c,
        h[4][0]:d
    }
    print("dictx1",x1)
    return render_template('table.html',result = x1)
    # z = json.dumps(resultdata)
    # print("jsondups",z)
    
    
# Create a Cursor object to execute queries.

# Select data from table using SQL query.
# cur.execute("select * from register")
# myresult = cur.fetchall()
# print(myresult)
# for i in myresult:
#     print(i)
if __name__ == '__main__':
    app.run(debug=True)