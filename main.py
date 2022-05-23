#!usr/bin/python
#import libraries

import numpy as np
import cv2
#from moviepy.editor import VideoFileClip
import pipeline
import globals
import sys

globals.init()
deb=input("please enter 0 for final result, 1 for debugging mode\n")
deb=int(deb)
#selecting debugging or not
workMode=input("please enter 0 for photo, 1 for video\n")
workMode=int(workMode)
#selecting work mode photo=1 or video=0


if workMode ==1:
    locationVideo=input("please enter the complete path of the video\n")

    cap=cv2.VideoCapture(locationVideo)

    while(cap.isOpened()):
        ret,frame=cap.read()
        if ret==1:
            out_frame=pipeline.lane_finding_pipeline(frame,deb)

            cv2.imshow("output",out_frame)
            if cv2.waitKey(10)==27:
             break
        else:
            print("Video has been Produced")
            break

    cap.release()
    #out.release()
    cv2.destroyAllWindows()

elif workMode ==0:
    locationPhoto=input("please enter the complete path of the photo\n")


    in_photo=cv2.imread(locationPhoto)
    out_photo=pipeline.lane_finding_pipeline(in_photo,deb)
    cv2.imshow("output",out_photo)
    cv2.waitKey(0)




