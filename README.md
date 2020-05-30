# Social Distancing
## Description
Application to monitor social distancing between people in public places using the video feed from Survillence or Security cameras.
Many countries have mandated social distancing as a rule that people should follow while they are out in public places amidst the COVID-19 situation. So this application will help government agencies and private organizations to monitor how safe is their place at the current given time.

This application gets a live video feed from the camera or a recorded video file as an input and carry out the below steps,
  - Detect people using SSD Mobilenet model trained on COCO dataset.
  - Calculate the pixel distance between each person
  - Highlight them if they cross the safe threshold distance

## Installation
List of neccessary python packages to run this application
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
## Run the application
Execute this application using the following command,
```
python3 script.py --minThresh 40 --x 10 --y 20 --input input/video.mp4
```
This appllication requires few input data,

  - minThresh - Minimum threshold score to detect person in the video
  - input - File path to the input video or Camera ID
  - x - Pixel difference in X axis
  - y - Pixel difference in Y axis
