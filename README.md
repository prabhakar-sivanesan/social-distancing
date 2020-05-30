# Social Distancing
## Description
Application to monitor social distancing between people in public places using the video feed from Survillence or Security cameras.
Many countries have mandated social distancing as a rule that people should follow while they are out in public places amidst the COVID-19 situation. So this application will help government agencies and private organizations to monitor how safe is their place at the current given time.

This application gets a live video feed from the camera or a recorded video file as an input and carry out the below steps,
  - Detect people using SSD Mobilenet model trained on COCO dataset.
  - Calculate the pixel distance between each person
  - Highlight them if they cross the safe threshold distance

## Installation
Install neccessary python packages
```
numpy==1.18.2
requests==2.18.4
tensorflow==1.15.2
opencv_python==4.1.2.30
```
Use this command to install all package at once
```
pip install requirements.txt 
```
