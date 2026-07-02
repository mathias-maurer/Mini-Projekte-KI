Balancing Pole

Das Balancing-Pole-Problem ist ein klassisches RL-Testproblem, bei dem ein Agent lernen soll, einen Stab (Pole), der auf einem Wagen (Cart) montiert ist, aufrecht zu halten.

Der Wagen kann sich nur nach links oder rechts bewegen.
Die einzige Aktion des Agenten ist also:

Wagen nach links schieben

Wagen nach rechts schieben


Der Agent bekommt pro Zeitschritt typischerweise diese Werte:

Position des Wagens

Geschwindigkeit des Wagens

Winkel des Stabs

Winkelgeschwindigkeit des Stabs

Ziel

Der Stab soll so lange wie möglich aufrecht bleiben.
Jeder Zeitschritt, in dem der Stab nicht umfällt, gibt eine Belohnung von +1.

Die Episode endet, wenn:

der Stab zu stark kippt (z. B. > 12°), oder

der Wagen aus dem Bereich fährt (z. B. x > 2.4)

Das Tutorial ist als Jupyter Notebook und als Python Quellcode verfügbar (Ordner Python)

