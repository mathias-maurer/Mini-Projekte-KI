from ultralytics import YOLO


# Konvertierung auf NCNN
#YOLO11n ist ein leichtgewichtiges Modell der YOLO11-Familie, das für ressourcenbeschränkte
# #Umgebungen entwickelt wurde. Mit etwa 2,6 Millionen Parametern ermöglicht es schnelle
# Inferenzzeiten bei moderater Genauigkeit und eignet sich daher besonders für Anwendungen
# auf mobilen Geräten oder eingebetteten Systemen.

# Load a pretrained YOLO model
model = YOLO("yolo11n.pt")

model.export(format="ncnn")