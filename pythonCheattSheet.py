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