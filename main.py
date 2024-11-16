import cv2
import numpy as np
import math
import matplotlib
import copy

# GATES NAV APP

image_path = "C:\\Users\\Alexi\\OneDrive\\Downloads\\15-112 Fundamentals of Programming and CS\\vidSS.png" # path file to user's image
image = cv2.imread(image_path, cv2.IMREAD_COLOR) # loads image in RBG color
# https://www.geeksforgeeks.org/python-opencv-cv2-imshow-method/
# https://realpython.com/python-heapq-module/


####################################################################################################################

# process video, frame by frame --> compare each frame to user's image
vidURL = "C:\\Users\\Alexi\\OneDrive\\Downloads\\15-112 Fundamentals of Programming and CS\\hack112TestVid.MOV"

def referenceVidFrames(vidURL, image):
    video = cv2.VideoCapture(vidURL)
    print(video)
    referenceFrames = []
    bestMatch = 0
    bestFrame = None

    while True: # loop through the frames and compare them to the user input image
        ret, frame = video.read()
        if not ret:
            break
        referenceFrames.append(frame)

        template = image.copy() #comparing against this pic
        result = cv2.matchTemplate(frame, template, cv2.TM_CCOEFF_NORMED) # normalized cross correllation between the template and current frame
        # crossCorrelation = (result[0][0])
        rows, cols = len(result), len(result[0])
        sum = 0
        for row in range(rows):
            for col in range(cols):
                sum += result[row][col]
        
        if sum > bestMatch:
            bestMatch = sum
            bestFrame = frame

        # if (result[0][0]).all() > bestMatch: # get the highest correlation
        #     bestMatch = result

    print(bestMatch, bestFrame)
    # print("Match Score:", result[0][0])

    # video.release()
    # return referenceFrames

referenceVidFrames(vidURL, image)
# video_frames = {some function that returns all the frames in a list or something}

# for frame in video_frames:
    

#Priority list 
#   1) Learn how to use OpenCV
#   2) Draft up photo comparison feature and test
#   3) Create floor map 
#   4) Draft up path finder feature and test
#   5) go to sleep 

# create superclass (GHC)
    # create subclasses (floors)
    # start and end point initialized for each floor
    #   find point closest to photo and make that your start point
    #   lets start off with end point being outside and then we can 
    #   change it to a specificed point later

    # OpenCV just used to identi

# database of landmarks 
    # specific landmarks 
    # training your model (takes a long time)
        # collect own data (take pictures)
        # take pictures from several angles and do image augmuntation (? how do you spell)
            # all these images are level X
            # outside models that take pics, train, and predict

# take a bunch of pictures -> compare user's photo to database of pictures
    # normalized cross correlation
    # loop through our dataset
    # cv2.videocapture

    # https://www.educative.io/answers/template-matching-opencv 