#-*- coding: utf-8 -*-
from flask import render_template
from flask import request,redirect,url_for
from app import app
import sys
import json
from quest import parse
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',title='Home')
@app.route('/success/<name>', methods=['POST','GET'])
def success(name):
    file1=str(name)
    filehandle = open(file1, 'r')
    textinput = filehandle.read()
    questions=parse(textinput)
    user = {'username': name}
    return render_template('index.html', title='Next', user=user,questions=questions)
@app.route('/success1/<textinput>', methods=['POST','GET'])
def success1(textinput):
    questions=parse(textinput)
    user = {'username': "divya"}
    return render_template('index.html', title='Next', user=user,questions=questions)
@app.route('/index',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      if(request.form=="form1"):
         user = request.form['fileToUpload']
         return redirect(url_for('success',name = user))
      else:
         user = request.form['fileToUpload']
         return redirect(url_for('success1',textinput = user))
