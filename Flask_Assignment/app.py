import logging
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Configure the logging
logging.basicConfig(filename='app.log', level=logging.DEBUG,
                    format='%(asctime)s [%(levelname)s] - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
result = 0
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        # Access the items data from the form
        if request.method == 'POST':
            data = request.get_json()  # Get JSON data from the request
            print(data)

            items = list(data.get('itemName', []))  # List of item names
            values = list(data.get('itemValue', []))  # List of item values
            print(items, values)

            # Log the received items for debugging
            logging.info(f'Received items: {dict(zip(items, values))}')

            # Perform the calculation (replace this with your calculation logic)
            total_cost = sum(map(int, values))

            if total_cost <= 1000:
                result = total_cost - ((total_cost * 10) / 100)
            elif 1000 < total_cost <= 2000:
                result = total_cost - ((total_cost * 20) / 100)
            else:
                result = total_cost - ((total_cost * 30) / 100)

            # Log the calculated total for debugging
            logging.info(f'Calculated result: {result}')

            # Return the result as JSON
            return jsonify({'result': result})

    except Exception as e:
        # Log any exceptions for debugging
        logging.error(f'An error occurred: {str(e)}')
        return jsonify({'error': 'An error occurred'}), 500

@app.route('/result')
def result_page():
    return render_template('result.html', result = str(result))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4000)
