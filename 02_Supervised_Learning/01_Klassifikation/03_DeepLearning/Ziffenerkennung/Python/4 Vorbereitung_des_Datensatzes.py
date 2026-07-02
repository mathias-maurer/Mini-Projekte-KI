from sklearn import datasets
from sklearn.model_selection import train_test_split

# Datensatz laden
digits = datasets.load_digits()


# 70% sind Trainingsdaten, 30% sind Testdaten
bilder_train, bilder_test, labels_train, labels_test = train_test_split(
    digits.data, digits.target, test_size=0.3, random_state=42)

print("Bilder für das Training: " , len(bilder_train) )
print(bilder_train)
print("Labels für das Training: " , len(labels_train))
print(labels_train)
print("Bilder für den Test:  " , len(bilder_test) )
print(bilder_train)
print("Labels für den Test:" , len(labels_test))
print(labels_train)
