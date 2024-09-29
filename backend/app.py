from flask import Flask
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/api/environment', methods=['GET'])
def get_environment_data():
    return{"message": "Hello from Flask!"}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
