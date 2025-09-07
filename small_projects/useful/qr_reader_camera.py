import cv2
import webbrowser

video = cv2.VideoCapture(0)
success, frame = video.read()
detector = cv2.QRCodeDetector()

while success:
    url, coords, pixels = detector.detectAndDecode(frame)

    if url:
        webbrowser.open(url)
        break

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

    success, frame = video.read()

video.release()
cv2.destroyAllWindows()
