import json

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ner', methods=['POST'])
def get_named_ents():
    data = request.get_json()
    response = True
    return json.dumps(response)

if __name__ == "__main__":
    app.run(debug = True)

