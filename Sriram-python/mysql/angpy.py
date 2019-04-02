from flask import Flask,jsonify,request
from flask_cors import CORS,cross_origin
import json
from pymongo import MongoClient
client = MongoClient()
client = MongoClient('mongodb://localhost:27017')
db = client.mydb
posts = db.ram

app = Flask(__name__)
cors = CORS(app)
@app.after_request
def add_headers(response):
  response.headers.add('Content-Type', 'application/json')
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Methods', 'PUT, GET, POST, DELETE, OPTIONS')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Expose-Headers', 'Content-Type,Content-Length,Authorization,X-Pagination')
  return response

@app.route('/createdata',methods=['post'])
def createdata():
    data = request.json
    print(data)
    conjosn = json.dumps(data)
    createdata = {
    "firstname":data['firstname'] ,
    "lastname":data['lastname']    
     }
    print(createdata)
    insertmongodata = posts.insert_one(createdata)
    selectmongodata = posts.find()
    for i in selectmongodata:
      print(i)

    # createdataresult = posts.insert_one(createdata)
    # print('inserted successfully')
    # # print('inserted successfully: {0}'.format(createdataresult))

    return str(selectmongodata)


@app.route('/selectall',methods=['get'])
def get():
  selectmongodata = posts.find()
  print("direct print",selectmongodata)
  cars =[]
  for i in selectmongodata:
    print(i)
    cars.append(str(i))
  print(cars,"cars")  
  return str(cars)


    #  data = request.data
    # # myfirst = request.form.get("fname")
    # print(myfirst)
    # # data = request.json #josn
    # # cjson = json.dumps(data) #convert to json
    # print("req.json",data)
    # # print("json parse python to json",cjson)
    # # y =  json.loads(cjson) #
    # # print("jsonto python",y["name"])
    # # for i in y:
    # #     print(i,y[i])
    # # # a = json.loads(cjson)
    # # return cjson
    # return ""



@app.route('/process',methods=['get','post'])
# @cross_origin(origin='*')
def test():
#  return "Python connectivity connected"
 return jsonify({"Python connectivity connected":"successyflly"})

if __name__ == "__main__":
    app.run(debug=True)





#     from flask import Flask,jsonify,request
# from flask_cors import CORS,cross_origin

# app = Flask(__name__)
# cors = CORS(app)

# @app.route('/process',methods=['get','post'])
# @cross_origin(origin='*')
# def test():
#  return jsonify({"Python connectivity connected":"successyflly"})

# @app.route('/')
# if __name__ == "__main__":
#     app.run(debug=True)



# #     @app.after_request
# # def add_headers(response):
# #     response.headers.add('Content-Type', 'application/json')
# #     response.headers.add('Access-Control-Allow-Origin', '*')
# #     response.headers.add('Access-Control-Allow-Methods', 'PUT, GET, POST, DELETE, OPTIONS')
# #     response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
# #     response.headers.add('Access-Control-Expose-Headers', 'Content-Type,Content-Length,Authorization,X-Pagination')
# #     return response


# # @app.route('/create',methods=["post"]) 
# # def create():
# #  name = request.form['name']  
# #  print(name) 
# #  return jsonify({"name":"con"})


# @app.route('/createdata',methods=['post'])
# def createdata():
#     data = request.data
#     datadict = json.loads(data)
#     print(datadict)  
#     return "created"