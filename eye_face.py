import cv2
import time
tempList=[None]*100
i=0

face_cascade = cv2.CascadeClassifier('cascade_face.xml')
eye_cascade = cv2.CascadeClassifier('open_eye_only.xml')
cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]

        eyes = eye_cascade.detectMultiScale(roi_gray)
        print(len(eyes))
        temp=len(eyes)

        if len(eyes)<1:
            time.sleep(1)
            if len(eyes)<1:

                tempList[i]=0

                i=i+1
                if len(eyes)>1:
                    i=0
                    tempList[5]==1
                if tempList[5]==0:
                    print('driver is sleeping')
                    tempList[5]=1
                    i=0
                else:

                    pass
        #print(s)
        #if s[5]==0:
         #   print('DRIVER IS SLEEPING')
          #  time.sleep(5)
           # s=[None]*100
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
