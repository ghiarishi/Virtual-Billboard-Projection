# Virtual-Billboard-Projection

In this repository, I have implemented the concepts of projective geometry and homographies to for projection of an image onto a scene in a natural way that respects perspective. 

In order to demonstrate that, I shall project the University of Pennsylvania logo onto the gial during a football match. For this, I have taken in an input of images from a certain video sequence, 
of a football match, as well as the corners of the goal for each image (using OpenCV). 

I have, for each image in the video sequence, computed the homography between the Penn logo and the goal, and then warped the goal points
onto the ones in the Penn logo to generate a projection of the logo onto the video frame. I have then outputted this into a video. 

Output: 
![result](https://user-images.githubusercontent.com/72302800/201510782-2082b1cc-fcda-4fa0-b64c-dc75d92e1e9d.gif)
