import time
import cv2
import numpy as np

color = None
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW) #windows only

#cv2.namedWindow("Test")

def viewImage(image):
    cv2.namedWindow('Display', cv2.WINDOW_NORMAL)
    cv2.imshow('Display', image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


def findColoredCircle(image, picked_color):
    #image = cv2.imread('./images/lol.png')
    original = image.copy()
    viewImage(original)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #blurred = cv2.medianBlur(gray, 25)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # print(image)
    # lower = np.array([60, 40, 0], dtype="uint8")
    # upper = np.array([80, 255, 232], dtype="uint8")
    if picked_color == "red":
        lower1 = np.array([0, 40, 50], dtype="uint8")
        upper1 = np.array([10, 255, 255], dtype="uint8")
        lower2 = np.array([175, 40, 50], dtype="uint8")
        upper2 = np.array([180, 255, 255], dtype="uint8")

        mask1 = cv2.inRange(image, lower1, upper1)
        mask2 = cv2.inRange(image, lower2, upper2)
        mask = cv2.bitwise_or(mask1, mask2)
    elif picked_color == "yellow":
        lower = np.array([20, 30, 200], dtype="uint8")
        upper = np.array([35, 255, 255], dtype="uint8")
        mask = cv2.inRange(image, lower, upper)

    minDist = 100
    param1 = 30  # 500
    param2 = 30  # 200 #smaller value-> more false circles
    minRadius = 5
    maxRadius = 200  # 10
    blurred = cv2.medianBlur(mask, 25)
    circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1, minDist, param1=param1, param2=param2,
                               minRadius=minRadius, maxRadius=maxRadius)
    cv2.imshow("blur", blurred)
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            cv2.circle(original, (i[0], i[1]), i[2], (0, 255, 0), 2)
            global color
            color = picked_color

    # contours = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # contours = contours[0] if len(contours) == 2 else contours[1]
    #
    # for cont in contours:
    #     perimeter = cv2.arcLength(cont, True)
    #     appox = cv2.approxPolyDP(cont, 0.04 * perimeter, True)
    #     if len(appox) > 5:
    #         cv2.drawContours(original, [cont], -1, (36, 255, 12), -1)
    #         global color
    #         color = picked_color

    #cv2.imshow('Test', original)
    cv2.imshow('mask', mask)
    cv2.imshow('original', original)


def recognizeFromFile():
    global image, lower, upper
    image = cv2.imread("./images/" + input('image name from ./images/'))
    picked_color = "red" if input("[r]ed or [y]ellow color?: ") == ("r" or "red") else "yellow"
    findColoredCircle(image, picked_color)
    print(color)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def recongnizeFromWebcamera():
    #picked_color = "red" if input("[r]ed or [y]ellow color?: ") == ("r" or "red") else "yellow"
    picked_color = "red"
    #while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        #break
    findColoredCircle(frame, picked_color)
    cv2.waitKey(0)
    #time.sleep(6)



recongnizeFromWebcamera()
#recognizeFromFile()
print(color)
