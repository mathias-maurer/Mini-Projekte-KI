from sklearn.neural_network import MLPClassifier
from sklearn import datasets
from sklearn.model_selection import train_test_split
import joblib

# Datensatz laden
digits = datasets.load_digits()

# 70% sind Trainingsdaten, 30% sind Testdaten
bilder_train, bilder_test, labels_train, labels_test = train_test_split(
    digits.data, digits.target, test_size=0.3, random_state=42)

# Modell erzeugen: 50 neuronen in der hidden layer
model = MLPClassifier(hidden_layer_sizes=(50,), max_iter=500, verbose = True)

# Training
model.fit(bilder_train, labels_train)

# Auswertung
print("Genauigkeit mit Trainingsdaten :", model.score(bilder_train, labels_train))
print("Genauigkeit mit Testdaten :", model.score(bilder_test, labels_test))

# Modell speichern
joblib.dump(model, 'digits_model.pkl')