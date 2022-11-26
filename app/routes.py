from datetime import datetime
from flask import render_template_string, request, render_template, redirect, session, jsonify, flash, send_file
from app import app, db
from app.db import Menu, Dishes

from app import modules 

@app.route("/")
@app.route("/home")
def home():
    result = Menu.query.all()

    return render_template("index.html", menus = result)

@app.route("/menu")
def menu():
    menu_id = request.args.get('menuid')
    week_commencing = request.args.get("wdc")

    result = modules.dish_format(Dishes.query.filter_by(Menu = menu_id).all())
    result = modules.order_query_by_date(result)
    modules.show_current_weeks_dishes(result)
    
    return render_template("menu.html", dishes = result)

@app.route("/menu/menu-planner")
def menu_planner():

    menu_id = request.args.get('menuid')
    week_commencing = request.args.get("wdc")

    if week_commencing == "none":
        return redirect(modules.menu_planner_url_format(menu_id))

    result = Dishes.query.filter_by(Menu = menu_id).all()
    
    return render_template("menu-planner.html", dishes = result)

@app.route("/db")
def db():
    result = Menu.query.all()
    print(result[0])
    return "hi"