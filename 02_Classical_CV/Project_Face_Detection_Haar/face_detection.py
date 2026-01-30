import cv2

def main():
    # 1. Load the Cascade
    # OpenCV comes with pre-trained models. using the default one for frontal face.
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    if face_cascade.empty():
        raise IOError("Unable to load the face cascade xml file.")

    # 2. Start Video Capture (0 is usually the default camera)
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Could not access the webcam.")
        print("Fallback: Using a static image instead.")
        # Fallback to an image if webcam fails
        # You can replace this with any image containing a face
        image_path = '02_Classical_CV/01_Image_Transformations/original.jpg' 
        frame = cv2.imread(image_path)
        if frame is None:
             print("Could not load fallback image.")
             return
        
        # Detect in the static image
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            
        cv2.imwrite('face_detection_result.jpg', frame)
        print("Face detection ran on static image. result saved to face_detection_result.jpg")
        return

    print("Press 'q' to quit the video stream.")

    while True:
        # 3. Read Frame
        ret, frame = cap.read()
        if not ret:
            break
        
        # 4. Convert to Grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # 5. Detect Faces
        # scaleFactor=1.1: Image is reduced by 10% at each scale
        # minNeighbors=5: How many neighbors each candidate rectangle should have
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        
        # 6. Draw Rectangles
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, "Face", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        # 7. Display
        cv2.imshow('Face Detection (Haar Cascades)', frame)
        
        # Stop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
