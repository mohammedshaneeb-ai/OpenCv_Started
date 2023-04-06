import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    #gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()