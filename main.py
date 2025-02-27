import cv2
import mediapipe as mp
import pyautogui
cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
thumb_y = 0
while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x= int(landmark.x*frame_width)
                y= int(landmark.y*frame_height)
                print(x,y)
                if id == 4:
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                    thumb_x = screen_width/frame_width*x
                    thumb_y = screen_height/frame_height*y



                if id == 8:
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 0))
                    index_x = screen_width/frame_width*x
                    index_y = screen_height/frame_height*y
                    if abs(index_y - thumb_y) < 30:
                        pyautogui.click()
                    elif abs(index_y - thumb_y) < 100:
                        pyautogui.moveTo(thumb_x, thumb_y)

                if id == 12:
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 0))
                    middle_x = screen_width / frame_width * x
                    middle_y = screen_height / frame_height * y
                    print('outside',abs(index_y - middle_y))
                    if abs(index_x - middle_x) < 20:
                        if abs(index_y - middle_y)<20:
                            pyautogui.rightClick()
                if id == 14:
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(255, 0,0))
                    ring_x = screen_width/frame_width*x
                    ring_y = screen_height/frame_height*y
                    if abs(ring_x - thumb_x) < 30:
                        if abs(ring_y - thumb_y) <30:
                            pyautogui.scroll(50)
                if id == 17:
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(255, 0, 0))
                    pinky_x = screen_width/frame_width*x
                    pinky_y = screen_height/frame_height*y
                    if abs(pinky_x - thumb_x) < 30:
                        if abs(pinky_y - thumb_y) < 30:

                             pyautogui.scroll(-50)

    print(hands)
    cv2.imshow('Virtual Mouse', frame)
    cv2.waitKey(1)
