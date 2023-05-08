import pytest
from app import app, db , rebuilddb
import json


@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_user_apis(client):
    rebuilddb()
    #Standard get and post requests
    rv = app.test_client().get('/user/getuser')
    assert b'not_logged_in' in rv.data
    rv = app.test_client().get('/user/getuserlist')
    assert b'jack0@gmail.com' in rv.data
    rv = app.test_client().post('/user/getuserbyid', json={"userid":"0"})
    assert b'admin@admin.com' in rv.data

    #Test postuser and verify by checking userlist
    rv = app.test_client().post('/user/postuser', json={"email":"test@unit.com","password":"password","first_name":"test","phone_no":"+44123123123"})
    assert b'success' in rv.data
    rv = app.test_client().post('/user/postuser', json={"email":"test@unit.com","password":"password","first_name":"test","phone_no":"+44123123123"})
    assert b'email_has_been_used' in rv.data
    rv = app.test_client().post('/user/postuser', json={"email":"admintest@unit.com","password":"password","first_name":"test","phone_no":"+44123123123", "privilege":"admin"})
    assert b'success' in rv.data
    rv = app.test_client().get('/user/getuserlist')
    assert b'test@unit.com' and b'admintest@unit.com' in rv.data

    rv = app.test_client().post('/user/deleteuser', json={"id":"0"})
    assert b'success' in rv.data
    #rv = app.test_client().post('/user/deleteuser', json={"id":"0"}) #TODO: You can delete an already deleted user
    #assert b'does not exist' in rv.data

    rv = app.test_client().post('/user/updateuser', json={"id":"1", "fields":[{"first_name":"test2"}]})
    assert b'success' in rv.data
    
    rv = app.test_client().post('/account/getuserlistings') #TODO: Do we need getuserlistingsbyid ?
    assert b'not_logged_in' in rv.data
    rv = app.test_client().post('/account/getuserdatalinks')
    assert b'not_logged_in' in rv.data

    #Add a notification and verify by checking user
    rv = app.test_client().post('/user/addnotification', json={"userid":"1", "title":"testnotification", "message":"test"})
    assert b'success' in rv.data
    rv = app.test_client().post('/user/getuserbyid', json={"userid":"1"})
    assert b'testnotification' in rv.data

    #Make user a staff and admin and verify by checking user
    rv = app.test_client().post('/user/makeuserstaff', json={"userid":"0"})
    assert b'success' in rv.data 
    user_info = db.Users.find_one({"_id":"0"})
    assert user_info.get("privilege") == "staff"

    rv = app.test_client().post('/user/makeuseradmin', json={"userid":"1"})
    assert b'success' in rv.data
    user_info = db.Users.find_one({"_id":"1"})
    assert user_info.get("privilege") == "admin"


def test_device_apis(client):
    rv = app.test_client().post('/device/getdevice', json={"id":"0"})
    assert b'device_not_found' in rv.data
    rv = app.test_client().post('/device/postdevice', json={"user_id":"0", "brand":"testbrand", "model":"testmodel", "identification":"rare", "status":"shipped", "operating_system":"android", "memory_storage":"64GB", "color":"red", "type":"phone", "description":"this is a phone", "service":"testservice", "datalink":"testdatalink", "qr_code":"testqrcode", "verified":False})
    assert b'success' in rv.data
    rv = app.test_client().get('/device/getdevicelist')
    assert b'success' and b'this is a phone' in rv.data
    device_id = json.loads(json.loads(rv.data).get("device_list"))[0].get("_id")

    rv = app.test_client().post('/device/addpayment' , json={"id":device_id, "payment_amount":100, "payment_id":999})
    assert b'success' in rv.data
    rv = app.test_client().post('/device/addpayment' , json={"id":device_id, "payment_amount":100, "payment_id":123, "type":"extended"})
    assert b'success' in rv.data
    rv = app.test_client().post('/device/generatedatalink', json={"id":device_id})
    assert b'success' in rv.data
    rv = app.test_client().post('/device/generateqr', json={"id":device_id})
    assert b'success' in rv.data

    rv = app.test_client().post('/device/getdevice', json={"id":device_id})
    assert b'success' and b'payment2' and b'extended' in rv.data

    #update device
    rv = app.test_client().post('/device/updatedevice', json={"id":device_id, "fields":[{"brand":"testbrand2"}]})
    assert b'success' in rv.data
    rv = app.test_client().post('/device/getdevice', json={"id":device_id})
    assert b'success' and b'testbrand2' in rv.data
    #delete device
    rv = app.test_client().post('/device/deletedevice', json={"id":device_id})
    assert b'success' in rv.data
    rv = app.test_client().post('/device/getdevice', json={"id":device_id})
    assert b'record deleted' in rv.data
    #TODO: Upload image untested


