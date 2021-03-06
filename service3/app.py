from flask import Flask, render_template, Response, request 
import requests

app = Flask(__name__)

@app.route('/noise', methods=['POST'])
def noise():
    animal = request.data.decode('utf-8')
    if animal == "Lion":
        noise = "Roar"
    elif animal == "Dog":
        noise = "woof"
    elif animal == "Cat":
        noise = "Meow"
    else: 
        noise = "Moo"
    return Response(noise, mimetype="text/plain")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5002)