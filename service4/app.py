from flask import Flask, render_template, Response, request
import requests
import random

app = Flask(__name__)

@app.route('/name', methods=['GET'])
def animal():
    names = ["Bill", "Bob", "Steve", "Claire"]
    return Response(random.choices(names), mimetype="text/plain")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5003)