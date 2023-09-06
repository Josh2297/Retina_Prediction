import cv2
from roboflow import Roboflow

def process_video_and_predict(video_path, api_key):
    # Initialize Roboflow API
    rf = Roboflow(api_key=api_key)
    project = rf.workspace().project("retina-detection-btcix")
    model = project.version(1).model

    # Get the frames per second (fps) of the video
    video = cv2.VideoCapture(video_path)
    fps = video.get(cv2.CAP_PROP_FPS)

    # Initialize variables to store the information of the prediction with the highest confidence
    highest_confidence = 0
    highest_confidence_frame = None
    highest_confidence_prediction = None

    frame_count = 0
    while True:
        ret, frame = video.read()
        if not ret:
            break

        # Calculate the time in seconds
        time = frame_count / fps

        if int(time) % 1 == 0:
            # Perform prediction on the current frame
            prediction = model.predict(frame, confidence=40, overlap=30)
            prediction_args = prediction.json()

            # Get the prediction with the highest confidence score
            predictions = prediction_args["predictions"]
            for pred in predictions:
                confidence = pred["confidence"]
                if confidence > highest_confidence:
                    highest_confidence = confidence
                    highest_confidence_frame = frame.copy()
                    highest_confidence_prediction = pred

        frame_count += 1

    if highest_confidence_frame is not None:
        # Get bounding box coordinates from the highest prediction
        width = int(highest_confidence_prediction["width"])
        height = int(highest_confidence_prediction["height"])
        x = int(highest_confidence_prediction["x"] - (0.5 * width))
        y = int(highest_confidence_prediction["y"] - (0.5 * height))

        # Crop the image using the bounding box
        cropped_image = highest_confidence_frame[y:y + height, x:x + width]
        resized_cropped_image = cv2.resize(cropped_image, (500, 500))
        final_image = list(resized_cropped_image)
        # Display the cropped image
        #cv2_imshow(resized_cropped_image)

    # Return the highest confidence prediction
    return final_image

if __name__  == "__main__":
    a = process_video_and_predict('VID1.mp4', 'TVZxyhQ0qA0Yztn1SjaF')
    print('Happy')
    print(a)