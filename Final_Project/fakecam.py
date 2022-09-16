import cv2
## from run_model import loaded_model

class VideoCamera2(object):
    def __init__(self):
        self.video = cv2.VideoCapture('fake_avi.mp4')

    def __del__(self):
        self.video.release()

    def get_frame(self):
        ret, frame = self.video.read()

        ret, jpeg = cv2.imencode('.jpg', frame)
        cv2.waitKey(10)

        return jpeg.tobytes()
