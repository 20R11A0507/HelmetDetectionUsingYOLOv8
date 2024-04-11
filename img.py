import cv2    
import time
cpt = 0
maxFrames = 100

count=0
cap=cv2.VideoCapture('2wheelerTrafficWOHelmet.webm')
while cpt < maxFrames:
    ret, frame = cap.read()
    frame=cv2.resize(frame,(1080,500))
    time.sleep(0.01)
    cv2.imshow("test window", frame)
    cv2.imwrite(r"path\to\folder\images\helmet_%d.jpg" %cpt, frame)
    cpt += 1
    if cv2.waitKey(5)&0xFF==27:
        break
cap.release()   
cv2.destroyAllWindows()
