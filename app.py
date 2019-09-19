# encoding: utf-8

#import datetime
from flask import Flask, render_template, request, redirect, url_for, flash
from flask import jsonify
from flask import abort, g

# to fix IO Error Broken Pipe
#from signal import signal, SIGPIPE, SIG_DFL
#signal(SIGPIPE,SIG_DFL) # no funciono porque en ves de darme el error apaga el servidor, al menos el local

APPLICATION_NAME = "Solotugracia"

app = Flask(__name__)

@app.route('/')
def showMain():
       return redirect('/videos')

@app.route('/videos')
def showVideos():
       """ Muestra pagina principal de videos"""
       return render_template(
              'videos.html')

if __name__ == '__main__':
    app.secret_key = '88040422507vryyo'
    app.debug = True
    app.run(host='0.0.0.0', port=8000) # app.run(threaded=True) tampoco sirvio para arreglar broken Pipe