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
        kommando = 'cal {}'.format(year)
        kommando_output = os.popen(kommando).read()
        output = 'Jeg kørte unix-kommandoen:\n> {}\n\nUdskrift fra systemet:\n\n{}'.format(
            kommando,
            kommando_output
        )
        return Response(output, mimetype='text/plain')
    elif request.method == 'GET':
        if os.path.isfile('KILROY'):
            return render_template('hacked.html')
        else:
            return render_template('form.html')
