HACK112 PROJECT IDEA

This application (on a larger level), would be able to take in a user-provided image of where in the building/where
on campus they currently are, and can return a map of the floor explaining fastest routes to nearest exits/cafes/
restrooms/study areas. This would be done by

a. using template matching with openCV to compare images and determine where in the building/zone they are
b. this establishes a starting point on the floor, which is passed to the a* search algorithm function
c. this search algorithm can quickly find the fastest path to the nearest desired locations (which can also be
    provided by user input i.e. a dropdown menu)

resources:
https://maps.scottylabs.org/GHC-5 