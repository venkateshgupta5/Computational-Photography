import cv2
import numpy as np 
#Step:-1
#Let's load our damaged photo
#imread function of cv2 reads the image
damaged_image = cv2.imread('/home/venkat/Downloads/orgimg.jpg')
cv2.imshow('Original Image', damaged_image)
cv2.waitKey(0)
#Step:-2
#Let's mark the damaged area with the help of paint. Bascially we are drawing lines.
marked_img = cv2.imread('/home/venkat/Downloads/marked3.jpg',0)
cv2.imshow('Damaged Image - Its marked now', marked_img)
cv2.waitKey(0)
#Step :-3
#Let's mask our marked_img
#By masking, we mean we are thresholding
#Thresholding - Things that are not white are made black
# So something white would appear on black background
ret, thresh = cv2.threshold(marked_img, 254, 255, cv2.THRESH_BINARY)
#Step 4 :- Thresholding Narrow's our Image
#Let's make it dilated(thicker)
kernel = np.ones((7,7), np.uint8)
#We are creating a 7X7 matrix 
mask = cv2.dilate(thresh, kernel, iterations=1)
cv2.imshow('Dilated Mask', mask)
cv2.waitKey(0)
restored = cv2.inpaint(image, mask, 3, cv2.INPAINT_TELEA)
cv2.imshow('Restored', restored)
cv2.waitKey(0)
cv2.destroyAllWindows()