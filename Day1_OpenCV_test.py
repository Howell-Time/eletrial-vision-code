import cv2
print(cv2.getVersionString())
image=cv2.imread("plane.jpg")
print(image.shape)
cv2.imshow("image",image)
cv2.waitKey(0)

image2=cv2.imread("opencv_logo.jpg")
cv2.imshow("blue",image2[:,:,0])
cv2.imshow("green",image2[:,:,1])
cv2.imshow("Red",image2[:,:,2])

gray=cv2.cvtColor(image2,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",gray)
cv2.waitKey()

crop=image2[10:170,40:200]
cv2.imshow("crop",crop)
cv2.waitKey()