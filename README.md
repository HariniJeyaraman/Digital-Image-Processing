# Digital-Image-Processing
Various exercises in DIP 
1) Take a Lena image and convert it into grayscale. 
   Add three different types of noises(salt and pepper, additive Gaussian noise, speckle), 
   each noise in the sets of 5,10,15,20,25,30. Take average for each set and display the average images.
   Report the observation made.
   Observation : Averaging removes noise.
   
2) a) Download Lena image and scale it by factors of 1,2,0.5 using bilinear interpolation and display the scaled images. Also, display the output of built-in functions for doing scaling by factors of 0.5,2. Compare the results.
   b) Download the leaning tower of PISA image and find the angle of inclination using appropriate rotations with bilinear interpolation.
   c) Do histogram equalization on pout-dark and display the same
   d) Do histogram matching(specification) on the pout-dark image, keeping pout-bright as a reference image.
   
 3) 1. Download Lena color image convert it to grayscale image and add salt and  pepper noise with noise quantity 0.1,0.2 upto 1 and generate 10 noisy images.
         a. Do average filtering ( by correlating with average filter ) of varying sizes for each image. Filter size can be 3*3, 5*5, 7*7. (In 3*3 filter all the values are 1/9, in 5*5 filter all the values are 1/25 and in 7*7 filter all the values are 1/49)
         b. Similarly, repeat the question 1.a by replacing the average filter by median filter.

    2. a. Consider the image the attached named as hdraw.png and crop each of the characters from the image and consider that as the sub-image. Find the location of the sub-image in the original by using correlation.

       b. Download Lena color image convert it to grayscale image and crop the left eye of Lena as sub-image and do the cross-correlation ( Normalized correlation) to find the location of the left eye in the original image.

Note: For all the above questions write user-defined functions and compare with predefined (in-built) function.
