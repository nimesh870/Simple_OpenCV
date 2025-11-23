import cv2

image = cv2.imread("download.jpg")

if image is not None:
    saved = cv2.imwrite("saved_file.jpg", image)
    
    if saved:
        print("Image saved successfully.")
    else:
        print("Couldnot save the image.")
    
else:
    print("No images found.")