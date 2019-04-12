from flask import Flask, request, g, json

import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
    
sentry_sdk.init(
    dsn="https://18562a9e8e3943088b1ca3cedf222e21@sentry.io/1435220",
    integrations=[FlaskIntegration()]
)

app = Flask(__name__)


# review demo spec in notion
    # set Inventory as 'extra' info on Sentry Event scope
# working endpoint, return response
# introduce broken code to trigger...
# graceful error handling
# return response


Inventory = {
    'wrench': 0,
    'nails': 0,
    'hammer': 1
}


@app.route('/checkout', methods=['POST'])
def checkout():
    
    # POST BODY
    dictionary = json.loads(request.data)

    # MODULARIZE THIS...MIDDLEWARE for other endpoints
    email = dictionary['email']
    # set as user...
    transactionId = request.headers.get('X-Transaction-ID')
    print transactionId # does not print anything...?
    # set as Tag...

    # CHECKOUT
    cart = dictionary['cart']
    print cart # [{u'id': u'nails'}]...?
    global Inventory
    tempInventory = Inventory
    for item in cart:
        if Inventory[item.id] <= 0:
            # set Inventory as the 'extra'
            raise Exception("Not enough inventory for ")
        else:
            tempInventory-= 1
    Inventory = tempInventory 

    return 'Success'



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
