
"""
La classe SpellChecker farà da interfaccia fra l’utente e la classe MultiDictionary.
"""

import time

import multiDictionary as md

class SpellChecker:

    def __init__(self):
        self.multiDict = md.MultiDictionary()

    def handleSentence(self, txtIn, language):
        # pulizia e preparazione
        clean_text = replaceChars(txtIn)
        clean_text = clean_text.lower()
        words = clean_text.split(" ")
        words = [p for p in words if p != ""]

        print("Uso contains...")
        start_time = time.time()
        rich_words_contains = self.multiDict.searchWord(words, language)
        time_elapsed = time.time() - start_time
        self.printResults(rich_words_contains, time_elapsed)

        print("Uso ricerca lineare...")
        start_time = time.time()
        rich_words_linear = self.multiDict.searchWordLinear(words, language)
        time_elapsed = time.time() - start_time
        self.printResults(rich_words_linear, time_elapsed)

        print("Uso ricerca dicotomica...")
        start_time = time.time()
        rich_words_dichotomic = self.multiDict.searchWordDichotomic(words, language)
        time_elapsed = time.time() - start_time
        self.printResults(rich_words_dichotomic, time_elapsed)

    def printResults(self, rich_words, time_elapsed):
        misspelled_rws = []
        for rw in rich_words:
            if not rw.correct:
                misspelled_rws.append(rw)

        for rw in misspelled_rws:
            print(rw) # funziona grazie al def __str__ di RichWord!

        print(f"Numero di parole errate: {len(misspelled_rws)}")
        print(f"Time elapsed: {time_elapsed}\n")

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