# Python code for Multiple Color Detection 
  
  
import numpy as np 
import cv2 
import time




start_time = time.time()
x = 1 # displays the frame rate every 1 second
counter = 0  
    
# Capturing video through webcam 
webcam = cv2.VideoCapture("1.MP4") 

frame_width = int(webcam.get(3)) 
frame_height = int(webcam.get(4)) 
   
size = (frame_width, frame_height) 
   
# Below VideoWriter object will create 
# a frame of above defined The output  
# is stored in 'filename.avi' file. 
result = cv2.VideoWriter('1.avi',  
                         cv2.VideoWriter_fourcc(*'MJPG'), 
                         10, size) 
  
# Start a while loop 
while(1): 
      
    # Reading the video from the 
    # webcam in image frames 
    _, imageFrame = webcam.read() 
  
    # Convert the imageFrame in  
    # BGR(RGB color space) to  
    # HSV(hue-saturation-value) 
    # color space 
    hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV) 
  
    # Set range for red color and  
    # define mask 
    red_lower = np.array([136, 87, 111], np.uint8) 
    red_upper = np.array([180, 255, 255], np.uint8) 
    red_mask = cv2.inRange(hsvFrame, red_lower, red_upper) 
  
    # Set range for yellow color and  
    # define mask 
    yellow_lower = np.array([25, 150, 50], np.uint8) 
    yellow_upper = np.array([35, 255, 255], np.uint8) 
    yellow_mask = cv2.inRange(hsvFrame, yellow_lower, yellow_upper) 
  
    # Set range for orange color and 
    # define mask 
    orange_lower = np.array([15, 150, 0], np.uint8) 
    orange_upper = np.array([25, 255, 255], np.uint8) 
    orange_mask = cv2.inRange(hsvFrame, orange_lower, orange_upper)
    
    # Set range for black color and 
    # define mask 
    #black_lower = np.array([0, 0, 0], np.uint8) 
    #black_upper = np.array([150, 255, 150], np.uint8) 
    #black_mask = cv2.inRange(hsvFrame, black_lower, black_upper)
    
    
      
    # Morphological Transform, Dilation 
    # for each color and bitwise_and operator 
    # between imageFrame and mask determines 
    # to detect only that particular color 
    kernal = np.ones((5, 5), "uint8") 
      
    # For red color 
    red_mask = cv2.dilate(red_mask, kernal) 
    res_red = cv2.bitwise_and(imageFrame, imageFrame,  
                              mask = red_mask) 
      
    # For yellow color 
    yellow_mask = cv2.dilate(yellow_mask, kernal) 
    res_yellow = cv2.bitwise_and(imageFrame, imageFrame, 
                                mask = yellow_mask) 
      
    # For orange color 
    orange_mask = cv2.dilate(orange_mask, kernal) 
    res_orange = cv2.bitwise_and(imageFrame, imageFrame, 
                               mask = orange_mask) 
    
    # For blue black 
    #black_mask = cv2.dilate(black_mask, kernal) 
    #res_black = cv2.bitwise_and(imageFrame, imageFrame, 
    #                           mask = black_mask) 
   
    # Creating contour to track red color 
    contours, hierarchy = cv2.findContours(red_mask, 
                                           cv2.RETR_TREE, 
                                           cv2.CHAIN_APPROX_SIMPLE) 
      
    for pic, contour in enumerate(contours): 
        area = cv2.contourArea(contour) 
        if(area > 100): 
            x, y, w, h = cv2.boundingRect(contour) 
            imageFrame = cv2.rectangle(imageFrame, (x, y),  
                                       (x + w, y + h),  
                                       (0, 0, 255), 2) 
              
            cv2.putText(imageFrame, "Red Colour", (x, y), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1.0, 
                        (0, 0, 255))     
  

            
    # Creating contour to track yellow color 
    contours, hierarchy = cv2.findContours(yellow_mask, 
                                           cv2.RETR_TREE, 
                                           cv2.CHAIN_APPROX_SIMPLE) 
      
    for pic, contour in enumerate(contours): 
        area = cv2.contourArea(contour) 
        if(area > 75): 
            x, y, w, h = cv2.boundingRect(contour) 
            imageFrame = cv2.rectangle(imageFrame, (x, y),  
                                       (x + w, y + h), 
                                       (35, 255, 255), 2) 
              
            cv2.putText(imageFrame, "yellow Colour", (x, y), 
                        cv2.FONT_HERSHEY_SIMPLEX,  
                        1.0, (35, 255, 255)) 

            
    # Creating contour to track orange color 
    contours, hierarchy = cv2.findContours(orange_mask, 
                                           cv2.RETR_TREE, 
                                           cv2.CHAIN_APPROX_SIMPLE) 
    for pic, contour in enumerate(contours): 
        area = cv2.contourArea(contour) 
        if(area > 100): 
            x, y, w, h = cv2.boundingRect(contour) 
            imageFrame = cv2.rectangle(imageFrame, (x, y), 
                                       (x + w, y + h), 
                                       (25, 255, 255), 2) 
              
            cv2.putText(imageFrame, "orange Colour", (x, y), 
                        cv2.FONT_HERSHEY_SIMPLEX, 
                        1.0, (25, 255, 255)) 
            



              
    # Program Termination
#    result.write(imageFrame) 
    cv2.imshow("Multiple Color Detection in Real-TIme", imageFrame)
    result.write(imageFrame)
    counter+=1
    if (time.time() - start_time) > x :
        print("FPS: ", counter / (time.time() - start_time))
        counter=0
        start_time = time.time()
        


    if cv2.waitKey(10) & 0xFF == ord('q'): 
        webcam.release() 
        result.release() 
        #cap.release()
        cv2.destroyAllWindows() 
        break