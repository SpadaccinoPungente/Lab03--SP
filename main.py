import spellchecker

sc = spellchecker.SpellChecker()

running = True

while running:

    sc.printMenu()

    txtIn = input()

    acceptable_inputs = {"1", "2", "3", "4"}

    if txtIn not in acceptable_inputs:
        print("Scelta non valida, riprova.")
        continue

    if txtIn == "1":
        print("Inserisci la tua frase in Italiano\n")
        txtIn = input()
        sc.handleSentence(txtIn,"italian")

    elif txtIn == "2":
        print("Inserisci la tua frase in Inglese\n")
        txtIn = input()
        sc.handleSentence(txtIn,"english")

    elif txtIn == "3":
        print("Inserisci la tua frase in Spagnolo\n")
        txtIn = input()
        sc.handleSentence(txtIn,"spanish")

    elif txtIn == "4":
        print("Ok, termino programma.")
        running = False



