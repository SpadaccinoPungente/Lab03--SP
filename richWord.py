
"""
Definire una classe RichWord. Ogni istanza di questa classe conterrà una parola del testo in ingresso, gestire
l’indicazione se tale parola è corretta o meno (utilizzare un boolean). Questa classe può essere utile per
filtrare le parole corrette durante l’esecuzione del programma.
"""

class RichWord:
    def __init__(self, word):
        self._word = word # this is a string
        self._correct = None #this is a bool

    @property # getter
    def correct(self):
        return self._correct

    @correct.setter # setter
    def correct(self, bool_value):
        self._correct = bool_value

    @property # getter
    def word(self):
        return self._word

    def __str__(self):
        return self._word