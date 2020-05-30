#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 21:28:28 2020

@author: the-transfer-learning-guy
"""

import cv2
import time
import argparse
import numpy as np
import tensorflow as tf

ap = argparse.ArgumentParser()
ap.add_argument("-t", "--minThresh", required=True, default=0,
	help="min threshold for person detection")
ap.add_argument("-x", "--x", required=True,
	help="pixel distance in X axis")
ap.add_argument("-y", "--y", required=True,
	help="pixel distance in Y axis")
ap.add_argument("-i", "--input", required=True,
	help="path to input video")
ap.add_argument("-m", "--model", required=False, default="saved_model/",
	help="path to model")
args = vars(ap.parse_args())

cv2.namedWindow("Display", cv2.WINDOW_NORMAL)
#cv2.namedWindow("Result", cv2.WINDOW_NORMAL)

def main():
    video_path = args["input"]
    model_path = args["model"]
    threshold = int(args["minThresh"])
    x = int(args["x"])
    y = int(args["y"])
    cap = cv2.VideoCapture(video_path)
    with tf.Session(graph = tf.Graph()) as sess:
        tf.saved_model.loader.load(sess, ['serve'], model_path)
        graph = tf.get_default_graph()
        
        input_tensor = graph.get_tensor_by_name("image_tensor:0")
        
        det_score = graph.get_tensor_by_name("detection_scores:0")
        det_class = graph.get_tensor_by_name("detection_classes:0")
        det_boxes = graph.get_tensor_by_name("detection_boxes:0")
        det_numbs = graph.get_tensor_by_name("num_detections:0")
        
        while True:
            start_time = time.time()
            ret, image = cap.read()
            center_list=[]
            if not ret:
                break
            image = cv2.resize(image, (640,480), interpolation = cv2.INTER_AREA)
            height, width, ch = image.shape
            #sub_zero = np.zeros(image.shape, dtype = "uint8")
            img_expanded = np.expand_dims(image, axis=0)
            
            score,classes,boxes,nums_det = sess.run([det_score, det_class, 
                                                     det_boxes, det_numbs], 
                                                     feed_dict={input_tensor:img_expanded})
            
            for i in range (int(nums_det[0])):
                draw = ()
                if(classes[0][i] == 1):
                    if(score[0][i]*100 >= threshold):
                        #print(score[0][i]*100)
                        per_box = boxes[0][i]
                        y1 = int(per_box[0]*height)
                        x1 = int(per_box[1]*width)
                        y2 = int(per_box[2]*height)
                        x2 = int(per_box[3]*width)
                        if not ((x2-x1)*(y2-y1) < 100000 ):
                            continue
                        p1 = (x1,y1)
                        p2 = (x2,y2)
                        center = (int((x1+x2)/2), int((y1+y2)/2))
                        for c in center_list:
                            
                            if(abs(center[0] - c[0][0]) < x and abs(center[1] - c[0][1]) < y and len(center_list) > 1):
                                cv2.line(image, center, c[0], (0,0,255), 2)
                                #cv2.line(sub_zero, center, c[0], (0,0,255), 2)
                                cv2.rectangle(image, c[1], c[2], (0,0,255), 2)
                                #cv2.rectangle(sub_zero, c[1],c[2], (0,0,255), 2)
                                draw = (p1, p2)
                            else:        
                                cv2.rectangle(image, p1, p2, (0,255,0), 2)
                                #cv2.rectangle(sub_zero, p1,p2, (0,255,0), 2)
                            if(len(draw)>1):
                                cv2.rectangle(image, draw[0], draw[1], (0,0,255), 2)
                                #cv2.rectangle(sub_zero, draw[0], draw[1], (0,0,255), 2)
                        center_list.append((center,p1,p2))
            #cv2.imshow("Result", sub_zero)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            cv2.imshow("Display", image)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()