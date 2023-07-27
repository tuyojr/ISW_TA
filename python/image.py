import cv2
import pytesseract

# Path to the Tesseract OCR executable (Change this if necessary)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Initialize the webcam capture
cap = cv2.VideoCapture(0)

while True:
    # Capture a frame from the webcam
    ret, frame = cap.read()

    # Preprocess the frame (you can add more preprocessing steps here)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Perform OCR on the preprocessed frame
    extracted_text = pytesseract.image_to_string(gray_frame)

    # Find bounding boxes for the detected characters
    boxes = pytesseract.image_to_boxes(gray_frame)
    for b in boxes.splitlines():
        b = b.split(' ')
        char, x, y, w, h = b[0], int(b[1]), int(b[2]), int(b[3]), int(b[4])
        cv2.rectangle(frame, (x, y), (w, h), ( 255,0, 0), 1)
        cv2.putText(frame, char, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

    # Display the extracted text
    print(extracted_text)

    # Display the original frame with bounding boxes and text
    cv2.imshow('Webcam', frame)

    # Stop the loop when the user presses 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()