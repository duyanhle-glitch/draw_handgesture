import cv2
import numpy as np
import mediapipe as mp
from utils import draw_on_canvas, save_drawing

# Khởi tạo Mediapipe Hand
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Khởi tạo webcam
cap = cv2.VideoCapture(0)

# Tạo canvas trắng
canvas = np.zeros((480, 640, 3), dtype=np.uint8)

# Chế độ để kiểm tra xem có đang vẽ không
drawing = False
prev_x, prev_y = None, None

with mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7) as hands:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)  # Lật ngược cho giống gương
        h, w, c = frame.shape
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb_frame)

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                x = int(hand_landmarks.landmark[8].x * w)
                y = int(hand_landmarks.landmark[8].y * h)

                if drawing:
                    canvas = draw_on_canvas(canvas, prev_x, prev_y, x, y)

                prev_x, prev_y = x, y
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        # Kết hợp frame + canvas
        combined = cv2.addWeighted(frame, 0.5, canvas, 0.5, 0)

        cv2.imshow('Air Drawing - Press d to toggle draw, s to save, q to quit', combined)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('d'):
            drawing = not drawing
        elif key == ord('s'):
            save_drawing(canvas)
        elif key == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
