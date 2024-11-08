"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Petr Král
email: petr.kral36@seznam.cz
"""
def pozdrav():
    print("Vítejte ve hře Tic-tac-toe!")
    print("Cílem hry je umístit tři hrací kameny (X nebo O) v řadě horizontálně, vertikálně nebo diagonálně.")
    print("Hra je určena pro dva hráče, kteří se střídají v tahu.")

def pravidla_hry():
    print("\nPravidla:")
    print("1. Hrací pole je očíslováno od 1 do 9.")
    print("2. Každý hráč si zvolí číslo pozice, kam chce umístit svůj symbol (X nebo O).")
    print("3. Cílem je získat tři symboly v řadě, sloupci nebo diagonále.")
    print("4. Pokud je hrací pole plné a nikdo nevyhrál, jde o remízu.")
    print("")

def zobraz_hraci_pole(pole):
    print("\n")
    print("+---+---+---+")
    print(f"| {pole[0]} | {pole[1]} | {pole[2]} |")
    print("+---+---+---+")
    print(f"| {pole[3]} | {pole[4]} | {pole[5]} |")
    print("+---+---+---+")
    print(f"| {pole[6]} | {pole[7]} | {pole[8]} |")
    print("+---+---+---+")
    print("\n")

def vyber_pozici(pole, symbol):
    while True:
        try:
            pozice = int(input(f"Hráč '{symbol}', zadejte číslo pozice (1-9): ")) - 1
            if pozice < 0 or pozice > 8:
                print("Neplatná pozice. Zadejte číslo mezi 1 a 9.")
            elif pole[pozice] != " ":
                print("Toto pole je již obsazeno. Vyberte jiné.")
            else:
                return pozice
        except ValueError:
            print("Neplatný vstup. Zadejte číslo mezi 1 a 9.")

def zkontroluj_vyhru(pole, symbol):
    vyherni_kombinace = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # horizontálně
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # vertikálně
        [0, 4, 8], [2, 4, 6]             # diagonálně
    ]
    for kombinace in vyherni_kombinace:
        if all(pole[i] == symbol for i in kombinace):
            return True
    return False

def je_remiza(pole):
    return all(p != " " for p in pole)

def hra():
    pozdrav()
    pravidla_hry()

    pole = [" "] * 9
    aktualni_hrac = "X"

    while True:
        zobraz_hraci_pole(pole)
        pozice = vyber_pozici(pole, aktualni_hrac)
        pole[pozice] = aktualni_hrac

        if zkontroluj_vyhru(pole, aktualni_hrac):
            zobraz_hraci_pole(pole)
            print(f"Hráč '{aktualni_hrac}' vyhrál! Gratulujeme!")
            break
        elif je_remiza(pole):
            zobraz_hraci_pole(pole)
            print("Hra skončila remízou!")
            break

        aktualni_hrac = "O" if aktualni_hrac == "X" else "X"

hra()