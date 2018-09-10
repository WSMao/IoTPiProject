#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from flask import Flask,render_template,jsonify
import os

app=Flask(__name__)

@app.route('/')
def index():
    return " it's my main page "

@app.route('/control')
def control():
    return render_template("control.html")


@app.route('/test')
def test():
    os.system("touch ~/Desktop/12345.txt")
    return jsonify ( result = 3)


if __name__=="__main__":
    app.run(debug=True)
 
