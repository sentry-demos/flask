from flask import Flask, request

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

@app.route('/')
def hello():
    # need request Body for POST Checkout route
    # param = request.args.get('name')
    # print param
    return 'Hello World'
