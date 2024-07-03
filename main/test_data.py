import cv2
import mediapipe as mp
import csv
import time
import numpy as np

# Initialize Mediapipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_drawing = mp.solutions.drawing_utils

def calculate_angle(a, b, c):
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)
    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)
    if angle > 180.0:
        angle = 360 - angle
    return angle

def extract_keypoints_and_angles(results):
    keypoints = []
    for lm in results.pose_landmarks.landmark:
        keypoints.extend([lm.x, lm.y, lm.z, lm.visibility])
    
    landmarks = results.pose_landmarks.landmark
    angle_elbow_left = calculate_angle(
        [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y],
        [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x, landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y],
        [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x, landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
    )
    angle_elbow_right = calculate_angle(
        [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y],
        [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y],
        [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]
    )
    angle_knee_left = calculate_angle(
        [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x, landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y],
        [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x, landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y],
        [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x, landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y]
    )
    angle_knee_right = calculate_angle(
        [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y],
        [landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y],
        [landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].y]
    )
    
    return keypoints, angle_elbow_left, angle_elbow_right, angle_knee_left, angle_knee_right

def write_to_csv(writer, keypoints, angles, label):
    time_stamp = time.time()
    row = [time_stamp] + keypoints + angles + [label]
    writer.writerow(row)

def main():
    cap = cv2.VideoCapture(0)
    
    with open('pose_data.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        
        header = ['time_stamp']
        for i in range(33):
            header.extend([f'keypoint_{i}_x', f'keypoint_{i}_y', f'keypoint_{i}_z', f'keypoint_{i}_confidence'])
        header.extend(['angle_elbow_left', 'angle_elbow_right', 'angle_knee_left', 'angle_knee_right', 'label'])
        writer.writerow(header)
        
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = pose.process(image)
            
            if results.pose_landmarks:
                keypoints, angle_elbow_left, angle_elbow_right, angle_knee_left, angle_knee_right = extract_keypoints_and_angles(results)
                angles = [angle_elbow_left, angle_elbow_right, angle_knee_left, angle_knee_right]
                label = "unknown"  # Placeholder label
                write_to_csv(writer, keypoints, angles, label)
            
            mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
            cv2.imshow('Webcam Feed', frame)
            
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
