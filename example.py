from invigilator.invigilator import Invigilator
import cv2 
import time
from invigilator.utils import preprocess_img
proctor = Invigilator()

cap = cv2.VideoCapture(0)

f = 0
t0 = time.time()
fps = 0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    warnings, dets = proctor.give_image(frame)
    if warnings is None:
        continue
    for warning in warnings:
        print(warning)
        print('Frame : '+str(f))
    
    # To find frame rate
    f+=1
    if f%5 == 0:
        fps = 5/(time.time() - t0)
        t0 = time.time()

    img_fd = preprocess_img(frame)

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
    
    img_fd = cv2.putText(img_fd
                         , 'FPS : '+"{:.2f}".format(fps)
                         , (25, 25)
                         , cv2.FONT_HERSHEY_SIMPLEX
                         , 0.5
                         , (0,255,0)
                         , 1
                         , cv2.LINE_AA)

    cv2.imshow('Landmarks',img_fd)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    f+=1


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()