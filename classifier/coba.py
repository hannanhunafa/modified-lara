import cv2
image_path = 'dataset/74.jpg'
bgr = cv2.imread(image_path)

lab = cv2.cvtColor(bgr, cv2.COLOR_BGR2LAB)

lab_planes = cv2.split(lab)

clahe = cv2.createCLAHE(clipLimit=)

lab_planes[0] = clahe.apply(lab_planes[0])

lab = cv2.merge(lab_planes)

bgr = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)

cv2.imshow('clahe',bgr)

cv2.waitKey(0) 