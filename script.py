import cv2
image = cv2.imread("Einstein.jpg")
print(image.shape)

# cv2.imshow("Original",image)
# cv2.waitKey(0)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print(gray_image.shape) #2666, 2000
smol = cv2.resize(gray_image, (666, 400))
cv2.imshow("New", smol)
cv2.imwrite("Einstein_modified.jpg", smol)
cv2.waitKey(0)
cv2.destroyAllWindows()

