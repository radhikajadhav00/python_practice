import cv2

img = cv2.imread("input.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (21, 21), 0)
sketch = cv2.divide(gray, blur, scale=256.0)

cv2.imwrite("sketch.png", sketch)
print("Sketch created as sketch.png")
