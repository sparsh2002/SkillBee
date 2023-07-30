from flask import Flask, render_template, jsonify , request
import requests

app = Flask(__name__)

@app.route('/' , methods=['GET'])
def index():
    if request.method=='GET':
        try:
            # Replace 'https://jsonplaceholder.typicode.com/posts/1' with the actual URL you want to request
            response = requests.get('https://www.boredapi.com/api/activity?participants=1')

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Parse the JSON response content and return it
                data = response.json()
                return render_template('index.html' , data=data)
            else:
                # If the request was not successful, return an error message
                return jsonify({'error': 'Failed to fetch data'}), 500

        except requests.RequestException as e:
            # Handle any exceptions that might occur during the request
            return jsonify({'error': 'An error occurred during the request'}), 500

if __name__ == '__main__':
    app.run(debug=True)
