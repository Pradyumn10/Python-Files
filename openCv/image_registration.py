'''
* @FileName : image_registration.py
* @author : Pradyumn Joshi
* @brief : It is image registration file , it registers image using opencv library's Brute Force Matcher
* @version : 0.1.0
*
* @copyright (c) 2021
'''
import cv2 
import numpy as np 
import os

a = 0
count = 0
print("Registering Image")

#reference image
ref = "left0026.jpg"
print("reference image", ref)

while a<162:
    path = "./bag1_images/{}.jpg".format(a)
    ref = "left0026.jpg"
    a += 1
    
    if os.path.isfile(path):
        img1_color = cv2.imread(path) # Image to be aligned. 
        img2_color = cv2.imread(ref) # Reference image. 
        print("Registration Image" , path)
        img1 = cv2.cvtColor(img1_color, cv2.COLOR_BGR2GRAY) 
        img2 = cv2.cvtColor(img2_color, cv2.COLOR_BGR2GRAY) 
        height, width = img2.shape 

        orb_detector = cv2.ORB_create() 
        kp1, d1 = orb_detector.detectAndCompute(img1, None) 
        kp2, d2 = orb_detector.detectAndCompute(img2, None) 

        # We create a Brute Force matcher with 
        matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True) 
        matches = matcher.match(d1, d2) 
        matches.sort(key = lambda x: x.distance) 

        # Take the top 90 % matches forward. 
        matches = matches[:int(len(matches)*90)] 
        no_of_matches = len(matches) 

        p1 = np.zeros((no_of_matches, 2)) 
        p2 = np.zeros((no_of_matches, 2)) 

        for i in range(len(matches)): 
            p1[i, :] = kp1[matches[i].queryIdx].pt 
            p2[i, :] = kp2[matches[i].trainIdx].pt 

        homography, mask = cv2.findHomography(p1, p2, cv2.RANSAC) 

        # colored image wrt the reference image. 
        transformed_img = cv2.warpPerspective(img1_color, homography, (width, height))
        img3 = cv2.drawMatches(img1, p1, img2, p2 , matches, None , flags=2)
        
        # Save the output. 
        cv2.imwrite("./registered_set5/{}.jpg".format(count), transformed_img) 
        print("written image ",count )
        cv2.imwrite("./registered_set5/matches/{}.jpg".format(count), img3)
        count += 1
    if a == 162:
        break
