import cv2
import os
from tqdm import tqdm

for image in tqdm(os.listdir('leaf/')):
    image_path = 'leaf/' + image
    bgr = cv2.imread(image_path)

    lab = cv2.cvtColor(bgr, cv2.COLOR_BGR2LAB)

    lab_planes = cv2.split(lab)

    clahe = cv2.createCLAHE(clipLimit=1.5)

    lab_planes[0] = clahe.apply(lab_planes[0])

    lab = cv2.merge(lab_planes)

    bgr = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)

    save_path = 'clahe/' + image
    cv2.imwrite(save_path, bgr)