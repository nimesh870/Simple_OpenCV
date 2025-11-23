# change a image to a gray scale, display and save it

import cv2 as cv

img_relative_path = input("Enter the path of the file : ")

real_image = cv.imread(img_relative_path)
    

print("\n1. Show image in grey scale form.")
print("\n2. Save image in grey scale form.\n")

choice = int(input("Enter your choice : "))

if real_image is not None:
    
    if choice == 1:
        gray_scale_spidey = cv.cvtColor(real_image, cv.COLOR_BGR2GRAY) # changing color to gray
        cv.imshow("Showing image....", gray_scale_spidey)
        cv.waitKey(0)
        cv.destroyAllWindows()
    elif choice == 2 :
        gray_spidey = cv.cvtColor(real_image, cv.COLOR_BGR2GRAY)
        save_gray_spidey = cv.imwrite("new_spidey.jpg", gray_spidey) # saving the image
        
        if save_gray_spidey:
            print("Image saved successfully.")
            
        else:
            print("Image not saved.")
            
    else:
        print("\nEnter proper choice.")
        
else:
    print("Image not found.")