import cv2
import mediapipe as mp
import math

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=True,max_num_hands=2,min_detection_confidence=0.5)
drawing_styles = mp.solutions.drawing_styles

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()

    w,h = 200,200
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, w)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, h)

    img = cv2.cvtColor(cv2.flip(img, 1), cv2.COLOR_BGR2RGB)
    img.flags.writeable = False
    results = hands.process(img)

    # Draw the hand annotations on the img.
    img.flags.writeable = True
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    if results.multi_hand_landmarks:
      for lms in results.multi_hand_landmarks:
          # print("Thumb: " + str(lms.landmark[4]))
          # print("Index: " + str(lms.landmark[8]))
          mp_drawing.draw_landmarks(img,lms,mp_hands.HAND_CONNECTIONS)

          x1, y1 = int(lms.landmark[4].x*w), int(lms.landmark[4].y*h)
          x2, y2 = int(lms.landmark[8].x*w), int(lms.landmark[8].y*h)

          distance = math.sqrt(((x1-x2)**2)+((y1-y2)**2))
          scaled = int((distance/125)*600)
          
          cv2.line(img, (30,30), (scaled,30), (255,0,255), 20)

    cv2.imshow('lol', img)
    cv2.waitKey(1)

cap.release()
