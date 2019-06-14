from app import app
from flask import render_template,request
import math
from sympy import *
import locale
from flaskext.mysql import MySQL

locale.setlocale(locale.LC_ALL,'')



@app.route('/', methods=["POST", "GET"])
def OP():
	if request.method =="POST":
		menu1 = request.form["menu1"]
		menu2 = request.form["menu2"]
		menu3 = request.form["menu3"]

		print menu1


		return render_template("agregarMenu.html")

	return render_template("agregarMenu.html")

# 	return render_template("agregarOP.html")

@app.route('/index')
def index():

    # return render_template("advance-form-element.html")
    return render_template("advance-form-element.html")



	return render_template("trazaOP.html")

@app.route('/tablas')
def tablas():

	return render_template("data-table.html")

	

