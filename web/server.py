import logging
from flask import Flask, render_template, request, Blueprint
import data

app = Flask(__name__)
images = Blueprint('images', __name__, template_folder="images")
app.register_blueprint(images)
app.debug = True

@app.route("/")
def start():
	db = data.load("data.json") 
	return render_template("start_page.html", data = enumerate(db))
 

@app.route("/list")
def list():
	db = data.load("data.json") 
	return render_template("list.html", data=[db, data.get_techniques(db)])

@app.route("/project/<int:id>")
def project(id):
	db = data.load("data.json") 
	if data.get_project(db, int(id)) == None:
		return render_template("not_found.html", data=id)
	else:
		return render_template("project.html", data=data.get_project(db, int(id)))

@app.route("/techniques")
def techniques():
	db = data.load("data.json")  
	return render_template("techniques.html", data=data.get_technique_stats(db))

@app.route("/search", methods=['POST'])
def search():
	db = data.load("data.json")

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

@app.errorhandler(404)
def pageNotFound(error):
		return render_template("error404.html", data=error)

if __name__ == "__main__":
	logging.basicConfig(filename='serverlog.log',level=logging.DEBUG)
	app.run('127.0.0.1')
