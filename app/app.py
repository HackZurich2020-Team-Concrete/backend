from flask import Flask
import requests
import json
from flask import jsonify
from flask import request


r=requests.get(
      'http://api.plos.org/search?q=title:%22Drosophila%22%20and%20body:%22RNA%22&fl=id,abstract&wt=json&indent=on')



demanRequestersText =  '[{ "demandRequestID":1, "userId":1, "locationN":48.75958376,"locationE":9.16500092,"startDate": "2020-08-04","endDate": "2020-09-27","amount": 8.65,"type": "normal", "chunkSize": "enormous"},'+\
    '{ "demandRequestID":2, "userId":2, "locationN":48.75958376,"locationE":9.16500092,"startDate": "2020-09-04","endDate": "2020-09-27","amount": 8.65,"type": "normal", "chunkSize": "small"}'+\
        ']'
suplyOffersText =  '[{ "offerId":3, "userId":3, "locationN":48.80256715,"locationE":9.22885895,"startDate": "2020-09-04","endDate": "2020-09-30","amount": 4.65,"type": "normal", "chunkSize": "ludacris"},'+\
    '{ "offerId":4, "userId":4, "locationN":48.80256715,"locationE":9.22885895,"startDate": "2020-09-04","endDate": "2020-09-30","amount": 4.65,"type": "normal", "chunkSize": "ludacris"},'+\
    '{ "offerId":5, "userId":2, "locationN":48.80256715,"locationE":9.22885895,"startDate": "2020-09-04","endDate": "2020-09-13","amount": 1.65,"type": "poor", "chunkSize": "enormous"},'+\
    '{ "offerId":6, "userId":4, "locationN":48.80256715,"locationE":9.22885895,"startDate": "2020-09-04","endDate": "2020-12-30","amount": 5.15,"type": "normal", "chunkSize": "small"}'+\
        ']'

logisticSuppliersText =  '[{"logisticID":5,"user ID":5,"startLocationN":48.75958376,"startLocationE":9.16500092,"endLocationN":48.75958376,"endLocationE":9.16500092,"startDate":"2020-07-04","endDate":"2020-09-27","trucks":[{"truckId":1,"freightCapacity":7.2,"operationCost":4.87},{"truckId":2,"freightCapacity":7.2,"operationCost":4.87},{"truck id":3,"freightCapacity":3.7,"operationCost":2.87}]},'+\
    '{"logisticID":6,"user ID":6,"startLocationN":48.75958376,"startLocationE":9.16500092,"endLocationN":48.75958376,"endLocationE":9.16500092,"startDate":"2020-09-04","endDate":"2020-09-27","trucks":[{"truckId":1,"freightCapacity":7.2,"operationCost":4.87},{"truckId":2,"freightCapacity":7.2,"operationCost":4.87}]}'+\
        ']'

userText='[{ "usersId":1, "name":"Katja J Gerste", "Address:":"Bayreuther Strasse 96,15232","phoneNumber":"069 35 85695","email": "t6zhavhc0p@temporary-mail.net"},'+\
   '{ "usersId":2,"name":"Ines P Holzman", "Address:":"Bayreuther Strasse 57,15832","phoneNumber":"069 79 45863","Email":"685cyc9cb9f@temporary-mail.net"},'+\
    '{ "usersId":3,"name":"Heike J Gruenewald", "Address:":"Genslerstraße 65,13587","phoneNumber":"030 29 83297","Email":"3x9r9s1wqy4@temporary-mail.net"},'+\
    '{ "usersId":4,"name":"Kristin M Huber", "Address:":"Leopoldstraße 76,13503","phoneNumber":"030 64 81370","Email":"n2i3ezfnm4k@temporary-mail.net"},'+\
    '{ "usersId":5,"name":"Ralf N Schweitzer", "Address:":"Genslerstraße 3,12103","phoneNumber":"030 54 82903","Email":"3x9r9s1wqy4@temporary-mail.net"},'+\
    '{ "usersId":6,"name":"Thomas Schulz", "Address:":"Rhinstrasse 44,80714","phoneNumber":"089 89 75728","Email":"svc5y2d3goj@temporary-mail.net"}'+\
        ']'

