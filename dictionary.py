
"""
Definire una classe dictionary, che può essere parzialmente ereditata dal Lab 2 con opportune
modifiche. Questa classe avrà il compito di gestire il dizionario di una singola lingua, dovrà leggere il
file e raccogliere le informazioni in una lista locale, oltre che a dare modo alle altre classi di consultare
il dizionario.
"""

class Dictionary:
    def __init__(self):
        self._dictionary = list()

    def loadDictionary(self, path):
        with open(path, "r", encoding="utf-8") as fin:
            for riga in fin:
                self.dictionary.append(riga.strip().lower())

    def printAll(self):
        print(f"Stampa dizionario corrente in corso...\n")
        for word in self.dictionary: print(word)
        print("\nFinito!")

    @property # getter
    def dictionary(self):
        return self._dictionary