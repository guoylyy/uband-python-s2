from flask import Flask
from flask import render_template
import json

app = Flask(__name__)

def read_json_file(filepath): #read the list
	jsonfile = open(filepath,'r+')
	jsontext = jsonfile.read()
	data = json.loads(jsontext)
	jsonfile.close()
	return data
	
@app.route('/') # define a route to show the main page
def hello_friends():
	data = read_json_file('static/data/index.json')
	return render_template('index.html',data=data)

@app.route('/details/<string:student_number>') # define a route using student number to show the personal page
def look_details(student_number):
	data = read_json_file('static/data/index.json')
	user_data = {}
	for item in data:
		if student_number == item['student_number']:
			user_data = item
			break
	print user_data
	return render_template('details.html',data=user_data)

@app.route('/details/<string:student_number>/favorite')
def favorite_thing(student_number):
	data = read_json_file('static/data/index.json')
	user_data = {}
	for item in data:
		if student_number == item['student_number']:
			user_data = item
			break
	return render_template('favorite.html',data=user_data)

@app.route('/details/<string:student_number>/current')
def current(student_number):
	data = read_json_file('static/data/index.json')
	user_data = {}
	for item in data:
		if student_number == item['student_number']:
			user_data = item
			break
	return render_template('current.html',data=user_data)

@app.route('/details/<string:student_number>/thoughts')
def thoughts(student_number):
	data = read_json_file('static/data/index.json')
	user_data = {}
	for item in data:
		if student_number == item['student_number']:
			user_data = item
			break
	return render_template('thoughts.html',data=user_data)

if __name__ == '__main__':
	app.run(debug=True)