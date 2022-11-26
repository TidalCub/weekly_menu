from flask import render_template_string, request, render_template, redirect, session, jsonify, flash, send_file
from app import app


@app.route("/")
@app.route("/home")
def home():

    return render_template("index.html")

@app.route("/menu")
def menu():

    return render_template("menu.html")