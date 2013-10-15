
from flask import Flask, render_template, request

import data
app = Flask(__name__)
app.debug = True

db = data.load("../data.json") 

@app.route("/")
def start():
 
    return render_template("start_page.html", data = enumerate(db))

@app.route("/list")
def list():
	return render_template("list.html", data=db)

@app.route("/project/<id>")
def project(id):
    return render_template("project.html", data=data.get_project(db, int(id)))

@app.route("/techniques")
def techniques():
    return render_template("techniques.html", data=data.get_technique_stats(db))

@app.route("/search", methods=['POST'])
def search():
    search_word = request.form["search_word"]
    fields = request.form.getlist("field_checkbox") #Returns a list of values of all checked field_checkboxes
    print(fields)

    return render_template("list.html", data=data.search(db, search=search_word, search_fields=fields))


if __name__ == "__main__":
    app.run('127.0.0.1')

