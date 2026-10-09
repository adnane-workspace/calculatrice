"""Calculatrice en ligne de commande : +, -, *, /."""


def addition(a: float, b: float) -> float:
    return a + b


def soustraction(a: float, b: float) -> float:
    return a - b


def multiplication(a: float, b: float) -> float:
    return a * b


def division(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Division par zero impossible.")
    return a / b


OPERATIONS = {
    "+": addition,
    "-": soustraction,
    "*": multiplication,
    "/": division,
}


def lire_nombre(message: str) -> float:
    while True:
        saisie = input(message).strip().replace(",", ".")
        try:
            return float(saisie)
        except ValueError:
            print("Entrez un nombre valide.")


def calculer(a: float, operateur: str, b: float) -> float:
    if operateur not in OPERATIONS:
        raise ValueError(f"Operateur inconnu : {operateur}")
    return OPERATIONS[operateur](a, b)


def main() -> None:
    print("Calculatrice")
    print("Operations : +  -  *  /")
    print("Tapez q pour quitter.\n")

    while True:
        choix = input("Operation (+, -, *, / ou q) : ").strip().lower()
        if choix in {"q", "quit", "quitter"}:
            print("Au revoir.")
            break
        if choix not in OPERATIONS:
            print("Choisissez +, -, * ou /.")
            continue

        a = lire_nombre("Premier nombre : ")
        b = lire_nombre("Deuxieme nombre : ")

        try:
            resultat = calculer(a, choix, b)
        except ZeroDivisionError as erreur:
            print(erreur)
            continue

        print(f"Resultat : {resultat}\n")


if __name__ == "__main__":
    main()
