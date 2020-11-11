# Invigilator
Invigilator is an artificially intelligent proctor which monitors student activity in real time and generates warnings for using unfair means during exams.

## Demo
A demo app has been deployed on Heroku using Flask and Gunicorn.\
Access it here: [try-invigilator.herokuapp.com](https://try-invigilator.herokuapp.com)(Ahh! Again fixing web host issues -_-) \
OR \
Just run `app.py` \
**Privacy Note:** The app doesn't save any image, video or metadata for any further use. All instances are destroyed as soon as you close the web page. Therefore, please feel free to use the app.

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
Do checkout [example.py](https://github.com/tnzl/Invigilator/blob/master/example.py).

## Contributing
Read Wiki pages to understand the ideas and inspiration behind Invigilator and path we wish to follow for the development of the project.
* [Ideas](https://github.com/tnzl/Invigilator/wiki/Ideas)
* [Path for developers](https://github.com/tnzl/Invigilator/wiki/Path-for-developers)
* [Resources for learning](https://github.com/tnzl/Invigilator/wiki/Resources-for-learning)

## FAQ
Q1. What are the metric to determine unfair means during exams?\
A1. There are no metric to label action as cheating in offline and online scenarios. An invigilator always issues warnings which if repeated can be marked as cheating. Here, we only generate warnings which makes online exam invigilation much easier for teachers. 

## License
[MIT License](https://github.com/tnzl/Invigilator/blob/master/LICENSE)

## References
[References](https://github.com/tnzl/Invigilator/wiki/Resources-for-learning)

**END**
