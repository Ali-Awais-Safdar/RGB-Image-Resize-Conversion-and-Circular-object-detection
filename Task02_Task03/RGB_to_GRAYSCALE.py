import cv2
image = cv2.imread("./coins.jpg")
cv2.imshow('Original', image)
cv2.waitKey(0) # 0 means wait for any keypress
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # BGR to GRAY
cv2.imshow('Grayscale', gray_image) # Displaying the grayscale image
cv2.waitKey(0)
cv2.destroyAllWindows() # Destroy all windows 
