from ultralytics import YOLO

model=YOLO('bestNew.pt')
source = '2wheelerTrafficWOHelmet.webm'
results = model(source, show=True)
