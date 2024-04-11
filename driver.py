from ultralytics import YOLO

model=YOLO('bestNew.pt')
source = '2wheelertraffic.webm'
results = model(source, show=True)