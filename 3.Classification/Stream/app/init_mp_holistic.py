import cv2
import mediapipe as mp

mp_holistic = mp.solutions.holistic

holistic = mp_holistic.Holistic(static_image_mode=True,
                                    model_complexity=2,
                                    min_detection_confidence=0.5,
                                    min_tracking_confidence=0.5)

file = 'data/holistic.jpg'
image = cv2.imread(file)
# Convert the BGR image to RGB before processing.
results = holistic.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

print('Initialization finished')