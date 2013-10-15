
from flask import Flask, render_template, request

import data
app = Flask(__name__)
app.debug = True

@app.route("/")
def start():
<<<<<<< HEAD
	db = data.load("../data.json") 
	return render_template("start_page.html", data = enumerate(db))
=======
 
    return render_template("start_page.html", data = enumerate(db))
>>>>>>> 0b892f66384c75a39349d54fe5e8eef01a4050e0

@app.route("/list")
def list():
	db = data.load("../data.json") 
	return render_template("list.html", data=[db, data.get_techniques(db)])

@app.route("/project/<id>")
def project(id):
	db = data.load("../data.json") 
	return render_template("project.html", data=data.get_project(db, int(id)))

@app.route("/techniques")
def techniques():
	db = data.load("../data.json") 
	return render_template("techniques.html", data=data.get_technique_stats(db))

@app.route("/search", methods=['POST'])
def search():
	db = data.load("../data.json") 
	if request.form["search_word"] == "":
		search_word = None
	else:
		search_word = request.form["search_word"]

	fields = request.form.getlist("field_checkbox") #List of all checked search_fields
	techniques = request.form.getlist("technique_checkbox") #List of all checked techniques
	sort_order = request.form.get("sort_order")
	sort_by = request.form.get("sort_by")

	data_search = data.search(db, search=search_word, search_fields=fields, techniques=techniques, sort_order=sort_order, sort_by=sort_by)
	return render_template("list.html", data=[data_search, data.get_techniques(db)])


if __name__ == "__main__":
    app.run('127.0.0.1')

