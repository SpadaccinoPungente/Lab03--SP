
"""
Definire una classe MultiDictionary che gestirà l’accesso ai vari dizionari a lingua singola, e
implementerà gli algoritmi di ricerca. Il metodo searchWord sarà dedicato a cercare una specifica parola
nel dizionario della lingua selezionata e restituisce una lista di RichWord, con indicazione se la parola
è stata trovata nel dizionario (e quindi è corretta) oppure no.
"""

import dictionary as d
import richWord as rw


class MultiDictionary:

    def __init__(self):
       self.dizionario_italiano = d.Dictionary()
       self.dizionario_inglese = d.Dictionary()
       self.dizionario_spagnolo = d.Dictionary()

    def printDic(self, language):
        if language == "italian":
            self.dizionario_italiano.printAll()
        elif language == "english":
            self.dizionario_inglese.printAll()
        elif language == "spanish":
            self.dizionario_spagnolo.printAll()

    def searchWords(self, words, language):
        parole_errate = []
        # dovrà ritornare un lista di parole errate

    # Esercizio 2

    def searchWordLinear(self):
        pass

    def searchWordDichotomic(self):
        pass


