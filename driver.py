from ultralytics import YOLO

model=YOLO('best.pt')
source = '2wheelerTrafficWOHelmet.webm'
results = model(source, show=True)
