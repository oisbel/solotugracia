# encoding: utf-8

#import datetime
from flask import Flask, render_template, request, redirect, url_for, flash
from flask import jsonify
from flask import abort, g

import os
import random

# to fix IO Error Broken Pipe
#from signal import signal, SIGPIPE, SIG_DFL
#signal(SIGPIPE,SIG_DFL) # no funciono porque en ves de darme el error apaga el servidor, al menos el local

APPLICATION_NAME = "Solotugracia"

app = Flask(__name__)
app.secret_key = '88040422507vryyo'

app.static_folder = 'static'


@app.errorhandler(404)
def page_not_found(e):
       return render_template('404.html'), 404

@app.route('/')
def showMain():
	path = 'static/docs/spurgeon'
	try:
		files = os.listdir(path)
	except Exception as e:
		print(e)
		return render_template("index.html")
	files = os.listdir(path)
	if len(files) == 0:
		return render_template("index.html")
	selectedFiles = random.sample(files, 15) 
	files1 = []
	files2 = []
	files3 = []
	filesTuples = []
	for i in range(0,len(selectedFiles)):
		file = selectedFiles[i]
		filesTuples.append((file[:-4].replace('_', ' '),file))
	files1 = filesTuples[0:5]
	files2 = filesTuples[5:10]
	files3 = filesTuples[-5:]
	return render_template('index.html', files1 = files1, files2 = files2, files3 = files3)

@app.route('/spurgeon')
def showSpurgeon():
	""" Muestra pagina principal de videos"""
	path = 'static/docs/spurgeon'
	try:
		files = os.listdir(path)
	except Exception as e:
		print(e)
		return redirect(url_for('showMain'))
	files = os.listdir(path)
	files1 = []
	files2 = []
	for i in range(0,len(files)):
		file = files[i]
		if i % 2:
			files1.append((file[:-4].replace('_', ' '),file))
		else:
			files2.append((file[:-4].replace('_', ' '),file))
	return render_template('spurgeon.html', files1 = files1, files2 = files2)

if __name__ == '__main__':
    app.secret_key = '88040422507vryyo'
    app.debug = True
    app.run(host='0.0.0.0', port=8000) # app.run(threaded=True) tampoco sirvio para arreglar broken Pipe