import cv2
import numpy as np
import time
import os

def draw_on_canvas(canvas, x1, y1, x2, y2, color=(255, 0, 0), thickness=5):
    if x1 is not None and y1 is not None:
        cv2.line(canvas, (x1, y1), (x2, y2), color, thickness)
    return canvas

def save_drawing(canvas):
    if not os.path.exists('output'):
        os.makedirs('output')
    filename = f'output/drawing_{int(time.time())}.png'
    cv2.imwrite(filename, canvas)
    print(f"Saved drawing to {filename}")
