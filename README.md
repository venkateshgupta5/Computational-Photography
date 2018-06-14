# Computational-Photography
Photo Restoration Using Open CV

Photo Restoration is an application of Computational Photography.
## WTF is Computational Photography?

It’s a digital image processing technique that helps to enhance images like removing noise, stabilising it and removing strokes and marks and blah-blah-blah!

It’s only because of many image processing techniques that you are able get quite good photos even with your smartphones. Computational photography is quite handy! Isn’t it?

#Requirements 

1. Open-cv
2. Python 2.7

# Let’s see what cv2.inpaint function parameters are :-
cv2.inpaint(input image, mask, inpaintRadius, Inpaint Method)
inpaintRadius – Radius of a circular neighbourhood of each point in painted that is considered by the algorithm. 

*Smaller values look less blurred, 
while larger values look more pixelated or blurred.*

Inpaint Methods - 
INPAINT_NS - Navier-Stokes based method [Navier01] - 
INPAINT_TELEA - Method by Alexandru Telea [Telea04] -
Better as it integrates more seamlessly into the image.



