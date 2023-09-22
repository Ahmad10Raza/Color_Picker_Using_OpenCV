import cv2
import numpy as np

def do_nothing(x):
    pass


# Creating a black images and a window
img=np.zeros((300,512,3),np.uint8)
cv2.namedWindow("Color Picker")

# Creating trackbars  1==ON and 0==OFF
switch='0:OFF \n 1:ON'
cv2.createTrackbar(switch,'Color Picker',0,1,do_nothing)


# Creating trackbars for Adjusting BGR values
cv2.createTrackbar('R','Color Picker',0,255,do_nothing) # Here do_nothing is a function which does nothing
cv2.createTrackbar('G','Color Picker',0,255,do_nothing) 
cv2.createTrackbar('B','Color Picker',0,255,do_nothing)

# Now Creating to handle trackbar events
while True:
    cv2.imshow('Color Picker',img)
    k=cv2.waitKey(1) & 0xFF
    if k==27: # 27 is the ASCII value of ESC key
        break 

    # Getting the current position of the trackbars
    s=cv2.getTrackbarPos(switch,'Color Picker') # Here s is the current position of the switch
    r=cv2.getTrackbarPos('R','Color Picker') # Here r is the current position of the Red trackbar
    g=cv2.getTrackbarPos('G','Color Picker') # Here g is the current position of the Green trackbar
    b=cv2.getTrackbarPos('B','Color Picker') # Here b is the current position of the Blue trackbar

    if s==0:
        img[:]=0
    else:
        img[:]=[b,g,r] # Here we are assigning the current position of the trackbars to the image

    # Display RGB Values On The Image
    rgb_text=f'RGB Value is: {r},{g},{b}'
    cv2.putText(img,rgb_text,(10,30),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,255,255),2)    

cv2.destroyAllWindows()