from imageai.Detection import ObjectDetection
import os



execution_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
detector.loadModel()

for filename in os.listdir("Real-World-Masked-Face-Dataset/RWMFD_part_1/0001"):
	if filename.endswith("jpg"): 
		detections = detector.detectObjectsFromImage(input_image=os.path.join("Real-World-Masked-Face-Dataset/RWMFD_part_1/0001" ,filename), output_image_path=os.path.join(execution_path , filename))
		for eachObject in detections:
			print(eachObject["name"] , " : " , eachObject["percentage_probability"] )
	else:
		continue

