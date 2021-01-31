#-*- coding:utf-8 -*-

from flask import Flask
from flask import render_template
import json

app = Flask(__name__)

def read_json_file(filepath):
	jsonfile=open(filepath,'r+')
	jsontext=jsonfile.read()
	data=json.loads(jsontext)
	return data

@app.route('/')
def C4():
	data=read_json_file('static/data/index.json')
	return render_template('index.html',data=data)

@app.route('/details/<student_number>')
def look_details(student_number):
	user_data={}
	data=read_json_file('static/data/index.json')
	for item in data:
		if student_number == item['student_number']:			
			user_data=item
			break
	return render_template('details.html',data=user_data)


@app.route('/details/<string:student_number>/news')
def news(student_number):
	user_data={}
	data=read_json_file('static/data/index.json')
	for item in data:
		if student_number == item['student_number']:			
			user_data=item
			break
	return render_template('news.html',data=user_data)


@app.route('/details/<student_number>/readnote')
def readnote(student_number):
	user_data={}
	data=read_json_file('static/data/index.json')
	for item in data:
		if student_number == item['student_number']:			
			user_data=item
			break
	return render_template('readnote.html',data=user_data)


@app.route('/details/<student_number>/travel')
def trival(student_number):
	user_data={}
	data=read_json_file('static/data/index.json')
	for item in data:
		if student_number == item['student_number']:			
			user_data=item
			break
	return render_template('travel.html',data=user_data)

if __name__ == '__main__':
    app.run(debug=True)