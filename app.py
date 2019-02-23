#!/usr/local/bin/python3.5
from flask import Flask, render_template, g, jsonify, request

APP = Flask(__name__, template_folder="templates", static_folder="static")

@APP.route("/")
def index():
    return render_template("index.html", test_string = "Index")

@APP.route("/data")
def data():
    return render_template("index.html", test_string = "Data")

@APP.route("/analyitcs")
def analyitics():
    return render_template("index.html", test_string = "Analyitcs")

@APP.route("/analyitcs/individual")
def analyitcs_individual():
    return render_template("index.html", test_string = "Individual")

@APP.errorhandler(404)
def four_oh_four(error):
    return render_template("index.html", test_string = "404"), 404

if __name__ == "__main__":
    APP.run(host='127.0.0.1', port=8080)
