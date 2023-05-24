from flask import Flask, render_template, request, jsonify, redirect, session
import requests
from flask_cors import CORS
from chat import get_response
import os

app = Flask(__name__)
CORS(app)


@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    response = get_response(text)
    message={"answer":response}
    return jsonify(message)

@app.get("/")
def index_get():
    return render_template("base.html")
if __name__ == "__main__":
    app.run(debug=True)