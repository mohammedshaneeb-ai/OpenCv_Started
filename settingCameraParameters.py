import cv2 
import datetime
cap = cv2.VideoCapture(2)
cap.set(3, 640)
cap.set(4, 480)
text = 'Width: ' + str(cap.get(3)) + ' Height : ' + str(cap.get(4))
font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    ret, frame = cap.read()
    if ret == True:
        date = str(datetime.datetime.now())

        frame = cv2.putText(frame,date,(10,50), font,1,(0,0,255),3)
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


print(cap.get(3))
print(cap.get(4))
cap.release()
cv2.destroyAllWindows()
