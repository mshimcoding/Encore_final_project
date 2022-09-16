from flask import Blueprint, render_template, flash, Response
from webcam import VideoCamera
from flask_login import login_required, current_user
from __init__ import create_app, db
from send_email import email_warning

# our main blueprint
main = Blueprint('main', __name__)

video_stream = VideoCamera()

def gen_frames(webcam):  # generate frame by frame from webcam.py
    while True:
        frame = webcam.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@main.route('/') # home page that return 'index'
def index():
    return render_template('index.html')

@main.route('/profile') # profile page that return 'profile'
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@main.route('/email') ## warning email sender
def email():
    email_warning(id=current_user.email)
    return render_template('email_sent.html')



@main.route('/video_feed')
def video_feed():
    #Video streaming route. Put this in the src attribute of an img tag
    return Response(gen_frames(video_stream), mimetype='multipart/x-mixed-replace; boundary=frame')

@main.route('/vid_index')
def vid_index():
    """Video streaming home page."""
    return render_template('vid_index.html')

app = create_app() # we initialize our flask app using the __init__.py function
if __name__ == '__main__':
    db.create_all(app=create_app()) # create the SQLite database
    app.run(debug=True) # run the flask app on debug mode
