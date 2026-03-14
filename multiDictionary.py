
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
        self.dictionary_ita = d.Dictionary()
        self.dictionary_ita.loadDictionary("resources/Italian.txt")

        self.dictionary_eng = d.Dictionary()
        self.dictionary_eng.loadDictionary("resources/English.txt")

        self.dictionary_spa = d.Dictionary()
        self.dictionary_spa.loadDictionary("resources/Spanish.txt")

    def printDic(self, language):
        if language == "italian":
            self.dictionary_ita.printAll()
        elif language == "english":
            self.dictionary_eng.printAll()
        elif language == "spanish":
            self.dictionary_spa.printAll()

    def searchWord(self, words, language):
        rich_words = []
        selected_dictionary = self.selectDictionary(language)

        for word in words:
            new_rw = rw.RichWord(word)
            rich_words.append(new_rw)

            # non esiste .contains() per le liste ma l'operatore in utilizza un __contains__
            if new_rw.word in selected_dictionary:
                new_rw.correct = True
            else:
                new_rw.correct = False

        return rich_words


    # Esercizio 2

    """
    Iterare su tutti gli elementi del vocabolario a partire dal primo. La ricerca termina quando viene trovato 
    l’elemento cercato o si raggiunge l’ultimo, nel caso in cui l’elemento cercato non sia presente nella lista. 
    """
    def searchWordLinear(self, words, language):
        rich_words = []
        selected_dictionary = self.selectDictionary(language)

        for word in words:
            new_rw = rw.RichWord(word)
            rich_words.append(new_rw)

            # ricerca lineare
            new_rw.correct = False # assumiamo che sia errata all'inizio
            for elem in selected_dictionary:
                if new_rw.word == elem:
                    new_rw.correct = True  # trovata!
                    break  # interrompiamo il ciclo

        return rich_words

    """
    Sapendo che il vocabolario è ordinato alfabeticamente, l'idea è quella di non iniziare la ricerca dal primo 
    elemento, ma da quello centrale, cioè a metà del dizionario. 
    
    Si confronta questo elemento con quello cercato:
    - se corrisponde, la ricerca termina indicando che l'elemento è stato trovato 
    - se è superiore, la ricerca viene ripetuta sugli elementi precedenti (ovvero sulla prima metà del 
    dizionario), scartando quelli successivi 
    - se è inferiore, la ricerca viene ripetuta sugli elementi successivi (ovvero sulla seconda metà del 
    dizionario), scartando quelli precedenti. 
    
    Il procedimento viene ripetuto iterativamente fino a quando o si trova l’elemento cercato, o tutti gli elementi 
    vengono scartati. In quest’ultimo caso la ricerca termina indicando che il valore non è stato trovato. 
    """
    def searchWordDichotomic(self, words, language):
        rich_words = []
        selected_dictionary = self.selectDictionary(language)

        for word in words:
            new_rw = rw.RichWord(word)
            rich_words.append(new_rw)

            # ricerca dicotomica
            """
            ciclo while e tre variabili che fanno da "puntatori" per gli indici della lista:
                - inizio: parte da 0
                - fine: parte dalla lunghezza del dizionario meno uno (len(selected_dictionary) - 1)
                - mezzo: calcolato a ogni iterazione del ciclo.
            """
            new_rw.correct = False  # assumiamo che sia errata all'inizio

            start = 0
            end = len(selected_dictionary) - 1
            while start <= end:

                middle = (start + end) // 2 # da calcolarsi a ogni iterazione

                if new_rw.word == selected_dictionary[middle]:
                    new_rw.correct = True  # trovato, termina la ricerca
                    break
                elif new_rw.word < selected_dictionary[middle]:
                    # la parola viene prima alfabeticamente: scartiamo la seconda metà
                    end = middle - 1
                else:
                    # la parola viene dopo alfabeticamente: scartiamo la prima metà
                    start = middle + 1

        return rich_words

    def selectDictionary(self, language):
        if language == "italian":
            selected_dictionary = self.dictionary_ita.dictionary
        elif language == "english":
            selected_dictionary = self.dictionary_eng.dictionary
        elif language == "spanish":
            selected_dictionary = self.dictionary_spa.dictionary
        else: raise ValueError(f"Lingua '{language}' non supportata.")
        return selected_dictionary


