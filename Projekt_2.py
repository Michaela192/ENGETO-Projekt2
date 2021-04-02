import random
ODDELOVAC = 47 * '-'

#Program pozdraví užitele a vypíše úvodní text
print('Hi there!')
print(ODDELOVAC)
print('I´ve generated a random 4 digit number for you.')
print('Let´s play a bulls and cows game.')
print(ODDELOVAC)

#Program dále vytvoří tajné 4místné číslo (číslice musí být unikátní a nesmí začínat 0)
TAJNE_CISLO = []
TAJNE_CISLO_PRVNI = int((random.random() * 10000) / 1000)
if TAJNE_CISLO_PRVNI == 10:
    TAJNE_CISLO_PRVNI = int(TAJNE_CISLO_PRVNI / 10)
TAJNE_CISLO.append(TAJNE_CISLO_PRVNI)

TAJNE_CISLO_DRUHE = int(random.random() * 9)
while TAJNE_CISLO_DRUHE == TAJNE_CISLO_PRVNI:
    TAJNE_CISLO_DRUHE = int(random.random())
TAJNE_CISLO.append(TAJNE_CISLO_DRUHE)

TAJNE_CISLO_TRETI = int(random.random() * 9)
while TAJNE_CISLO_TRETI == TAJNE_CISLO_PRVNI or TAJNE_CISLO_TRETI == TAJNE_CISLO_DRUHE:
    TAJNE_CISLO_TRETI = int(random.random())
TAJNE_CISLO.append(TAJNE_CISLO_TRETI)

TAJNE_CISLO_CTVRTE = int(random.random() * 9)
while TAJNE_CISLO_CTVRTE == TAJNE_CISLO_PRVNI or TAJNE_CISLO_CTVRTE == TAJNE_CISLO_DRUHE or TAJNE_CISLO_CTVRTE == TAJNE_CISLO_TRETI:
    TAJNE_CISLO_CTVRTE = int(random.random())
TAJNE_CISLO.append(TAJNE_CISLO_CTVRTE)

POCET_POKUSU = 0

#Hráč hádá číslo. Program jej upozorní, pokud zadá číslo kratší nebo delší než 4 čísla, pokud bude obsahovat duplicity, začínat nulou, příp. obsahovat nečíselné znaky.
while TAJNE_CISLO:
    VSTUP = input('Enter a number:')
    VSTUP_FINAL = []
    for ZNAK in VSTUP:
        VSTUP_FINAL.append(ZNAK)

    if len(VSTUP_FINAL) > 4 or len(VSTUP_FINAL) < 4:
        print('Špatně, nezadal jste 4místné číslo.')
        break

    if VSTUP_FINAL[0] == VSTUP_FINAL[1] or VSTUP_FINAL[0] == VSTUP_FINAL[2] or VSTUP_FINAL[0] == VSTUP_FINAL[3] or VSTUP_FINAL[1] == VSTUP_FINAL[2] or VSTUP_FINAL[1] == VSTUP_FINAL[3] or VSTUP_FINAL[2] == VSTUP_FINAL[3]:
        print('Špatně, zadal jste duplicitní čísla.')
        break

    if VSTUP_FINAL[0].isnumeric() and VSTUP_FINAL[1].isnumeric() and VSTUP_FINAL[2].isnumeric() and VSTUP_FINAL[3].isnumeric():
        I = 0
    else:
        print('Špatně, zadal jste nečíselné znaky.')
        break


    #for ZNAK in VSTUP_FINAL:
    #    if ZNAK.isnumeric():
    #        continue
    #    else:
    #        print('Špatně, zadal jste nečíselné znaky.')
    #        break

    VSTUP_FINAL[0] = int(VSTUP_FINAL[0])
    VSTUP_FINAL[1] = int(VSTUP_FINAL[1])
    VSTUP_FINAL[2] = int(VSTUP_FINAL[2])
    VSTUP_FINAL[3] = int(VSTUP_FINAL[3])

    #Program vyhodnotí tip uživatele. Program dále vypíše počet bull/ bulls (pokud uživatel uhodne jak číslo, tak jeho umístění), příp. cows/ cows (pokud uživatel uhodne
    # pouze číslo, ale ne jeho umístění). Vrácené ohodnocení musí brát ohled na jednotné a množné číslo ve výstupu. Tedy 1 bull a 2 bulls (stejně pro cow/cows).
    I = 0
    VYSLEDEK = {'bulls': 0, 'cows': 0}
    for ZNAK in TAJNE_CISLO:
        I2 = 0
        for ZNAK2 in VSTUP:
            if int(ZNAK2) == int(ZNAK):
                if I == I2:
                    VYSLEDEK['bulls'] += 1
                else:
                    VYSLEDEK['cows'] += 1
            I2 += 1
        I += 1

    if VYSLEDEK['bulls'] == 4:
        POCET_POKUSU += 1
        print("Correct, you've guessed the right number")
        if POCET_POKUSU == 1:
            print('in ', POCET_POKUSU, ' guess!', sep='')
        else:
            print('in ', POCET_POKUSU, ' guesses!', sep='')
        print(ODDELOVAC)
        if POCET_POKUSU == 1:
            print("That's amazing.")
        elif POCET_POKUSU == 2:
            print("That's really very good.")
        elif POCET_POKUSU == 3:
            print("That's very good.")
        elif POCET_POKUSU == 4:
            print("That's average.")
        else:
            print("That's not so good.")
        break
    else:
        POCET_POKUSU += 1
        VYSLEDEK_BULLS = str(VYSLEDEK['bulls'])
        VYSLEDEK_COWS = str(VYSLEDEK['cows'])
        if VYSLEDEK['bulls'] == 0 or VYSLEDEK['bulls'] == 1:
            VYSLEDEK_BULLS = VYSLEDEK_BULLS + ' bull'
        elif VYSLEDEK['bulls'] > 1:
            VYSLEDEK_BULLS = VYSLEDEK_BULLS + ' bulls'

        if VYSLEDEK['cows'] == 0 or VYSLEDEK['cows'] == 1:
            VYSLEDEK_COWS = VYSLEDEK_COWS + ' cow'
        elif VYSLEDEK['cows'] > 1:
            VYSLEDEK_COWS = VYSLEDEK_COWS + ' cows'
        print(VYSLEDEK_BULLS, ', ', VYSLEDEK_COWS, sep='')
        print(ODDELOVAC)