# parse users:
requesters = json.loads(demanRequestersText)
suplyOffers = json.loads(suplyOffersText)
logisticSuppliers = json.loads(logisticSuppliersText)
users = json.loads(userText)

f= open("guru99.txt","w+")
f= open("data.txt","r")

if f.mode == 'r':
    contents =f.read()

if not contents:
     requesters = json.loads(contents)





app = Flask(__name__)

@app.route('/')
def index():
    return jsonify(r.text)

@app.route('/getAll')
def getAlls():
    return jsonify(requesters+suplyOffers+logisticSuppliers)



@app.route('/getRequesters')
def getRequesters():
    return jsonify(requesters)

@app.route('/getRequester/<int:requester_id>')
def show_post(requester_id):
    found = []
    for requester in requesters:
        if requester["demandRequestID"] == requester_id:
            found.append(requester)
    return jsonify(found)


@app.route('/deleteRequester/<int:requester_id>')
def deleteRequester(requester_id):
    temp = []
    while requesters:
        x = requesters.pop()
        if x["demandRequestID"] != requester_id:
            temp.append(x)
    while temp:
        requesters.append(temp.pop())
    return jsonify(requesters)

@app.route('/addRequester',methods=['GET', 'POST'])
def createRequester():
    requesters.append(request.json)
    return jsonify(requesters)




@app.route('/getLogistics')
def getLogistics():
    return jsonify(logisticSuppliers)

@app.route('/getLogistic/<int:requester_id>')
def show_logistic(requester_id):
    found = []
    for requester in logisticSuppliers:
        if requester["logisticID"] == requester_id:
            found.append(requester)
    return jsonify(found)


@app.route('/deleteLogistic/<int:requester_id>')
def deleteLogistic(requester_id):
    temp = []
    while logisticSuppliers:
        x = logisticSuppliers.pop()
        if x["logisticID"] != requester_id:
            temp.append(x)
    while temp:
        logisticSuppliers.append(temp.pop())
    return jsonify(logisticSuppliers)

@app.route('/addLogistic',methods=['GET', 'POST'])
def createLogistic():
    logisticSuppliers.append(request.json)
    return jsonify(logisticSuppliers)



@app.route('/getSuplyOffers')
def getSuppliers():
    return jsonify(suplyOffers)

@app.route('/getSuplyOffers/<int:requester_id>')
def show_supplier(requester_id):
    found = []
    for requester in suplyOffers:
        if requester["offerId"] == requester_id:
            found.append(requester)
    return jsonify(found)


@app.route('/deleteSupplier/<int:requester_id>')
def deleteSupplier(requester_id):
    temp = []
    while suplyOffers:
        x = suplyOffers.pop()
        if x["offerId"] != requester_id:
            temp.append(x)
    while temp:
        suplyOffers.append(temp.pop())
    return jsonify(suplyOffers)

@app.route('/addSupplier',methods=['GET', 'POST'])
def createSupplier():
    suplyOffers.append(request.json)
    return jsonify(requesters)



@app.route('/getUsers')
def getSUsers():
    return jsonify(users)

@app.route('/getUser/<int:requester_id>')
def show_user(requester_id):
    found = []
    for requester in users:
        if requester["usersId"] == requester_id:
            found.append(requester)
    return jsonify(found)


@app.route('/deleteUser/<int:requester_id>')
def deleteUser(requester_id):
    temp = []
    while users:
        x = users.pop()
        if x["usersId"] != requester_id:
            temp.append(x)
    while temp:
        users.append(temp.pop())
    return jsonify(users)

@app.route('/addUser',methods=['GET', 'POST'])
def createUser():
    users.append(request.json)
    return jsonify(users)

@app.route('/getAddress/<int:long>/<int:lat>')
def calculateLoc(long,lat):
    return jsonify(long)