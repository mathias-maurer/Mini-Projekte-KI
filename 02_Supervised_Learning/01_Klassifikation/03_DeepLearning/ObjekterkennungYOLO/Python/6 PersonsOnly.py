from ultralytics import YOLO

# Load a pretrained YOLO model
model = YOLO("yolo11n_ncnn_model")

# Perform object detection on an image
#
# Liste aller Klassen:
# https://gist.github.com/rcland12/dc48e1963268ff98c8b2c4543e7a9be8

# Klasse 0 = Personen
results = model.predict("Bilder/tools.jpg", classes=[0])

# Personen im Ergebnis?
if len(results[0].boxes) > 0:
    print("Personen erkannt")
else:
    print("Keine Personen erkannt")

# Darstellung des Ergebnisses
for result in results:
    result.show()

