import json
from flask import Flask
from flask import render_template

app = Flask(__name__)

#read data from json
def read_json_file(filepath):
	jsonfile = open(filepath, 'r+')
	jsontext = jsonfile.read()
	data = json.loads(jsontext, strict = False)
	jsonfile.close()
	return data

@app.route('/')
def index():
	#read data from json
	data = read_json_file('static/data/index.json')

	return render_template('index.html', data=data)

@app.route('/details/<string:student_number>')
def details(student_number):
	data = read_json_file('static/data/index.json')
	user_data = {}
	for item in data:
		if student_number == item['student_number']:
			user_data = item
	return render_template(student_number + '.html', data=user_data)

@app.route('/details/<string:student_number>_self_info')
def self_intro(student_number):
	data = read_json_file('static/data/index.json')
	user_data = {}
	for item in data:
		if student_number == item['student_number']:
			user_data = item
			break
	return render_template(student_number + '-infopage.html', data=user_data)


if __name__ == '__main__':
	app.run(debug = True)


