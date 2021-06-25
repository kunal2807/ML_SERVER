from flask import Flask, jsonify, request
import cv2
import numpy as np

app = Flask(__name__)

URL = 'http://192.168.1.3:8080/video'
cap = None


def get_frames():
    global URL, cap
    cap = cv2.VideoCapture(URL)
    while(True):
        _, frame = cap.read()
        if frame is not None:
            cv2.imshow('frame', frame)
        q = cv2.waitKey(1)
        if q == ord("q"):
            break


get_frames()
cv2.destroyAllWindows()
