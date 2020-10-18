# Invigilator
This project aims at detecting cheating during online exams with help of deep learning algorithms on video stream.

## Stage : 1
Basic left/right model\
          v\
Create a repo \
          v\
Deploy on cloud\
          v\
Start writing medium article \
          v\
Make a demo video\
## Stage : 2
Add more complex tasks like face id\
v\
Start with your own efficient model\
          


# Path ahead:
Level 1:\
  A. Create a basic left right working python package.\
  B. Use third party trained models and libraries.\
  C. Have basic demo, try scripts and deployment.\
Level 2:\
  A. Start adding more complex tasks to invigilator.\
  B. Start removing third party libraries.\
  C. Improve pipelines aiming FPS improvement.\
Level 3: \
  A. Independent of third party models aiming FLOPS, accuracy.\
  B. Ready for large scale deployment.\

----------
Aim:
"Predict probability of a person cheating and other related metrics"
[Like this]( https://www.youtube.com/watch?v=-lmc2-podgQ)

Approach:
1. Create a backbone.
2. Predict different tasks.
3. Deploy algorithms to process above predictions to predict different metrics that are indicaative of cheating.

Tasks: 
NN Predictions: 
1. Bounding box 
2. Number of people in image
2. Direction of face, aka gaze = roll + pitch 
3. Gender maybe
4. Person id periodically

Product outputs:
1. anti spoofing 
2. some cheating metrics

Notes:
-7: Search paper with code for all related datasets eg. https://paperswithcode.com/sota/head-pose-estimation-on-biwi
-6: Backbone oriented face angle predictions: https://arxiv.org/pdf/1901.06778v2.pdf
-5: Complete guide on face angles, pose https://www.learnopencv.com/head-pose-estimation-using-opencv-and-dlib/
-4: Roll, Pitch, yaw : https://github.com/fisakhan/Face_Pose/blob/master/pose_detection_retinaface.py
-3: MTCNN vs dlib https://www.youtube.com/watch?v=Yt4TpRmwVPI
-2: Impo- use this probably https://www.youtube.com/watch?v=IZnbd29gtIQ
-1: Facemesh tf js
0: TF js implement.
1. If more than one person appear then save their faces.
2. Person id not on all frames but periodically

Research Papers and Articles:
1. https://machinelearningmastery.com/introduction-to-deep-learning-for-face-recognition/
2. https://arxiv.org/pdf/1804.06655.pdf Complete face recognition book. MANDATORY READ.
2. https://towardsdatascience.com/an-intro-to-deep-learning-for-face-recognition-aa8dfbbc51fb
3. Google about 
  a. Face detection tasks
  b. driver status monitoring system deep learning
  c. Multi task deep learning
4. https://arxiv.org/pdf/1804.06655.pdf
5. Lightweight Driver Monitoring System Based onMulti-Task Mobilenets
6. http://images.nvidia.com/cn/gtc/downloads/pdf/ecs/6%20Deep%20Learning%20for%20Eye%20Tracking(7invensun)%20Thomas%20%5BFinal%20Big%5D10.0.pdf
7. FaceNet 

Youtube, Courses and other important links:
Explore youtube for inspiration.
1. https://www.youtube.com/watch?v=_wuyh37gO-4
2. [VVV IMPORTANT introduction to gaze by opencv](https://www.youtube.com/watch?v=-lmc2-podgQ)
3. [Multitask learning ny Dr. Ng](https://www.youtube.com/watch?v=UdXfsAr4Gjw&feature=youtu.be)
4. [Similar project](https://www.youtube.com/watch?v=YEZMk1P0-yw)
5. [Similar Project](https://www.youtube.com/watch?v=VWUgkcX_KoY)

Datasets:
1. MS-Celeb-1M: Challenge of Recognizing One Million Celebrities in the Real World
2. https://www.robots.ox.ac.uk/~vgg/data/vgg_face2

END

