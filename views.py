from flask import Blueprint, render_template 
import database 

views = Blueprint(__name__, "views")

@views.route("/")
def main():
    return render_template("index.html", planets=database.planets) 

