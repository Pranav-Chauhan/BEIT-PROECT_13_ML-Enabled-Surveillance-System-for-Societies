# TOPIC
ML Enabled Surveillance System for Societies

# GROUP MEMBERS
Pranav Chauhan, Sachin Gupta, Rohit Arava

# BRIEF DESCRIPTION
Many residential societies in India face an impending problem of illegal vehicle parking inside
their societies and theft of the vehicles. This issue is not bounded to just vehicles, but also
adds to other security concerns inside the residential societies. Though there are solutions
that exist in the market for monitoring through cameras and software system but are ex-
pensive and the affordability comes into the question. In this regard, we would like to have
an affordable and innovative solution that caters to the Indian market. Scope of the System
is notifying the vehicle owners about the check-in and check-out of their respective vehicle
into their apartment's. The project will work as a security system for a residential society.
Proper Details of the outsiders will be maintained in the form of an image which will be
stored in the database. If any intruder comes from the boundary wall of the society can be
easily detected and the alarm will on to restrict the intruder.
Our ML Enabled Surveillance System for Societies is based on three modules which are
face detection, vehicle number plate detection and imaginary line/virtual line. The face de-
tection module is used for detecting residential members and non-residential member's faces
in real-time. If a person is detected non-residential, then the person's face will be stored in
the database for future use. Another module is the vehicle number plate detection which
is used for detecting residential and non-residential vehicles number plate in real-time from
live footage. If a vehicle is detected non-residential vehicle, then the vehicle's number plate
is stored in the database for future use. And the last module is the imaginary line/virtual
line module which is placed at the boundary wall of the societies and if any intruder passed
through the imaginary line/virtual line, it will detect the intruder and an alarm will ON
to stop that intruder. If any object like a cat, dog, etc passed through the imaginary
line/virtual line, it will detect the object but no alarm will ON for such objects.And the
imaginary line/virtual line module is also used for counting the number of members which
can be residential or non-residential in real-time.For the face detection module, we have used
the OpenCV library and K-Nearest Neighbors (KNN) classiffer.
OpenCV is a library of programming functions mainly aimed at real-time computer vision. 
Originally developed by Intel, it was later supported by Willow Garage then Itseez. The
library is cross-platform and free for use under the open-source BSD license. And K-Nearest
Neighbors (KNN) is one of the simplest algorithms used in Machine Learning for regression
and classiffcation problems. KNN algorithms use data and classify new data points based
on similarity measures (e.g. distance function).
Classiffcation is done by a majority vote to its neighbors. The data is assigned to the
class which has the nearest neighbors. As you increase the number of nearest neighbors, the
value of k, accuracy might increase. For the vehicle number plate detection module, we have
used the ANPR/ALPR is an open-source Automatic License Plate Recognition library to
perform vehicle number plate recognition. The library analyses images and video streams
to identify license plates. For creating the imaginary line/virtual line we have used python
math function and we have used YOLOv3 model for object detection.YOLO is a clever
convolutional neural network (CNN) for doing object detection in real-time. The algorithm
applies a single neural network to the full image, and then divides the image into regions
and predicts bounding boxes and probabilities for each region.
