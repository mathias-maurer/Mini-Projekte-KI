from pathlib import Path
import random
import shutil

# Pfade
original = Path("./garbage_classification_enhanced")
neu = Path("./garbage_classification_enhanced_500")

# Unterordner für Datensätze
train_ordner = neu / "train"
test_ordner = neu / "test"

# Bildformate
bild_endungen = {".jpg", ".jpeg", ".png", ".bmp", ".gif", ".webp"}

# Anzahl Bilder pro Klasse
anzahl_train = 500
anzahl_test = int(anzahl_train * 0.2)

# Falls reproduzierbare Zufallsauswahl gewünscht:
# random.seed(42)

# Hauptordner anlegen
train_ordner.mkdir(parents=True, exist_ok=True)
test_ordner.mkdir(parents=True, exist_ok=True)

for ordner in original.iterdir():
    if ordner.is_dir():

        # Klassenordner in train und test anlegen
        ziel_train = train_ordner / ordner.name
        ziel_test = test_ordner / ordner.name

        ziel_train.mkdir(parents=True, exist_ok=True)
        ziel_test.mkdir(parents=True, exist_ok=True)

        # Bilder sammeln
        bilder = [
            datei for datei in ordner.iterdir()
            if datei.is_file() and datei.suffix.lower() in bild_endungen
        ]

        # Zufällig mischen
        random.shuffle(bilder)

        # Aufteilen
        train_bilder = bilder[:anzahl_train]
        test_bilder = bilder[anzahl_train:anzahl_train + anzahl_test]

        # Train kopieren
        for bild in train_bilder:
            shutil.copy2(bild, ziel_train / bild.name)

        # Test kopieren
        for bild in test_bilder:
            shutil.copy2(bild, ziel_test / bild.name)

        print(
            f"{ordner.name}: "
            f"{len(train_bilder)} Train / "
            f"{len(test_bilder)} Test Bilder kopiert"
        )

print("Fertig.")