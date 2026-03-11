
"""
Definire una classe dictionary, che può essere parzialmente ereditata dal Lab 2 con opportune
modifiche. Questa classe avrà il compito di gestire il dizionario di una singola lingua, dovrà leggere il
file e raccogliere le informazioni in una lista locale, oltre che a dare modo alle altre classi di consultare
il dizionario.
"""

class Dictionary:
    def __init__(self):
        self._dizionario = list()

    def loadDictionary(self, path):
        with open(path, "r", encoding="utf-8") as fin:
            for riga in fin:
                self.dizionario.append(riga)

    def printAll(self):
        print(f"Stampa dizionario corrente in corso...\n")
        for parola in self.dizionario: print(parola)
        print("\nFinito!")

    @property # questo è un getter di _dict che è "nascosta"
    def dizionario(self):
        return self._dizionario

"""
class Dictionary:

    def __init__(self):
        self.dizionario_alieno = dict()

    def addWord(self, parola_aliena, traduzione):
        if parola_aliena in self.dizionario_alieno.keys():
            self.dizionario_alieno[parola_aliena].add(traduzione)
        else:
            self.dizionario_alieno[parola_aliena] = {traduzione}

    def translate(self, query):
        if query in self.dizionario_alieno:
            return self.dizionario_alieno[query]
        else:
            return None

    def translateWordWildCard(self, query):
        traduzioni_trovate = []

        indice_jolly = query.find("?") # restituisce l'indice numerico del jolly

        # string[start_index:stop_index] prende da start_index incluso fino a stop_index escluso
        prefisso = query[:indice_jolly]  # prende tutto fino al jolly (escluso)
        suffisso = query[indice_jolly + 1:]  # prende tutto dopo il jolly

        # .items() per ciclare su chiavi e valori
        for parola_aliena, lista_traduzioni in self.dizionario_alieno.items():
            if len(parola_aliena) == len(query):
                if parola_aliena.startswith(prefisso) and parola_aliena.endswith(suffisso):
                    traduzioni_trovate.extend(lista_traduzioni) # .extend() fonde due liste

        return traduzioni_trovate

    def getDizionarioAlieno(self):
        return self.dizionario_alieno
"""