import pandas as pd
import numpy as np
import time
import csv
import os 

class data_pandas():

    def __init__(self, name) -> None:
        self.ts = time.time()
        self.name = name
        self.directory = name
        self.parent_dir = "data_collection"

    def write_to_csv(writer, keypoints):
        # time_stamp = time.time()
        row = keypoints
        writer.writerow(row)

    def data_to_pasdan_side(self,list):
        # path = os.path.join(self.parent_dir, self.directory)
        # try:
        #     os.mkdir(path)
        # except OSError as error:  
        #     print(error)

        list = list
        with open(f'data_collection/{self.name}/data/pose_data_side{time.time()}.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            
            header = ['time_stamp']
            for i in range(33):
                header.extend([f'keypoint_{i}_x', f'keypoint_{i}_y', f'keypoint_{i}_z', f'keypoint_{i}_confidence'])
            header.extend(['angle_shoulder_right', 'angle_elbow_right','angle_neck', 'angle_body','label'])
            writer.writerow(header)

            for ti, key, a, l in list:
                # print(ti,key,a,l,sep='\t')
                writer.writerow([ti]+key+a+[l])
                # print(li)

    def data_to_pasdan_top(self,list):
        # path = os.path.join(self.parent_dir, self.directory)
        # try:
        #     os.mkdir(path)
        # except OSError as error:  
        #     print(error)

        list = list
        with open(f'data_collection/{self.name}/data/pose_data_top{time.time()}.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            
            header = ['time_stamp']
            for i in range(33):
                header.extend([f'keypoint_{i}_x', f'keypoint_{i}_y', f'keypoint_{i}_z', f'keypoint_{i}_confidence'])
            header.extend(['angle_elbow_left', 'angle_elbow_right','angle_shoulder_left', 'angle_shoulder_right', 'label'])
            writer.writerow(header)

            for ti, key, a, l in list:
                # print(ti,key,sep='\t')
                writer.writerow([ti]+key+a+[l])