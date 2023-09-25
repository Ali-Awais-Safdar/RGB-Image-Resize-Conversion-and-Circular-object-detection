import cv2
image = cv2.imread("./coins.jpg",2) # 2 means read image in grayscale
cv2.imshow('Grayscale', image)
cv2.waitKey(0)
#pixels with intensity value greater than 127 are set to white and less are set to black\
ret, bw_img = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY) 
cv2.imshow('Binary', bw_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
