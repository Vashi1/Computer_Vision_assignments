import cv2
image = cv2.imread("Einstein.jpg")
print(image.shape)

# cv2.imshow("Original",image)
# cv2.waitKey(0)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print(gray_image.shape)
cv2.imshow("New", gray_image)
cv2.waitKey(0)
# cv2.destroyAllWindows()

