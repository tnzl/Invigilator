# Invigilator
Invigilator is an artificially intelligent proctor which monitors student activity in real time and generates warnings for using unfair means during exams.

## Demo
Heroku + Flask
See example.py
Under construction

## Installation
`pip` installable.\
Under construction...

## Usage
Usage is as simple as instantiating an Invigilator object and passing image of each frame of video to generate warnings.\
Import and instatiate `Invigilator`.
```
from invigilator.invigilator import Invigilator
proctor = Invigilator()
```
Pass the frame to get warnings and predictions
```
warnings, dets = proctor.give_image(frame)
```

## Contributng
Wiki page

## FAQ
Q1. What are the metric to determine unfair means during exams?\
A1. There are no metric to label action as cheating in offline and online scenarios. An invigilator always issues warnings which if repeated can be marked as cheating. Here, we only generate warnings which makes online exam invigilation much easier for teachers. 

## License
MIT License
Under construction.

## References
Under construction

**END**
