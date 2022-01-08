# **Caesar-Verschlüsselung**

Die Caesar-Verschlüsselung ist eine der ältesten bekannten Verschlüsselungsmethoden. Sie ist jedoch sehr unsicher und kann sogar ohne Computerunterstützung schnell geknackt werden.


## Vorgehen zum Verschlüsseln

Bei der Caesar-Verschlüsselung wird jeder Buchstabe der Nachricht um eine bestimmte Zahl im Alphabet weitergeschoben. Diese Zahl ist der geheime Schlüssel.

![Caesar Verschlüsselung](https://upload.wikimedia.org/wikipedia/commons/2/2b/Caesar3.svg)

Wählt man zum Beispiel den Schlüssel **3**, so wird aus einem **A** (1. Buchstabe im Alphabet) ein **D** (4. Buchstabe), aus einem **B** ein **E**, aus einem **C** ein **F** usw.

Gelangt man bei der Verschiebung über Z hinaus, so wird wieder bei A begonnen.Also wird in dem Beispiel mit dem Schlüssel 3 das **X** durch **A**, **Y** durch **B** und **Z** durch **C** ersetzt.

## Vorgehen zum Entschlüsseln

Zum Entschlüsseln verwendet man den geheimen Schlüssel und verschiebt alle Buchstaben im Geheimtext um diese Zahl im Alphabet zurück.

## **Sicherheit**

Das Verfahren ist sehr unsicher. Die eigentliche Sicherheit bestand früher darin, dass das Verfahren unbekannt war. Ein gutes / sicheres Verschlüsselungsverfahren sollte jedoch allein auf der Geheimhaltung des Schlüssels, nicht auf der Geheimhaltung des Algorithmus basieren. Bei der Beurteilung der Sicherheit geht man deswegen davon aus, dass man das Verschlüsselungsverfahren kennt, den Schlüssel jedoch nicht.

Da es nur 25 unterschiedliche Schlüssel gibt, kann man alle Möglichkeiten in relativ kurzer Zeit durchprobieren.

Meistens genügen auch bereits die ersten Buchstaben um zu erkennen, ob der Schlüssel richtig ist: Bei dem Geheimtext oben ist der Anfang "TLP", probiert man den Schlüssel **2** aus (2 Buchstaben zurück rotieren) ergiebt sich der Klartext "RJN". Dass der Text mit diesen Buchstaben anfängt ist nicht sehr wahrscheinlich und man kann den nächsten Schlüssel probieren.

## **Wie könnte man die Caesar-Verschlüsselung etwas sicherer machen?**

Eine Möglichkeit besteht darin, zusätzlich zu den Großbuchstaben auch Kleinbuchstaben und Sonderzeichen zuzulassen und zu verschlüsseln. Dies erhöht nämlich die Anzahl der möglichen Verschiebungen. Sicher ist das Verfahren aber auch dann nicht.

Mit größerer Abweichung von dem ursprünglichen Caesar-Algorithmus gibt es die Vigenère-Verschlüsselung. Dabei wird nicht nur eine Zahl bzw. ein Schlüsselbuchstabe wie bei dem Caesar-Algorithmus verwendet, sondern mehrere. Wählt man z.B. die Schlüsselbuchstaben T O R, so wird der erste Buchstabe wie im Caesar-Algorithmus mit T verschoben, der 2. aber mit O (nicht auch mit T), und der 3. mit R, der 4. wieder mit T, der 5. mit O usw.

Dies erhöht die Sicherheit enorm, wenn man lange Schlüssel wählt - bis hin zur perfekten Sicherheit: dem One-Time-Pad!
