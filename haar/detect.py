import numpy as np
import cv2
import os
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
for filename in os.listdir("Real-World-Masked-Face-Dataset/RWMFD_part_1/0001"):
	if filename.endswith("jpg"): 
		flag = 0
		img = cv2.imread(os.path.join("Real-World-Masked-Face-Dataset/RWMFD_part_1/0001" ,filename))
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		faces = face_cascade.detectMultiScale(gray, 1.3, 5)
		for (x,y,w,h) in faces:
			flag = 1
			img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
			roi_gray = gray[y:y+h, x:x+w]
			roi_color = img[y:y+h, x:x+w]
			eyes = eye_cascade.detectMultiScale(roi_gray)
			for (ex,ey,ew,eh) in eyes:
				cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
		if flag == 1:
			print("PERSON")
		else:
			print("No person")
		cv2.imwrite(filename, img) 
		# cv2.imshow('img',img)
		# cv2.waitKey(0)
		# cv2.destroyAllWindows()
