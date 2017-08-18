from flask import Flask
from flask import render_template
import json

app = Flask(__name__)

def read_json_file(filepath):
	jsonfile = open(filepath,'r+',encoding='utf-8')
	jsontext = jsonfile.read()
	data = json.loads(jsontext)
	return data

@app.route('/')
def shouye():
	data = read_json_file('static/data/index.json')
	return render_template('index.html', data=data)

@app.route('/details/<string:student_number>')
def look_details(student_number):
	data = read_json_file('static/data/index.json')
	user_data = {}
	for item in data:
		if student_number == item['student_number'] :
			user_data = item
			break
	return render_template('details.html', data=user_data)

@app.route('/details/<string:student_number>/materials')
def materials(student_number):
	data = read_json_file('static/data/index.json')
	user_data = {}
	for item in data:
		if student_number == item['student_number']:
			user_data = item
			break
	return render_template('materials.html', data= user_data)

@app.route('/details/<string:student_number>/friend')
def friend(student_number):
	data = read_json_file('static/data/index.json')
	user_data = {}
	for item in data:
		if student_number == item['student_number']:
			user_data = item
			break
	return render_template('friend.html', data= user_data)

@app.route('/details/<string:student_number>/hotspot')
def hotspot(student_number):
	data = read_json_file('static/data/index.json')
	user_data = {}
	for item in data:
		if student_number == item['student_number']:
			user_data = item
			break
	return render_template('hotspot.html', data=user_data)

if __name__== '__main__':
	app.run(debug = True)