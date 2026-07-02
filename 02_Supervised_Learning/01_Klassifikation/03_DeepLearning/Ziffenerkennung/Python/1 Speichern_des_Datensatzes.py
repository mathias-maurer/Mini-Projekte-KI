from sklearn import datasets
import matplotlib.pyplot as plt

digits = datasets.load_digits()
# print(len(digits.images))

# Speichere die ersten 200 Bilder
for i in range(200):
    image = digits.images[i]
    label = digits.target[i]
    filename = "bilder/bild" + str(i) + "_" + str(label) + ".png"
    plt.imsave(filename, image, cmap='gray')

print("Bilder gespeichert!")