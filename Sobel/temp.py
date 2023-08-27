import cv2
imgpath = "luffy.jpg"
img = cv2.imread(imgpath, 1)

edgesx = cv2.Sobel(img, -1, dx=1, dy=0, ksize=1)
edgesy = cv2.Sobel(img, -1, dx=0, dy=1, ksize=1)
edges = edgesx + edgesy

# This will display the original image
cv2.namedWindow('Original', cv2.WINDOW_NORMAL)
cv2.imshow('Original', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# This will display the X gradient
cv2.namedWindow('X Gradient', cv2.WINDOW_NORMAL)
cv2.imshow('X Gradient', edgesx)
cv2.waitKey(0)
cv2.destroyAllWindows()

# This will display the Y gradient
cv2.namedWindow('Y Gradient', cv2.WINDOW_NORMAL)
cv2.imshow('Y Gradient', edgesy)
cv2.waitKey(0)
cv2.destroyAllWindows()

# This will display the Edges (X + Y Gradients)
cv2.namedWindow('Edges (X + Y Gradients)', cv2.WINDOW_NORMAL)
cv2.imshow('Edges (X + Y Gradients)', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
