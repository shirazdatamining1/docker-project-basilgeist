from flask import Flask, jsonify
import secrets

app = Flask(__name__)

@app.route('/')
def home():

    random_number = secrets.randbelow(1000)
    return jsonify({"secure_random_number": random_number})

if __name__ == "__main__":

    app.run(host='0.0.0.0', port=8080)
