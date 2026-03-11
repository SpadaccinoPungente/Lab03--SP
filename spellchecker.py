
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
        clean_text = replaceChars(txtIn)
        clean_text = clean_text.lower()
        words = clean_text.split(" ")
        words = [p for p in words if p != ""] # elimina parole vuote dovute a doppi spazi

        # tempo e avvio della ricerca
        print("Using contains")

        start_time = time.time()

        # riceviamo TUTTE le parole convertite in oggetti RichWord
        rich_words_list = self.multiDict.searchWords(words, language)

        end_time = time.time()
        time_elapsed = end_time - start_time

        #
        misspelled_words = []
        for rw in rich_words_list:
            if not rw.correct:  # attributo correct è False
                misspelled_words.append(rw)

        # output
        for word in misspelled_words:
            print(word)  # funziona grazie al def __str__ di RichWord

        print(f"Numero di parole errate: {len(misspelled_words)}")
        print(f"Time elapsed: {time_elapsed}")

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