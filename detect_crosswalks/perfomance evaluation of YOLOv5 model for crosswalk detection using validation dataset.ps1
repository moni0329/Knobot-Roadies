(base) C:\Users\ss>conda activate KnobotRoadies

(KnobotRoadies) C:\Users\ss>cd C:/Users/ss/yolov5/yolov5

(KnobotRoadies) C:\Users\ss\yolov5\yolov5>python val.py --data E:/Cw_detection/data/crosswalk.yaml --weights C:/Users/ss/yolov5/yolov5/runs/train/exp6/weights/best.pt --img 200
val: data=E:/Cw_detection/data/crosswalk.yaml, weights=['C:/Users/ss/yolov5/yolov5/runs/train/exp6/weights/best.pt'], batch_size=32, imgsz=200, conf_thres=0.001, iou_thres=0.6, max_det=300, task=val, device=, workers=8, single_cls=False, augment=False, verbose=False, save_txt=False, save_hybrid=False, save_conf=False, save_json=False, project=runs\val, name=exp, exist_ok=False, half=False, dnn=False
YOLOv5  v7.0-331-gab364c98 Python-3.11.9 torch-2.3.0+cpu CPU

Fusing layers...
Model summary: 157 layers, 7012822 parameters, 0 gradients, 15.8 GFLOPs
WARNING  --img-size 200 must be multiple of max stride 32, updating to 224
val: Scanning E:\Cw_detection\data\labels\val\crosswalk.cache... 446 images, 223 backgrounds, 0 corrupt: 100%|██████████| 446/446 [00:00<?, ?it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100%|██████████| 14/14 [01:49<00:00,  7.81s/it]
                   all        446        387       0.95      0.982      0.984      0.733
Speed: 2.3ms pre-process, 229.1ms inference, 3.4ms NMS per image at shape (32, 3, 224, 224)
Results saved to runs\val\exp6

(KnobotRoadies) C:\Users\ss\yolov5\yolov5>
