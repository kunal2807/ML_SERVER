from flask import Flask, redirect, url_for, request, render_template
import cv2
import numpy as np
import os

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@app.route('/predict/face', methods=['GET', 'POST'])
def upload():
    stream = 'http://192.168.1.3:8080/video'  # or the uploaded file
    cap = cv2.VideoCapture(stream)
    while(True):
        _, frame = cap.read()
        if frame is not None:
            # manuplate frame accordigly like calling the model or something like that
            # after that simply return response
            cv2.imshow('frame', frame)
        q = cv2.waitKey(1)
        if q == ord("q"):
            break


if __name__ == '__main__':
    app.run(debug=True, port=5001)
    print('Model loaded. Check http://127.0.0.1:5001')
