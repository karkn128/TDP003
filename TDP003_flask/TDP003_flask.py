<<<<<<< HEAD
from flask import Flask, render_template, request
=======
from flask import Flask, render_template
>>>>>>> da3d0df705f447e7bca98a6fc6d27c3de11f5adf
import data
app = Flask(__name__)
app.debug = True

db = data.load("../data.json") 

@app.route("/")
def start():
    return render_template("start_page.html")

@app.route("/list")
def list():
	project_list = []
	for project in db:
		project_list.append(project)
	return render_template("list.html", data=project_list)

@app.route("/project/<id>")
def project(id):
    return render_template("project.html", data=data.get_project(db, int(id)))

@app.route("/techniques")
def techniques():
    return render_template("techniques.html", data=data.get_technique_stats(db))

@app.route("/search", methods=['POST'])
def search():
    search_word = request.form['search_word']
    print(request.form['search_field'])
    return render_template("list.html", data=data.search(db, search=search_word))


if __name__ == "__main__":
    app.run('127.0.0.1')

