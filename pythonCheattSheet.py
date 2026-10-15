import os
os.system("cls")

# Dies ist ein kleines Cheat-Sheet fuer die Verwendung von Python fuer C und C++ Programmierer.


# Variable
#int eineZahl = 43;
eineVariable = 13
print ("eineVariable =", eineVariable)
eineVariable = "blablabla"
print ("eineVariable =", eineVariable)

# Typisierung in Python: Ducktyping

# Daher: bitte immer nach moeglichkeit typisieren:
eineZweiteVariable : int = 14
print ("eineZweiteVariable =", eineZweiteVariable**3)
eineZweiteVariable = "text"
# erzeugt leider erst den fehler zur laufzeit
#print ("eineZweiteVariable =", eineZweiteVariable**3)

datenTyp = type(eineVariable)
print ("datenTyp von eineVariable =", datenTyp)

eineVariable = 15

datenTyp = type(eineVariable)
print ("datenTyp von eineVariable =", datenTyp)

# formatierte Ausgabe
# C: printf("Zahl lautet %i \n und ist Cool!", eineVariable);
#print("Zahl lautet %i \nund ist Cool!" % eineVariable)
# formatierte strings
einText = f"Zahl lautet {eineVariable**2} und ist cool!"
print(einText)

# Eingabe von der Kommandozeile C:
#int i = 0
#printf("Bitte eine Zahl eingeben:\n");
#scanf = (&i);

eingeleseneZahl = int (input("Bitte Zahl eingeben: "))
print ("Zahl eingelesen vom typ", type(eingeleseneZahl))