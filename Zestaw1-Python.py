def main(): 
 
    program = input("Wybierz program: kalkulator [1], konwerter [2], srednia [3]\n")
    while program not in ("1", "2", "3"):
        program = input("Nieprawidlowy program, wybierz ponownie: ")
 
    match program:
        case "1":
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
        
        case "2":
            def naFarenheit(c):
                return c * 1.8 + 32
            
            def naCelcjusz(f):
                return (f - 32) / 1.8
            
            operacja = input("Celcjusz -> Farenheit [c], Farenheit -> Celcjusz [f]\n")
            while operacja not in ("c", "f"):
                operacja = input("Nieprawidlowa operacja, wybierz ponownie: ")
            
            temp = float(input("Podaj temperature do przeliczenia: "))
            
            if operacja == "c":
                wynik = naFarenheit(temp)
            elif operacja == "f":
                wynik = naCelcjusz(temp)

            print(f"Wynik = {wynik}")
 
if __name__ == "__main__": 
    main()
