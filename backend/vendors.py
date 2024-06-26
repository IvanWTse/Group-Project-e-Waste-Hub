# import packages and modules
from flask import Blueprint, request
from app import db
from bson.json_util import dumps
import datetime
import uuid

# define a blueprint for vendor APIs
vendors_api = Blueprint('vendors_api', __name__)

#path = /vendor

# get all vendors
@vendors_api.route("/getvendorlist")
def getVendors():
    # find all vendors that haven't been deleted
    vendors = db.Vendors.find({"is_deleted":False})
    list_vendors = list(vendors)

    # check the result and return response accordingly
    if len(list_vendors) == 0:
        return {"message":"empty list", "response":"error"}
    return {"response":"success", "vendor_list":list_vendors}

# get a specific vendor
@vendors_api.route("/getvendor", methods=['POST'])
def getVendor():
    # extract vendor id from request body
    data = request.get_json()
    vendor_id = data.get("id")
    # look up vendor in the collection
    vendor = db.Vendors.find_one({"_id":vendor_id})

    # check if vendor does not exist or has been deleted
    if vendor is None:
        return {"message":"vendor_not_found"}
    if vendor.get("is_deleted"):
        return {"message":"record deleted", "response":"error"}
    # return the vendor
    return {"response":"success", "vendor_info":vendor}

# get all vendors
@vendors_api.route("/getall")
def getAll():
    # find all vendors that haven't been deleted
    vendors = db.Vendors.find({"is_deleted":False})
    list_vendors = list(vendors)

    # check the result and return response accordingly
    if len(list_vendors) == 0:
        return {"message":"empty list", "response":"error"}
    json_vendors = dumps(list_vendors)
    return {"response":"success", "vendor_list":json_vendors}

# post vendor
@vendors_api.route("/postvendor", methods=['POST'])
def postVendor():
    # generate a random unique id
    vendor_id = str(uuid.uuid4())
    # extract data from request body
    data = request.get_json()
    brand = data.get("brand")
    model_name = data.get("model_name")
    size = data.get("size")
    storage = data.get("storage")
    sale_price = data.get("sale_price")
    ts = datetime.datetime.utcnow()
    ts_mod = datetime.datetime.utcnow()
    
    # insert the new vendor into collection
    db.Vendors.insert_one({"_id":vendor_id,"brand":brand,"model_name":model_name,"size":size,"storage":storage,\
                           "sale_price":sale_price,"ts":ts,"ts_mod":ts_mod,"is_deleted":False})
    return {"response":"success"}

# delete vendor
@vendors_api.route("/deletevendor", methods=['POST'])
def deleteVendor():
    # extract vendor id from request body
    data = request.get_json()
    vendor_id = data.get("id")
    query = {"_id":vendor_id}
    newvalues = { "$set": { "ts_mod": datetime.datetime.utcnow(),"is_deleted":True}}
    # delete the vendor
    result = db.Vendors.update_one(query, newvalues)

    # if successfully deleted, return success, otherwise return an error message
    if result.matched_count == 1:
        return {"response":"success"}
    else:
        return {"message": "vendor does not exist", "response":"error"}

# update vendor
@vendors_api.route("/updatevendor", methods=['POST'])
def updateVendor():
    # extract vendor id and fields to be updated from the request body
    data = request.get_json()
    vendor_id = data.get("id")
    query = {"_id":vendor_id}
    fields = data.get("fields")[0]
    # create a update dictionary
    update_dict = {}
    for key in fields:
        update_dict[key] = fields[key]
    update_dict["ts_mod"] = datetime.datetime.utcnow()
    # update the vendor
    result = db.Vendors.update_one(query, {"$set": update_dict})

    # check if the update was successful, return a response accordingly
    if result.matched_count == 1:
        return {"response": "success"}
    else:
        return {"message": "Vendor does not exist", "response":"error"}
