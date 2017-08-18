from flask import Flask
from flask import render_template
import json

app = Flask(__name__)

#def number(student_number):
#	folder = "static/json"
#	file =open(folder+"/"+str(student_number)+'.json',"r+")
#	text = file.read()
#	text = dict(json.loads(text))
#	return text


def read():
	file =open("static/json/index.json","r+")
	text = file.read()
	text = json.loads(text)
	file.close()
	return text

@app.route('/')
def homepage():
	text = read()
	return render_template('index.html', data = text)

@app.route('/<string:student_number>/'+'details/page1')
def intro(student_number):
	text = read()
	data = {}
	for i in text:
		if i["num"] == student_number:
			data = i
			break
	return render_template("page1.html",data=data)

@app.route('/<string:student_number>/'+'details/page2')
def page2(student_number):
	text = read()
	data = {}
	for i in text:
		if i["num"] == student_number:
			data = i
			break
	return render_template("page2.html",data=data)


@app.route('/<string:student_number>/'+'details/page3')
def page3(student_number):
	text = read()
	data = {}
	for i in text:
		if i["num"] == student_number:
			data = i
			break
	return render_template("page3.html",data=data)


@app.route('/<string:student_number>/'+'details/page4')
def page4(student_number):
	text = read()
	data = {}
	for i in text:
		if i["num"] == student_number:
			data = i
			break
	return render_template("page4.html",data=data)


if __name__ == '__main__':
    app.run(debug=True)
