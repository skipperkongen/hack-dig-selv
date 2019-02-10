#!/usr/bin/python3
from __future__ import print_function
from flask import Flask, render_template, request, Response

import os
app = Flask(__name__)

@app.route('/', methods=('GET', 'POST'))
def systemkald():
    if request.method == 'POST':
        year = request.form['year']
        # Serious vulnerability!!!! execute unsanitised commands
        output = os.popen('cal {}'.format(year)).read()
        return Response(output, mimetype='text/plain')
    elif request.method == 'GET':
        return render_template('form.html')
