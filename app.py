from flask import Flask, request


# name of the app and the entry point of the application
app = Flask(__name__)


# Start handling the hosting
# routing menas which URL we want to coinsider

@app.route('/', )
def hello_world():
    return "Hello, world"

@app.route('/aboutus')
def aboutus():
    return "About us: we are ineuronses"

@app.route('/add', methods = ['GET', 'POST'])
def math_operation_add():
    if (request.method == 'POST'):
        operation = request.json['operation']
        num1 = request.json['num1']
        num2 = request.json['num2']
        result = num1 + num2 
        return "The operation is {} and the result is {}".format(operation, result)

@app.route('/multiply', methods = ['GET', 'POST'])
def math_operation_multiply():
    if (request.method == 'POST'):
        operation = request.json['operation']
        num1 = request.json['num1']
        num2 = request.json['num2']
        result = num1 * num2 
        return "The operation is {} and the result is {}".format(operation, result)

if __name__ == '__main__':
    app.run(host = "0.0.0.0", port=9000)
