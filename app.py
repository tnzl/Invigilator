
from flask import Flask, render_template, Response
import cv2
from invigilator.invigilator import Invigilator
from invigilator.utils import preprocess_img

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self, proctor):
        ret, frame = self.video.read()

        warnings, dets = proctor.give_image(frame)

        img_fd = preprocess_img(frame)

        if warnings is None:
            ret, jpeg = cv2.imencode('.jpg', img_fd)
            return jpeg.tobytes()

        if len(warnings)>0:
            color = (0,0,255)
        else:
            color = (0,255,0)

        for i in range(len(dets)):
            cv2.rectangle(img_fd, (dets[i]['box'][0], dets[0]['box'][1]), (dets[0]['box'][0]+dets[0]['box'][2], dets[0]['box'][1]+dets[0]['box'][3]), color , 1)
            cv2.circle(img_fd ,(dets[i]['keypoints']['left_eye'][0], dets[0]['keypoints']['left_eye'][1]), 3, (0,0,255), thickness=-1)
            cv2.circle(img_fd ,(dets[i]['keypoints']['right_eye'][0], dets[0]['keypoints']['right_eye'][1]), 3, (0,0,255), thickness=-1)
            cv2.circle(img_fd ,(dets[i]['keypoints']['nose'][0], dets[0]['keypoints']['nose'][1]), 3, (0,0,255), thickness=-1)
            cv2.circle(img_fd ,(dets[i]['keypoints']['mouth_left'][0], dets[0]['keypoints']['mouth_left'][1]), 3, (0,0,255), thickness=-1)
            cv2.circle(img_fd ,(dets[i]['keypoints']['mouth_right'][0], dets[0]['keypoints']['mouth_right'][1]), 3, (0,0,255), thickness=-1)
            img_fd = cv2.putText(img_fd
                                , 'pitch:' + "{:.2f}".format(dets[i]['pitch'])
                                , (dets[0]['box'][0]+dets[0]['box'][2]+5, dets[0]['box'][1]+8)
                                , cv2.FONT_HERSHEY_SIMPLEX
                                , 0.5
                                , color
                                , 1
                                , cv2.LINE_AA)
        
        ret, jpeg = cv2.imencode('.jpg', img_fd)
        return jpeg.tobytes()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera, proctor):
    while True:
        frame = camera.get_frame(proctor)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera(), Invigilator()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
