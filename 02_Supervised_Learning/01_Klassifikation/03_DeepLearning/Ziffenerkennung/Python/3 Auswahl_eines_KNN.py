from sklearn.neural_network import MLPClassifier

# MLPClassifier ist ein Multilayer Perceptron (MLP) aus der Familie der neuronalen Netze.
# Es ist ein Feedforward-Netzwerk:
# Es hat mindestens 3 Schichten: Eingabeschicht → versteckte Schicht(en) → Ausgabeschicht
# Signale fließen nur in eine Richtung (keine Rückkopplungen, kein RNN)


# ACHTUNG: Die Anzahl der Neuronen in der Eingangsschicht entspricht der Anzahl der Merkmale (Features) deiner Eingabedaten.
# die Anzahl der Neuronen der Ausgangsschicht  wird automatisch anhand der Zielwerte (y) beim Training festgelegt.
# max_iter = Anzahl der maximalen Epochen
# Wenn das Modell vorher schon gut genug ist, kann es aber auch früher stoppen (abhängig von tol und early_stopping).
# tol steht für Tolerance (Toleranz) und gibt an, ab welchem minimalen Verbesserungswert das Training als „konvergiert“ gilt und gestoppt wird.

model = MLPClassifier(hidden_layer_sizes=(50,), max_iter=500)
params = model.get_params()
for key, value in params.items():
    print(key + " : " + str(value))

# Parameter	            Bedeutung	                                                    Standardwert
#hidden_layer_sizes	    Tuple mit der Größe jeder versteckten Schicht (z. B. (100,))	(100,)
#activation	            Aktivierungsfunktion: 'relu', 'tanh', 'logistic', 'identity'	'relu'
#solver	                Optimierer:     'adam', 'sgd', 'lbfgs'	                        'adam'
#alpha	                L2-Regularisierung (Gewichtungsbestrafung)	                    0.0001
#batch_size	            Größe der Mini-Batches (int oder 'auto')	                    'auto'
#learning_rate	        Lernratenstrategie: 'constant', 'invscaling', 'adaptive'	    'constant'
#learning_rate_init	    Anfangslernrate	                                                0.001
#max_iter   	        Maximale Anzahl Iterationen (Epochen)	                        200
#tol	                Toleranz für Optimierungsstopp	                                1e-4
#early_stopping	        Frühzeitiges Stoppen bei stagnierender Leistung (nur mit adam/sgd)	False
#shuffle	            Trainingsdaten bei jedem Durchgang mischen	                    True
#random_state	        Zufallsstart reproduzierbar machen	                            None
#momentum	            Nur bei sgd: Momentum-Faktor	                                0.9
#n_iter_no_change	    Anzahl Iterationen ohne Verbesserung bis Stop	                10
#verbose	            Trainingsfortschritt ausgeben	                                False