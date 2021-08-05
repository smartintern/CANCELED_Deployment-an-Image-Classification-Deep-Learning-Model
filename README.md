# misclassification
## Project Name: Misclassification 

## What's the problem?
The camera classifies the image incorrectly when classifying it.

## How are images obtained?
Cameras are installed at the facility. The cameras shoot the product from 8 different angles. According to the captured image, the camera gives a result.

## Where is the wrong place?
The most difficult error the camera encounters when grading is the loose wire. So the error is happening on the camera

## Why is there a possibility of misclassification?
Due to the burrs found in the coils, the camera can classify it as loose wire even though there is no loose wire in the image. This is why the camera can misclassify.

## What solution should be implemented?
Images that the camera classifies as loose wire are collected in a pool. Most images in the pool actually turn out to be acceptable burrs. We use deep learning to find out if the images in this repository are faulty. We support the camera with deep learning.
