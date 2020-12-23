#credit: Creating Time Lapse with Python and OpenCV Youtube Video

import os
import numpy as numpy
import cv2
import glob

from datetime import date
import datetime
import time

import tkinter as tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

tk.Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filepath = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(filepath)

#I think I have to specify my file
def create_images(filepath):
    """creates a directory filled with images for source videos"""

    droneFootagePaths = glob.glob(filepath)

    #print(droneFootagePaths)
    
    for path in droneFootagePaths:
        
        cap = cv2.VideoCapture(path)

        name = path[-8:-4]
        print(name)

        #where do I want to save this
        save_path = f"../vid/lapses/{name}.mp4"
        fps = 6.0
        #config = CFEVideoConf(cap, filepath = save_path, res = '1080p')
        out = cv2.VideoWriter(save_path, cv2.VideoWriter_fourcc(*'mp4v'),
        fps, (1920,1080))

        #params for taking timelapse from video
        seconds_duration = 100
        seconds_between_shots = 10
        timelapse_img_dir = f"/Users/wconrad/Desktop/seniorproject/vid/{name}"

        if not os.path.exists(timelapse_img_dir):
            os.mkdir(timelapse_img_dir)

        
        success = 1
        frames = []
        count = 0
        speed = 6
        on = 1
        insertbackimage = 1
        backimage = None

        while success:

            success, image = cap.read()
            if(count % speed == 0 and on == 1):
                frames.append(image)
                if(insertbackimage == 4):
                    frames.append(backimage)
            if(count % speed == 0 and on == 3):
                backimage = image
            if(count % speed == 0):
                on += 1
                if (on == 3):
                    on = 1
            count +=1
            insertbackimage += 1
            if(insertbackimage == 4):
                insertbackimage = 1


        print(len(frames))
        print(frames[len(frames)-1])
        #why is the last frame None?


        frames.pop(len(frames)-1)
        i = 1
        for frame in frames:
            #out.write(frame)
            filename = f"{timelapse_img_dir}/{i}.jpg"
            cv2.imwrite(filename, frame)
            i +=1
            print(i/len(frames)*100)

        out.release()
        
        #when everything is done, release the capture
        cap.release()
    
    return

#when everything is done, release the capture
cv2.destroyAllWindows() 

create_images(filepath)

    


#out.write(frame)
#display image
#cv2.imshow('frame', frame)
#time.sleep(seconds_between_shots)


#clear_images = True

def images_to_video(out, img_dir, clear_images=True):
    #link images together into lapse
    image_list = glob.glob(f"{img_dir}/*.jpg")
    sorted_images = sorted(image_list, key = os.path.getmtime)

    for img_path in sorted_images:
        #print(img_path)
        image_frame = cv2.imread(img_path)
        out.write(image_frame)
    if clear_images:
        for img_path in image_list:
            os.remove(img_path)

    return

