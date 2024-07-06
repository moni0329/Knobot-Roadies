#Anaconda prompt was used

conda activate KnobotRoadies

#clone the YOLOv5 repository

git clone https://github.com/ultralytics/yolov5
cd yolov5

#dataset was placed in following directory paths
#images
'''
E:\Cw_detection\data\images\test\crosswalk
E:\Cw_detection\data\images\test\no_crosswalk

E:\Cw_detection\data\images\train\crosswalk
E:\Cw_detection\data\images\train\no_crosswalk

E:\Cw_detection\data\images\val\crosswalk
E:\Cw_detection\data\images\val\no_crosswalk

#lables

E:\Cw_detection\data\labels\test\crosswalk
E:\Cw_detection\data\labels\test\no_crosswalk

E:\Cw_detection\data\labels\train\crosswalk
E:\Cw_detection\data\labels\train\no_crosswalk

E:\Cw_detection\data\labels\val\crosswalk
E:\Cw_detection\data\labels\val\no_crosswalk

'''

#placed train.py from YOLOv5 directory in path

E:\Cw_detection\train.py

#Create a file named crosswalk.yaml inside the E:\Cw_detection\data
'''
train: E:/Cw_detection/data/images/train
val: E:/Cw_detection/data/images/val
nc: 1  # Number of classes
names: ['crosswalk']
'''

#Train the Model

python train.py --img 200 --batch 32 --epochs 50 --data E:/Cw_detection/data/crosswalk.yaml --weights yolov5s.pt

#Validate the model
python val.py --data E:/Cw_detection/data/crosswalk.yaml --weights C:/Users/ss/yolov5/yolov5/runs/train/exp6/weights/best.pt --img 200
