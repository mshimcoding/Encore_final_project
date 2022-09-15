import cv2
from run_model import loaded_model

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        ret, frame = self.video.read()

        # DO WHAT YOU WANT WITH TENSORFLOW / KERAS AND OPENCV

        # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        result = loaded_model(frame)

        ret, jpeg = cv2.imencode('.jpg', result)

        return jpeg.tobytes()

