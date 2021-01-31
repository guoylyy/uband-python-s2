from flask import Flask
from flask import render_template
import json

app = Flask(__name__)

def read_json(filepath):
	jsonfile = open(filepath, 'r+')
	jsontext = jsonfile.read()
	data = json.loads(jsontext)
	jsonfile.close()
	return data

def read_user_data(filepath, student_number):
	data = read_json(filepath)
	user_data ={}
	for item in data:
		if item['student_number'] == student_number:
			user_data = item
			break
	return user_data

@app.route('/')
def hello_world():
	data = read_json('static/data/index.json')
	print data
	return render_template('index.html', data = data)

@app.route('/details/<string:student_number>/home')
def show_details_home(student_number):
	user_data = read_user_data('static/data/index.json', student_number)
	return render_template('/details_home.html', data=user_data)

@app.route('/details/<string:student_number>/art')
def show_details_art(student_number):
	user_data = read_user_data('static/data/index.json', student_number)
	return render_template('/details_art.html', data=user_data)

@app.route('/details/<string:student_number>/eat')
def show_details_eat(student_number):
	user_data = read_user_data('static/data/index.json', student_number)
	return render_template('/details_eat.html', data=user_data)

@app.route('/details/<string:student_number>/study')
def show_details_study(student_number):
	user_data = read_user_data('static/data/index.json', student_number)
	return render_template('/details_study.html', data=user_data)

if __name__ == '__main__':
    app.run(debug=True)