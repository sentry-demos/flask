from flask import Flask, request, g

import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
    
sentry_sdk.init(
    dsn="https://18562a9e8e3943088b1ca3cedf222e21@sentry.io/1435220",
    integrations=[FlaskIntegration()]
)

app = Flask(__name__)

# request.form .args .files .method

# 1 POST request to /checkout
# 2 variablize the request's body
# 3 variablize the request's header X-Transaction-Id
# 4 review demo spec in notion
# 5 working endpoint, return response
# 6 introduce broken code to trigger...
# 7 graceful error handling
# 6 return response

# global Inventory
Inventory = {
    'wrench': 0,
    'nails': 0,
    'hammer': 1
}

# {cart: [{ id: 'nails' }, ...], email: '...@yahoo.com'}
# param = request.args.get('name')
@app.route('/checkout', methods=['POST'])
def checkout():
    
    # POST BODY
    req_data = request.get_json()
    
    # MODULARIZE THIS...
    email = req_data['email']
    
    # CHECKOUT
    cart = req_data['cart']
    global Inventory
    tempInventory = Inventory
    for item in cart:
        print Inventory[item.id]
        if Inventory[item.id] <= 0:
            raise Exception("Not enough inventory for ")
        else:
            tempInventory-= 1
    Inventory = tempInventory 

    # RESPONSE
    return 'Success'


#GET requests
@app.route('/handled', methods=['GET'])
def handled_exception():
    return 'Success'


@app.route('/unhandled', methods=['GET'])
def unhandled_exception():
    return 'Success'

@app.route('/warn', methods=['GET'])
def warn():
    return 'Success'

@app.route('/error', methods=['GET'])
def error():
    return 'Success'

# RIGHT BEFORE ERROR...
# in the Event that gets sent? so before throwing error, update the Extra..
# - set Inventory as **extra information** / additional data

# MIDDLEWARE
# let transactionId = request.header('X-Transaction-ID');
# transaction-id` as tag
# email as user
