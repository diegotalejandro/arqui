from app import app
from flask import render_template,request
import math
#from sympy import *
import locale
#from flaskext.mysql import MySQL

locale.setlocale(locale.LC_ALL,'en_US.utf-8')



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


@app.route('/tablas')
def tablas():

	return render_template("data-table.html")

@app.route('/ventasdiarias')
def ventasdiarias():
	nretiro = 45
	vretiro = 45000
	vretiro = locale.currency(vretiro, grouping = true).replace(',','.')
	ndespacho = 50
	vdespacho = 50000
	vdespacho = locale.currency(vdespacho, grouping = true).replace(',','.')

	return render_template("ventasdiarias.html", nretiro = nretiro, vretiro = vretiro, ndespacho = ndespacho, vdespacho = vdespacho)

@app.route('/ventasmensual')
def ventasmensual():
	nretiro = 45
	vretiro = 45000
	vretiro = locale.currency(vretiro, grouping = true).replace(',','.')
	ndespacho = 50
	vdespacho = 50000
	vdespacho = locale.currency(vdespacho, grouping = true).replace(',','.')

	return render_template("ventasmensual.html", nretiro = nretiro, vretiro = vretiro, ndespacho = ndespacho, vdespacho = vdespacho)

@app.route('/ventaretiro')
def ventaretiro():
	nretiro = 45

	return render_template("ventaretiro.html", nretiro = nretiro)
