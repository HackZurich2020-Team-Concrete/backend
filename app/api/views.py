from flask import Flask

import requests
import json
from flask import current_app,jsonify
from . import api_bp


demanRequestersText =  '[{"id":1,"userId":5,"locationN":48.75958376,"locationE":9.16500092,"startDate":"2020-09-04","endDate":"2020-09-27","amount":8.65,"type":"normal","chunkSize":"enormous","model":"demander"},{"id":2,"userId":29,"locationN":48.81206377,"locationE":9.15470123,"startDate":"2020-09-04","endDate":"2020-09-27","amount":3.65,"type":"normal","chunkSize":"enormous","model":"demander"},'+\
'{"id":3,"userId":4,"locationN":48.74079525,"locationE":9.30747986,"startDate":"2020-09-04","endDate":"2020-09-27","amount":4,"type":"normal","chunkSize":"enormous","model":"demander"}'+\
']'

logisticSuppliersText =  '[{"id":1,"userId":29,"startLocationN":48.75958376,"startLocationE":9.16500092,"endLocationN":48.75958376,"endLocationE":9.16500092,"startDate":"2020-09-04","endDate":"2020-09-27","trucks":[{"truckId":1,"freightCapacity":7.2,"operationCost":4.87},{"truckId":2,"freightCapacity":7.2,"operationCost":4.87},{"truckId":3,"freightCapacity":3.7,"operationCost":2.87}],"model":"logistic_supplier"},'+\
    '{"id":2,"userId":2,"startLocationN":48.75958376,"startLocationE":9.16500092,"endLocationN":48.75958376,"endLocationE":9.16500092,"startDate":"2020-09-04","endDate":"2020-09-27","trucks":[{"truckId":1,"freightCapacity":7.2,"operationCost":4.87},{"truckId":2,"freightCapacity":7.2,"operationCost":4.87},{"truckId":3,"freightCapacity":3.7,"operationCost":2.87}],"model":"logistic_supplier"},'+\
    '{"id":3,"userId":3,"startLocationN":48.75958376,"startLocationE":9.16500092,"endLocationN":48.75958376,"endLocationE":9.16500092,"startDate":"2020-09-12","endDate":"2020-09-27","trucks":[{"truckId":1,"freightCapacity":7.2,"operationCost":4.87},{"truckId":2,"freightCapacity":7.2,"operationCost":4.87},{"truckId":3,"freightCapacity":3.7,"operationCost":2.87}],"model":"logistic_supplier"},'+\
    '{"id":4,"userId":2,"startLocationN":48.75958376,"startLocationE":9.16500092,"endLocationN":48.75958376,"endLocationE":9.16500092,"startDate":"2020-07-04","endDate":"2020-08-27","trucks":[{"truckId":1,"freightCapacity":7.2,"operationCost":4.87},{"truckId":2,"freightCapacity":7.2,"operationCost":4.87},{"truckId":3,"freightCapacity":3.7,"operationCost":2.87}],"model":"logistic_supplier"}'+\
    ']'

suplyOffersText =  '[{"id":5,"userId":4,"locationN":48.80256715,"locationE":9.22885895,"startDate":"2020-09-04","endDate":"2020-09-30","amount":4.65,"type":"normal","chunkSize":"ludacris","model":"supplier"},'+\
'{"id":6,"userId":2,"locationN":48.80256715,"locationE":9.22885895,"startDate":"2020-09-04","endDate":"2020-09-30","amount":4.65,"type":"normal","chunkSize":"ludacris","model":"supplier"}'+\
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


app = Flask(__name__)

@api_bp.route('/')
def index():
    return jsonify({})

@api_bp.route('/getAll')
def getAlls():
    return jsonify(requesters+suplyOffers+logisticSuppliers)



@api_bp.route('/getRequesters')
def getRequesters():
    return jsonify(requesters)

@api_bp.route('/getRequester/<int:requester_id>')
def show_post(requester_id):
    found = []
    for requester in requesters:
        if requester["demandRequestID"] == requester_id:
            found.append(requester)
    return jsonify(found)


@api_bp.route('/deleteRequester/<int:requester_id>')
def deleteRequester(requester_id):
    temp = []
    while requesters:
        x = requesters.pop()
        if x["demandRequestID"] != requester_id:
            temp.append(x)
    while temp:
        requesters.append(temp.pop())
    return jsonify(requesters)

@api_bp.route('/addRequester',methods=['GET', 'POST'])
def createRequester():
    requesters.append(request.json)
    return jsonify(requesters)




@api_bp.route('/getLogistics')
def getLogistics():
    return jsonify(logisticSuppliers)

@api_bp.route('/getLogistic/<int:requester_id>')
def show_logistic(requester_id):
    found = []
    for requester in logisticSuppliers:
        if requester["logisticID"] == requester_id:
            found.append(requester)
    return jsonify(found)


@api_bp.route('/deleteLogistic/<int:requester_id>')
def deleteLogistic(requester_id):
    temp = []
    while logisticSuppliers:
        x = logisticSuppliers.pop()
        if x["logisticID"] != requester_id:
            temp.append(x)
    while temp:
        logisticSuppliers.append(temp.pop())
    return jsonify(logisticSuppliers)

@api_bp.route('/addLogistic',methods=['GET', 'POST'])
def createLogistic():
    logisticSuppliers.append(request.json)
    return jsonify(logisticSuppliers)



@api_bp.route('/getSuplyOffers')
def getSuppliers():
    return jsonify(suplyOffers)

@api_bp.route('/getSuplyOffers/<int:requester_id>')
def show_supplier(requester_id):
    found = []
    for requester in suplyOffers:
        if requester["offerId"] == requester_id:
            found.append(requester)
    return jsonify(found)


@api_bp.route('/deleteSupplier/<int:requester_id>')
def deleteSupplier(requester_id):
    temp = []
    while suplyOffers:
        x = suplyOffers.pop()
        if x["offerId"] != requester_id:
            temp.append(x)
    while temp:
        suplyOffers.append(temp.pop())
    return jsonify(suplyOffers)

@api_bp.route('/addSupplier',methods=['GET', 'POST'])
def createSupplier():
    suplyOffers.append(request.json)
    return jsonify(requesters)



@api_bp.route('/getUsers')
def getSUsers():
    return jsonify(users)

@api_bp.route('/getUser/<int:requester_id>')
def show_user(requester_id):
    found = []
    for requester in users:
        if requester["usersId"] == requester_id:
            found.append(requester)
    return jsonify(found)


@api_bp.route('/deleteUser/<int:requester_id>')
def deleteUser(requester_id):
    temp = []
    while users:
        x = users.pop()
        if x["usersId"] != requester_id:
            temp.append(x)
    while temp:
        users.append(temp.pop())
    return jsonify(users)

@api_bp.route('/addUser',methods=['GET', 'POST'])
def createUser():
    users.append(request.json)
    return jsonify(users)

@api_bp.route('/getAddress/<int:long>/<int:lat>')
def calculateLoc(long,lat):
    return jsonify(long)