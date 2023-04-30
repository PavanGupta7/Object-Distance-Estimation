import cv2
cap = cv2.VideoCapture(0)
frame_count=0

while cap.isOpened():
    ret, frame = cap.read()
    
    cv2.imshow("Webcam", frame)
    if cv2.waitKey(1) == ord(' '):
        frame_count+=1
        filename = f".dataset/pen/pencil_{frame_count}.jpg"
        cv2.imwrite(filename, frame)
        print(f"Saved {filename}")
    if cv2.waitKey(1) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()