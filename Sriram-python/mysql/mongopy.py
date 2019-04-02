from flask import Flask,render_template,url_for,redirect,request
from pymongo import MongoClient
client = MongoClient()
client = MongoClient('mongodb://localhost:27017')
db = client.mydb
posts = db.ram

post_data = {
    'title': 'Python and MongoDB',
    'content': 'PyMongo is fun, you guys',
    'author': 'Scott'
}
resultinsert = posts.insert_one(post_data)
print('One post: {0}'.format(resultinsert.inserted_id))


resultselect = posts.find(post_data)
print('select: {0}'.format(resultselect))

resultfindone = posts.find_one({"author":"Scott"})
print('One select: {0}'.format(resultfindone))
for i in resultfindone.values():
    print(i)
    print(resultfindone))





app = Flask(__name__)

@app.route('/')
def myindex():
 return render_template('index.html')

@app.route('/process',methods=['get','post'])
def process():
    d = mongo.db.ram.find()
    print(d)
    return "Helo"

if __name__ == '__main__':
    app.run(debug=True)