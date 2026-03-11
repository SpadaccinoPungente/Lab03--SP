
"""
La classe SpellChecker farà da interfaccia fra l’utente e la classe MultiDictionary.
"""

import time

import multiDictionary as md

class SpellChecker:

    def __init__(self):
        self.multiDict = md.MultiDictionary()

    def handleSentence(self, txtIn, language):
        # pulizia e preparazione dell'input
        testo_pulito = replaceChars(txtIn)
        testo_pulito = testo_pulito.lower()
        parole = testo_pulito.split(" ")

        # rimuove stringhe vuote se ci sono doppi spazi
        parole = [p for p in parole if p != ""]
        print("Using contains:")

        start_time = time.time()

        parole_errate = self.multiDict.searchWords(parole, language)

        end_time = time.time()

        tempo_impiegato = end_time - start_time

        # output dei risultati
        for parola in parole_errate:
            print(parola)

        print(f"Numero di parole errate: {len(parole_errate)}")
        print(f"Time elapsed {tempo_impiegato}")


    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$%^;,=_~"
    for c in chars: text = text.replace(c, "")
    return text