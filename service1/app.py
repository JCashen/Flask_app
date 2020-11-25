from flask import Flask, render_template 
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    #gets animal
    animal = requests.get("http://service-2:5001/animal")
    #gets noise
    noise = requests.post("http://service-3:5002/noise", data=animal.text)
    #get name
    name = requests.get("http://service-4:5003/name")


    return render_template('index.html', animal=animal.text, noise=noise.text, name=name.text)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')