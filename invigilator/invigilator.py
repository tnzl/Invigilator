from invigilator.utils import preprocess_img, euclidean_dist
from mtcnn import MTCNN
from cv2 import resize

class Invigilator():
    '''
    Generates warnings and other notifications based on predictions by BigBrain

    '''
    def __init__(self):
        self.brain = BigBrain()

    def give_image(self, img):
        preds = self.brain.get_predictions(img)
        if preds == None or len(preds) == 0:
            return None, None
        '''
        Warnings:
        1. More than one person
        2. Pitch, yaw and roll is out of safe limit
        3. FaceID 
        4. Phone is detected in surrounding
        '''
        warnings = []
        if len(preds) > 1:
            warnings.append('More than one person in frame')
        if preds[0]['pitch'] > 10 or preds[0]['pitch'] < -10:
            warnings.append('Facing in wrong direction')
        return warnings, preds

class BigBrain():
    '''
    Detector class does all the backend prediction tasks.

    ...

    Attributes
    ----------
    detector : MTCNN
        Predicts face bounding box, landmarks
    
    Methods
    -------
    pitch(self,det) : 
        predicts pitch based on face landmarks
    
    yaw(self,det) : 
        predicts yaw based on face landmarks
    
    roll(self,det) : 
        predicts roll based on face landmarks

    get_predictions(self, frame) :
        returns all the predictions

    '''
    
    def __init__(self):
        
        self.detector = MTCNN()
        print('Detector online')
        
        
    def pitch(self,det):
        '''
        Here bounding box gives an idea about scale of the face. Therefore dividing l2n-r2n by
        width gives a normalized result.
        Note: In further stages this definition can be improved more.
        '''

        l2n = euclidean_dist(det['keypoints']['left_eye'], det['keypoints']['nose'])
        r2n = euclidean_dist(det['keypoints']['right_eye'], det['keypoints']['nose'])
        return 100 * (l2n - r2n) / det['box'][2]
    
    def yaw(self,det):
        return None
    
    def roll(self,det):
        return None

    def get_predictions(self, frame):
        if frame is None:
            return None
        
        frame = preprocess_img(frame)

        dets = self.detector.detect_faces(frame)
        for i in range(len(dets)):
            dets[i]['pitch'] = self.pitch(dets[i])
            # dets[i]['yaw'] = self.yaw(frame)
            # dets[i]['roll'] = self.roll(frame)

        return dets
            
            