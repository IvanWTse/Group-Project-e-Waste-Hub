# APIS

### user
- GET one (/user/getuser) working
- GET all (/user/getuserlist) working
- POST one (/user/postuser) working post:{email,password,first_name,last_name(optional)}
- DELETE one (soft) (/user/deleteuser) working post:{id}
- PATCH one (/user/updateuser) working post {"id":"xx","fields":[{"password":"new","email":"new@gmail.com"}]}

### user
Get User Information
- URL: /user/getuser
- Method: GET
- Description: Retrieves information about the currently logged-in user.
- Response:
Success：{"response": "success","user_info": {id,email,first_name,last_name,ts,ts_mod,"is_deleted": false}}(if user is logged in and session cookie is valid)
Error: {"message": "not_logged_in", "response": "error"}(if session cookie is invalid or user is not logged in)

Get user information based on ID
- URL: /user/getuserbyid
- Method: POST
- Description: Obtain detailed information of the user based on their ID.
- Data Params: { "userid": "user_id" }
- Response: Details of the user with the specified ID, or error message


Get user list
- URL: /user/getuserlist
- Method: GET
- Description: Obtain a list of all undeleted users in the system.
- Response: List containing all undeleted users, or error message

Create New Document:
- URL: /user/postdocument
- Method: POST
- Description: Creates a new document.
- Response:
Success: {"response": "success"}
Error: {"message": "creation_failed", "response": "error"}(if the document creation failed)

Delete Document:
- URL: /user/deletedocument
- Method: POST
- : Deletes the document with a specific ID.
- Response:
Success: {"response": "success"}(if the document is deleted successfully)
Error: {"message": "document_does_not_exist", "response": "error"}(if the document does not exist)

Update Document:
- URL: /user/updatedocument
- Method: POST
- Description: Updates the document with a specific ID.
- Response:
Success: {"response": "success"}(if the document is updated successfully)
Error: {"message": "document_does_not_exist", "response": "error"}(if the document does not exist)

Get User Device Listings:
- URL: /user/getuserlistings
- Method: POST
- Description: Retrieves a list of devices for the currently logged in user.
- Response:
Success: {"response":"success", "user_list":json_list}
Error: {"message":"not_logged_in", "response":"error"} or {"message":"empty list","response":"error"}

Get User Device Listings by User ID:
- URL: /user/getuserlistingsbyid
- Method: POST
- Description: Retrieves a list of devices for a user by their user ID.
- Response:
Success: {"response":"success", "user_list":json_list}
Error: {"message":"empty list","response":"error"}

Get User Data Links:
- URL: /user/getuserdatalinks
- Method: POST
- Description: Retrieves data retrieval links for the devices of the currently logged in user.
- Response:
Success: {"response":"success", "user_list":json_list}
Error: {"message":"not_logged_in", "response":"error"} or {"message":"empty list","response":"error"}

Add Notification:
- URL: /user/addnotification
- Method: POST
- Description: Adds a notification for a specific user.
- Response:
Success: {"response": "success"}
Error: {"message": "User does not exist", "response":"error"}

Mark Notification as Seen:
- URL: /user/notificationisseen
- Method: POST
- Description: Marks a specific notification as seen for a user.
- Response:
Success: {"response": "success"}
Error: {"message": "Notification does not exist", "response":"error"}

Make User a Staff:
- URL: /user/makeuserstaff
- Method: POST
- Description: Upgrades a user's privilege to staff level.
- Response:
Success: {"response": "success"}
Error: {"message": "User does not exist", "response":"error"}

Make User an Admin:
- URL: /user/makeuseradmin
- Method: POST
- Description: Upgrades a user's privilege to admin level.
- Response:
Success: {"response": "success"}
Error: {"message": "User does not exist", "response":"error"}


### device
- GET one (/device/getdevice) working post:{id}
- GET all (/device/getdevicelist) working
- POST one (/device/postdevice) working post:{"user_id":"a","vendor_id":"b","status":"c","color":"d","type":"e"}
- DELETE one (soft) (device/deletedevice) working post:{id}
- PATCH one (/device/updatedevice) working post {"id":"xx","fields":[{"status":"newstatus","color":"newcolor"}]}

Get Device
- URL: /getdevice
- Method: POST
- Description: Retrieve a specific device based on its ID.
- Response:
Success: {"response": "success", "device_info": {}}
Error:
If device not found: {"message": "device_not_found"}
If device record is deleted: {"message": "record deleted", "response":"error"}

Get Device List
- URL: /getdevicelist
- Method: GET
- Description: Retrieve a list of all devices, sorted by timestamp in descending order.
- Response:
Success: {"response": "success", "device_list": []}
Error: {"message": "empty list", "response":"error"}

Post a Device
- URL: /postdevice
- Method: POST
- Description: Add a new device to the database.
- Response:
Success: {"response": "success", "new_device_id": ""}
Error: {"message": "error message", "response":"error"}

Add Payment to a Device
- URL: /addpayment
- Method: POST
- Description: Add a payment to a specific device.
- Response:
Success: {"response":"success"}
Error: {"message":"device does not exist", "response":"error"}

Generate Data Link
- URL: /generatedatalink
- Method: POST
- Description: Generates a new data link for a device.
- Response:
Success: {"response": "success"}
Error: {"message": "device does not exist", "response":"error"}

Generate QR Code
- URL: /generateqr
- Method: POST
- Description: Generates a new QR code for a device.
- Response:
Success: {"response": "success"}
Error: {"message": "device does not exist", "response":"error"}

Delete a Device
- URL: /deletedevice
- Method: POST
- Description: Marks a device as deleted in the database.
- Response:
Success: {"response": "success"}
Error: {"message": "device does not exist", "response":"error"}

Update a Device
- URL: /updatedevice
- Method: POST
- Description: Updates the specified fields for a device in the database.
- Response:
Success: {"response": "success"}
Error: {"message": "Device does not exist", "response":"error"}

Verify Device by ID
- URL: /verifydevicebyid
- Method: POST
- Description: Verifies a device by its ID.
- Response:
Success: {"response": "success"}
Error: {"message": "Device does not exist", "response":"error"}

Create Checkout Session
- URL: /create-checkout-session
- Method: POST
- Description: Creates a new Stripe checkout session.
- Response:
Success: {"response": "success", "checkout_session": ""}
Error: {"message": "error message"}

Upload Image
- URL: /uploadimg
- Method: POST
- Description: Uploads an image for a device and saves the path in the database.
- Response:
Success: {"response": "success"}
Error: {"message": "device does not exist", "response":"error"}

### payment
- GET one
- GET all
- POST one
- DELETE one (soft)
- PATCH one

### transaction
- GET all (/transaction/gettransactionlist) working
- POST getuserpayments (/transaction/getuserpayments) working
- POST getuserpaymentsbyid (/transaction/getuserpaymentsbyid) working post:{userid}


### auth
- POST login (/auth/login) working post:{email, password}
- POST register working post:{email,password,first_name,last_name(optional)}
- POST login/callback not working
- GET logout working

### account
- GET user-listings working (returns devices?)
- GET user-payments not working
- GET user-data-links not working

### datalinks
- GET one
- GET all
- POST one
- DELETE one (soft)
- PATCH one

### vendors
- GET vendorlist (/vendor/getvendorlist) working
- GET vendor working post:{id}
- GET all working
- POST one working post:{"brand":"a","model_name":"b","size":"c","storage":"d","sale_price":"123"}
- DELETE one (soft) working
- PATCH one (/vendor/updatevendor) working post {"id":"xx","fields":[{"brand":"newbrand","size":"new"}]}
