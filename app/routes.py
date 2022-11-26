from flask import render_template_string, request, render_template, redirect, session, jsonify, flash, send_file
from app import app

from app import modules 

@app.route("/")
@app.route("/home")
def home():

    return render_template("index.html")

@app.route("/menu")
def menu():
    menu_id = request.args.get('menuid')
    week_commencing = request.args.get("wdc")
    print(menu_id, week_commencing)
    return render_template("menu.html")

@app.route("/menu/menu-planner")
def menu_planner():
    
    menu_id = request.args.get('menuid')
    week_commencing = request.args.get("wdc")

    if week_commencing == "none":
        week_num = modules.week_number()
        redirect_url = f"/menu/menu-planner?menuid={menu_id}&wdc={week_num}"
        return redirect(redirect_url)

    print(menu_id, week_commencing)
    return render_template("menu-planner.html")