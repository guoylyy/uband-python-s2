#-*-coding:utf-8-*-  

from flask import Flask
from flask import render_template
import json

app = Flask(__name__)

def read_json_files(filepath):
    
    file = open(filepath,'r+')
    file_text = file.read()
    data = json.loads(file_text)
    return data
    


@app.route('/')
def hello_world():
    data = read_json_files('index.json')
    
    return render_template('index.html',data=data)

@app.route('/details/<string:student_number>')
def details(student_number):
    data = read_json_files('index.json')
    for item in data:
      user_data = {}
      if student_number == item['student_number']:
         user_data = item
         break
    return render_template('details.html',data = user_data)

@app.route('/details/<string:student_number>/comments')
def comments(student_number):
    data = read_json_files('index.json')
    for item in data:
      user_data = {}
      if student_number == item['student_number']:
         user_data = item
         break
    return render_template('comments.html',data = user_data)

@app.route('/details/<string:student_number>/my_uband')

def my_uband(student_number):
    data = read_json_files('index.json')
    for item in data:
      user_data = {}
      if student_number == item['student_number']:
         user_data = item
         break
    return render_template('my_uband.html',data = user_data)

@app.route('/details/<string:student_number>/brainstorm')
def brainstorm(student_number):
    data = read_json_files('index.json')
    for item in data:
      user_data = {}
      if student_number == item['student_number']:
         user_data = item
         break
    return render_template('brainstorm.html',data = user_data)

if __name__ == '__main__':
    app.run(debug=True)