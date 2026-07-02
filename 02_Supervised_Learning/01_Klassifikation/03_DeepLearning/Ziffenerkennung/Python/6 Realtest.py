import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtGui import QPainter, QPen, QImage
from PyQt5.QtCore import Qt, QPoint
import numpy as np
from PIL import Image
import joblib

class Ziffern_Test(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Test auf Digitalen Ziffern")
        self.setGeometry(100, 100, 300, 350)

        # Bild auf dem gezeichnet wird
        self.image = QImage(280, 280, QImage.Format_RGB32)
        self.image.fill(Qt.black)

        self.drawing = False
        self.last_point = QPoint()

        # Button für Überprüfung
        self.button = QPushButton("Check")
        self.button.clicked.connect(self.check_digit)

        # Vertikales Layout erstellen
        layout = QVBoxLayout()
        layout.addStretch()
        layout.addWidget(self.button)
        self.setLayout(layout)

        # Modell laden
        self.model = joblib.load('digits_model.pkl')

    def mousePressEvent(self, event):
        self.drawing = True
        self.last_point = event.pos()

    def mouseMoveEvent(self, event):
        if self.drawing:
            painter = QPainter(self.image)
            pen = QPen(Qt.white, 20, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
            painter.setPen(pen)
            painter.drawLine(self.last_point, event.pos())
            self.last_point = event.pos()
            # trigger paint event
            self.update()

    def mouseReleaseEvent(self, event):
        self.drawing = False

    def paintEvent(self, event):
        canvas = QPainter(self)
        canvas.drawImage(10, 10, self.image)

    def check_digit(self):
        # Konvertierung des Qimage in ein PIL Image:
        # Das Bild wird als PNG gespeichert
        self.image.save("pic.png")

        # Das gespeicherte Bild wird als PIL IMage geladen
        # das convert("L") lädt das Bild mit 256 Graustufen
        img = Image.open("pic.png").convert("L")
        # Das Bild muss auf 8x8 Pixel reduziert werden, damit es mit den
        # Trainingsdaten übereinstimmt
        img = img.resize((8,8))
        # Das Bild wird in ein 8x8 Array konvertiert
        img_data = np.array(img)
        # Das Bild wird von 256 Graustufen auf 16 Graustufen konvertiert
        img_data = img_data / 16
        # Das 8x8 Array wird in ein 1 x 64 Array konverteirt
        img_data = img_data.flatten().reshape(1, -1)
        # Das konvertierte Bild wird in das NN Netz geladen und das Netz macht seine Vorhersage
        prediction = self.model.predict(img_data)
        print("Vorhersage:" + str(prediction[0]))

        # Für neue Zeichnung leeren
        self.image.fill(Qt.black)
        self.update()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    fenster = Ziffern_Test()
    fenster.show()
    sys.exit(app.exec_())
