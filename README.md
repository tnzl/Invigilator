# Invigilator
---------------
Invigilator is an artificially intelligent proctor which monitors student activity in real time and generates warnings for using unfair means during exams.

## Demo
-------
Azure+Flask demo.\
See example.py
Under construction

## Installation
---------------
`pip` installable.\
Under construction...

## Usage
---------
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
--------------
Wiki page

## License
----------
MIT License
Under construction.

## References
--------------
Under construction
END

