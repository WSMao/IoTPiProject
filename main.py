#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask,render_template,jsonify
import os

#video streaming lib
from importlib import import_module
from flask import Response

# import camera driver
if os.environ.get('CAMERA'):
    Camera = import_module('camera_' + os.environ['CAMERA']).Camera
else:
    from camera import Camera
    #from camera_opencv import Camera
# Raspberry Pi camera module (requires picamera package)
# from camera_pi import Camera

from flask import redirect,url_for
from forms import LoginForm
isLogin=False


app=Flask(__name__)
#Set a secret key 
app.config['SECRET_KEY'] = '8fdee849163f9610d482779bc313c968'


@app.route('/')
def index():
    return "it's mao's homepage!"

@app.route('/home')
def home():
    global isLogin
    """Video streaming home page."""
    if isLogin:
        print(isLogin)
        return render_template('home.html')
    else:
        return redirect(url_for('login'))
        
def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/login', methods=['GET','POST'])
def login():
    global isLogin
    form = LoginForm()
    if isLogin:
        isLogin = False
        print(isLogin)
    else:
        print(isLogin)
        if form.validate_on_submit(): #必須定義在 forms.py 的全部都要 valid 
            print('is valid!!!')
            if form.email.data == 'admin@blog.com' and form.password.data == 'password' :
                print('correct')
                isLogin = True
                return redirect(url_for('home'))
    return render_template('login.html',form=form)


#for testing control function 
@app.route('/control')
def control():
    
    return render_template("control.html")

#for testing AJAX !
@app.route('/ajax')
#Server side replies the requests from client side 
def AJAX():
    os.system("touch ~/Desktop/12345.txt")
    return jsonify ( result = 3)



if __name__=="__main__":
    # app.run(debug=True)
    app.run( threaded=True, debug=True)

 




