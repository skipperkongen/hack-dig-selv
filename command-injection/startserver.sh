#!/bin/sh
export FLASK_APP=server.py
flask run --port=8082  # brug denne for at køre mere sikkert
#flask run --host=0.0.0.0 --port=8082
