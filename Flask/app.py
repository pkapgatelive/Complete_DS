from flask import Flask, request, render_template


# name of the app and the entry point of the application
app = Flask(__name__)


# Start handling the hosting
# routing menas which URL we want to coinsider

@app.route('/', )
def welcome():
    return render_template('index.html')
@app.route('/aboutus')
def aboutus():
    return "About us: we are ineuronses"

# this we are using for the testing purpose at Postman
@app.route('/demo', methods = ['GET', 'POST'])
def math_operation_demo():
    if (request.method == 'POST'):
        operation = request.json['operation']
        num1 = request.json['num1']
        num2 = request.json['num2']
        result = 0

        if operation == 'add':
            result = num1 + num2
        elif operation =='multiply':
            result = num1 * num2
        elif operation == 'divide':
             result = num1 / num2
        else:
            result = num1 - num2

        return "The operation is {} and the result is {}".format(operation, result)
 
# this we are using for the HTML page
@app.route('/math_operation', methods = ['GET', 'POST'])
def math_operation():
    if (request.method == 'POST'):
        operation = request.form['operation']
        num1 = int(request.form['num1']) 
        num2 = int(request.form['num2'])
        result = 0

        if operation == 'add':
            result = num1 + num2
        elif operation =='multiply':
            result = num1 * num2
        elif operation == 'divide':
             result = num1 / num2
        else:
            result = num1 - num2

        return render_template("results.html", result=result)
if __name__ == '__main__':
    app.run(host = "0.0.0.0", port=9000)
