from flask import Flask, request, g, json, abort
from flask_cors import CORS
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
from sentry_sdk import configure_scope, capture_exception
import pdb # set_trace()
import os

VERSION = os.environ.get("VERSION")

sentry_sdk.init(
    dsn="https://2ba68720d38e42079b243c9c5774e05c@sentry.io/1316515",
    release=VERSION,
    integrations=[FlaskIntegration()]
)
app = Flask(__name__)
CORS(app)

Inventory = {
    'wrench': 1,
    'nails': 1,
    'hammer': 1
}


@app.route('/checkout', methods=['POST'])
def checkout():
    
    body = json.loads(request.data)

    # Event Context - make into Flask middleware
    email = body["email"]
    transactionId = request.headers.get('X-Transaction-ID')
    sessionId = request.headers.get('X-Session-ID')
    with configure_scope() as scope:
        scope.user = { "email" : email }
        scope.set_tag("transaction-id", transactionId)
        scope.set_tag("session-id", sessionId)

    # Checkout
    cart = body["cart"]
    global Inventory
    tempInventory = Inventory
    for item in cart:
        if Inventory[item['id']] <= 0:
            with configure_scope() as scope:
                scope.set_extra("inventory", tempInventory)
            raise Exception("Not enough inventory for " + item['id'])
        else:
            tempInventory[item['id']] -= 1
            response = 'Success purchased ' + item['id'] + ' the updated remaining stock is ' + str(tempInventory[item['id']])
    
    Inventory = tempInventory 

    return response



@app.route('/handled', methods=['GET'])
def handled_exception():
    try:
        '2' + 2
    except TypeError as err:
        capture_exception(err)
        abort(500)

    return 'Success'

@app.route('/unhandled', methods=['GET'])
def unhandled_exception():
    obj = {}
    obj['keyDoesntExist']

