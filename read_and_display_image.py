import cv2

image = cv2.imread("download.jpg", 1) #reads and loads image

if image is not None:
    cv2.imshow("Showing Image.........", image) #shows image in a window
    cv2.waitKey(0) #waits until a key is pressed to exit
    cv2.destroyAllWindows() #exits the window safely
    
else:
    print("Image not loaded.")
    
    