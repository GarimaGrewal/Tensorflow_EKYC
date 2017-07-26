##TensorFlow Image Classifier For E-KYC System

This Classifier identifies whether a given ID proof is an aadhar card , Pan Card or a Passport. Its based on the Tensorflow Image Classifier. 

##REQUIREMENTS

* [docker](https://www.docker.com/products/docker-toolbox)
*Tensorflow
*Python

##USAGE

You just need to make a "classifier" directory with a directory "data" inside it with all your images
For example

 [any_path]/my_own_classifier/
 [any_path]/my_own_classifier/data
 [any_path]/my_own_classifier/data/aadhar
 [any_path]/my_own_classifier/data/pancard
 [any_path]/my_own_classifier/data/passport

 and then put your images in it. 
(Images should be in a jpg format strictly)
 This "classifier" directory will have your samples but also trained classifier after execution of "train.sh". 

##TRAIN PROCESS
 
Just type

 ./train.sh [any_path]/my_own_classifier
 
And this will generate 2 files inside the classifier directory , retrained_labels.txt and retrained_graph.pb. 
Now you need to change the paths to that of these 2 files in the label_image.py and classifier.py files.

##GUESS PROCESS

Just go inside the required source directory that has the label_image.py file and the classifier.py file.
You can guess the ID card image by 2 methods :-

1.       python label_image.py /path_to_your_test_image/img.jpg

  This will produce results as: -
pan card (score = 0.98420)
unacceptable id (score = 0.01548)
aadhar (score = 0.00030)
passport (score = 0.00002)
--------time_for_execution-------


2.       python classifier.py /path_to_your_test_image/img.jpg

  This will produce results as: -
pan card (score = 0.98420)
--------time_for_execution-------

The program classifier.py has certain thresholds defined within the program so only if the percentage match of an image with a particular category is more than a specific threshold for that category, only then it will display the result. These threshold values can be changed in the program as per the user requirement.
NOTE:-
THE LINKS TO MY RETRAINED GRAPH AND RETRAINED LABELS FILES ARE AS FOLLOWS:-
https://www.dropbox.com/s/dudqhdkxsf6haks/retrained_graph.pb?dl=0
https://www.dropbox.com/s/o5bhgz4uic0lvox/retrained_labels.txt?dl=0

