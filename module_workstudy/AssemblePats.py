import math
import numpy as np

def findDistance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    dist = int(math.sqrt((x2-x1)**2 + (y2-y1)**2))
    return dist

def findAngle(p1,p2):
    x1, y1 = p1
    x2, y2 = p2
    try:
        theta = math.acos((y2-y1)*(-y1) / (math.sqrt(
            (x2 - x1) ** 2 +(y2 - y1)**2)*y1))
        # theta = math.atan2(y2 - y1 , x2 - x1)
        degree = round((180/math.pi)*theta,3)
        return degree
    except:
        pass

def findAngle_elbow(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    angle = round(math.degrees(math.atan2(y3 - y2, x3 - x2) -
                        math.atan2(y1 - y2, x1 - x2)),2)
    
    if angle < 0:
        angle += 360
    
    return angle

def calculate_angle(a, b, c):
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)
    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)
    if angle > 180.0:
        angle = 360 - angle
    return angle



