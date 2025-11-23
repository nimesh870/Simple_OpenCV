import cv2 as cv

capture = cv.VideoCapture(0) # vaptures the video
frame_width = int(capture.get(cv.CAP_PROP_FRAME_WIDTH))
frame_height = int(capture.get(cv.CAP_PROP_FRAME_HEIGHT))

codec = cv.VideoWriter_fourcc(*'XVID')

# Define the codec for video compression using FourCC (here 'XVID' for MPEG-4)
codec = cv.VideoWriter_fourcc(*'XVID')
record = cv.VideoWriter("attandence.py", codec, 20, (frame_width, frame_height))

while True:
    success , image = capture.read()
    
    if not success:
        break
    
    record.write(image)
    cv.imshow("Recording image.....", image)
    saved = cv.imwrite("exported_pic.jpg", image)
    
    if cv.waitKey(1) & 0xFF == ord('e'):  #waits until user presses "e" to exit
        break

if saved:
    print("\nPicture saved.")
    
else:
    print("Failed to to save picture.")
    
capture.release()
cv.destroyAllWindows()
        
        