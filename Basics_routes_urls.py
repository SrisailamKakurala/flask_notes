from flask import Flask, request, make_response

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'


## Dynamic routes
@app.route('/hello/<name>')
def greet(name):
    return f'Hello, {name}!'


# by default the params are of type string 
@app.route('/add/<n1>/<n2>')
def add(n1, n2):
    return f'{n1 + n2}'  # 5 + 10 = 510


@app.route('/adds/<int:n1>/<int:n2>')
def add1(n1, n2):
    return f'{n1 + n2}'  # 5 + 10 = 15
    


@app.route('/handle_url_params')
def handle_url_params():
    if 'firstname' in request.args.keys() and 'lastname' in request.args.keys():
        firstname, lastname = request.args['firstname'], request.args['lastname']
        return f'Hello {firstname} {lastname}'
        # http://127.0.0.1:3000/handle_url_params?firstname=ssl&lastname=kakurala
        # o/p: Hello ssl kakurala
    else:
        return "some params are missing"
    
    
    
@app.route('/default-method', methods=['GET'])
def get():
    return 'default method is get'
    
@app.route('/other-methods', methods=['GET', 'POST', 'PUT', 'DELETE'])
def others():
    return 'other methods can be specified in an array'



# differentiating the methods
@app.route('/diff', methods=['GET', 'POST'])
def diff():
    if request.method == 'POST':
        return 'POST'
    elif request.method == 'GET':
        return 'GET'
    else:
        return "u'll never see this"
    
    
# status codes
@app.route('/status')
def status():
    return 'hello', 200



# make_response
@app.route('/response')
def response():
    response = make_response('hello')
    response.status_code = 200
    response.headers['Content-Type'] = 'application/json'
    return response


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)