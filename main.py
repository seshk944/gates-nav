# import cv2
# import numpy as np
import math
import heapq

# GATES NAV APP

# image_path = "path/to/your/image.jpg" # path file to user's image
# image = cv2.imread(image_path, cv2.IMREAD_COLOR) # loads image in RBG color
# https://www.geeksforgeeks.org/python-opencv-cv2-imshow-method/
# https://realpython.com/python-heapq-module/


# fifth floor map
map = """
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
X..........................................
X.........X....X....X....X....X....X....XXX
X....XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX....XXX
X....X..............................X....X
X....X....X....X....X....X....X....X....X
X....X....X....X....X....X....X....X....X
X....X..............................X....X
X....X....X....X....X....X....X....X....X
X....XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX....XXX
X....X..............................X....X
X....X....X....X....X....X....X....X....X
X....X....X....X....X....X....X....X....X
X...XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
"""

def parse_map(map):
    lines = map.splitlines()
    origin = 0, 0
    destination = len(lines[-1]) - 1, len(lines) - 1
    return lines, origin, destination

def is_valid(lines, position):
    x, y = position
    if not (0 <= y < len(lines) and 0 <= x < len(lines[y])):
        return False
    if lines[y][x] == "X":
        return False
    return True

def get_neighbors(lines, current):
    x, y = current
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            position = x + dx, y + dy
            if is_valid(lines, position):
                yield position

def get_shorter_paths(tentative, positions, through):
    path = tentative[through] + [through]
    for position in positions:
        if position in tentative and len(tentative[position]) <= len(path):
            continue
        yield position, path


# those are all helper functions above it
def find_path(map):
    lines, origin, destination = parse_map(map)
    tentative = {origin: []}
    candidates = [(0, origin)]
    certain = set()
    while destination not in certain and len(candidates) > 0:
        _ignored, current = heapq.heappop(candidates)
        if current in certain:
            continue
        certain.add(current)
        neighbors = set(get_neighbors(lines, current)) - certain
        shorter = get_shorter_paths(tentative, neighbors, current)
        for neighbor, path in shorter:
            tentative[neighbor] = path
            heapq.heappush(candidates, (len(path), neighbor))
    if destination in tentative:
        return tentative[destination] + [destination]
    else:
        raise ValueError("no path")

def show_path(path, map):
    lines = map.splitlines()
    for x, y in path:
        lines[y] = lines[y][:x] + "@" + lines[y][x + 1 :]
    return "\n".join(lines) + "\n"


path = find_path(map)
print(show_path(path, map))


####################################################################################################################

# process video, frame by frame --> compare each frame to user's image
# cam = cv2.VideoCapture('video url')
# if not cap.isOpened():
#     print('Error')
#  while cap.isOpened():
#     ret, frame = cap.read
#     if ret:
#         cv2.imshow('Frame', frame)

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