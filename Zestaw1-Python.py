def main(): 
    def dodawanie(a, b):
        return a + b

    def odejmowanie(a, b):
        return a - b

    def mnozenie(a, b):
        return a * b

    def dzielenie(a, b):
        while b == 0:
            print("Nie mozna dzielic przez 0")
            b = float(input("Podaj druga liczbe: "))
        return a / b;

    operacja = input("Podaj operacje: [+], [-], [*], [/]\n")
    while operacja not in ("+", "-", "*", "/"):
        operacja = input("Nieprawidlowa operacja, wybierz ponownie: ")

    x = float(input("Podaj pierwsza liczbe: "))
    y = float(input("Podaj druga liczbe: "))
    
    if operacja == "+":
        wynik = dodawanie(x, y)
    elif operacja == "-":
        wynik = odejmowanie(x, y)
    elif operacja == "*":
        wynik = mnozenie(x, y)
    elif operacja == "/":
        wynik = dzielenie(x, y)

    print(f"Wynik = {wynik}")

if __name__ == "__main__": 
    main()
