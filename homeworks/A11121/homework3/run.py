# -*- coding: utf-8 -*-
from flask import Flask
from flask_wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import Required
from flask import render_template
import json
import time
import codecs
import os
from flask import request,redirect

app = Flask(__name__)
# 加载配置文件
app.config.from_object('config')

# 初始化form
class MockCreate(Form):
	note = StringField("note",[Required()])
	student = StringField("student",[Required()])
	submit = SubmitField("Submit")

# 读取留言文件信息
def read_note_txt(file_path):
	BASE_DIR = os.path.dirname(__file__)
	nfile = codecs.open(file_path, 'r', 'utf-8')
	lines=nfile.readlines()
	datas=[]
	for line in lines:
		line = line.strip()
		data = line.split(",")
		datas.append(data)
	return datas
	nfile.close()

def read_json_file(filepath):
	file=open(filepath,"r+")
	file_text=file.read()
	data=json.loads(file_text)
	return data

@app.route('/')
def index():
	BASE_DIR = os.path.dirname(__file__)
	data=read_json_file(BASE_DIR+'/static/data/index.json')
	return render_template('index.html',data=data)


# 获取页面传过来的留言信息，写入文件并且返回首页
@app.route("/notes",methods=['GET','POST'])
def MockController():
	form = MockCreate()
	note = form.note.data
	student=form.student.data
	now=time.strftime("%Y-%m-%d", time.localtime())
	data = {}
	BASE_DIR = os.path.dirname(__file__)
	data["note_time"] =now
	data["note"] =note
	file_path=BASE_DIR+'/static/data/'+student+'.txt'
	nfile = codecs.open(file_path, 'a+', 'utf-8')
	nfile.write("%s,%s\n" % (data["note"], data["note_time"]))
	note=request.url_root
	return redirect(note+'details/'+student)


@app.route('/details/<string:student_number>')
def details(student_number):
	BASE_DIR = os.path.dirname(__file__)
	data=read_json_file(BASE_DIR+'/static/data/index.json')
	user_data={}
	for item in data:
		if student_number==item['student_number']:
			file_path = BASE_DIR + '/static/data/' + item['student_number'] + '.txt'
			notes = read_note_txt(file_path)
			user_data=item
			break
	data = read_json_file(BASE_DIR + '/static/data/project.json')
	pro_data = []
	for item in data:
		if student_number==item['student_number']:
			pro_data=item["project_info"]
			break
	return render_template('details.html',data=user_data,note=notes,pro_data=pro_data)

# 跳转至项目信息页面
@app.route('/<string:student_number>/project/<int:number>')
def project(student_number,number):
	BASE_DIR = os.path.dirname(__file__)
	data = read_json_file(BASE_DIR + '/static/data/project.json')
	project_data = {}
	per_data={}
	for item in data:
		if student_number == item['student_number']:
			project_data["project"]=item["project"][number]
			per_data=item
			break
	return render_template('essay.html',data=per_data,pro_data=project_data)





if __name__ == '__main__':
    app.run(debug=True)