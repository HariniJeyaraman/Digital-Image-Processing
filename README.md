# Digital-Image-Processing
Various exercises in DIP 

1) 1. Read a matrix of size 5*5 and find the following by using a user-defined function.
    i. sum
    ii. maximum
    iii.mean  
    iv.median   
    v.mode    
    vi.standard deviation       
    v. frequency distribution

   2. Read the matrix size through keyboard and create a random matrix of integers ranging from  0 to 10 and compute all the                   above functions listed in question 1.

Note: 1. Should not import any module for Question 1
          2. Only a random module package is allowed in Question 2.
          
2) Take a Lena image and convert it into grayscale. 
   Add three different types of noises(salt and pepper, additive Gaussian noise, speckle), 
   each noise in the sets of 5,10,15,20,25,30. Take average for each set and display the average images.
   Report the observation made.
   Observation : Averaging removes noise.
   
3) a) Download Lena image and scale it by factors of 1,2,0.5 using bilinear interpolation and display the scaled images. Also, display the output of built-in functions for doing scaling by factors of 0.5,2. Compare the results.
   b) Download the leaning tower of PISA image and find the angle of inclination using appropriate rotations with bilinear interpolation.
   c) Do histogram equalization on pout-dark and display the same
   d) Do histogram matching(specification) on the pout-dark image, keeping pout-bright as a reference image.
   
 4) 1. Download Lena color image convert it to grayscale image and add salt and  pepper noise with noise quantity 0.1,0.2 upto 1 and generate 10 noisy images.
         a. Do average filtering ( by correlating with average filter ) of varying sizes for each image. Filter size can be 3*3, 5*5, 7*7. (In 3*3 filter all the values are 1/9, in 5*5 filter all the values are 1/25 and in 7*7 filter all the values are 1/49)
         b. Similarly, repeat the question 1.a by replacing the average filter by median filter.

    2. a. Consider the image the attached named as hdraw.png and crop each of the characters from the image and consider that as the sub-image. Find the location of the sub-image in the original by using correlation.

       b. Download Lena color image convert it to grayscale image and crop the left eye of Lena as sub-image and do the cross-correlation ( Normalized correlation) to find the location of the left eye in the original image.

Note: For all the above questions write user-defined functions and compare with predefined (in-built) function.
