from flask import Flask, render_template
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
    term = request.form['key']
    return "search for " + term


if __name__ == "__main__":
    app.run('127.0.0.1')

