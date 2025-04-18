def main(): 
    program = input("Wybierz program: kalkulator [1], konwerter [2], srednia [3]\n")
    while program not in ("1", "2", "3"):
        program = input("Nieprawidlowy program, wybierz ponownie: ")
 
    match program:
        case "1":
            operacja = input("Podaj operacje: [+], [-], [*], [/]\n")
            while operacja not in ("+", "-", "*", "/"):
                operacja = input("Nieprawidlowa operacja, wybierz ponownie: ")
 
            x = float(input("Podaj pierwsza liczbe: "))
            y = float(input("Podaj druga liczbe: "))
 
            if operacja == "+":
                wynik = x + y
            elif operacja == "-":
                wynik = x - y
            elif operacja == "*":
                wynik = x * y
            elif operacja == "/":
                while y == 0:
                    print("Nie mozna dzielic przez 0")
                    y = float(input("Podaj druga liczbe: "))
                wynik = x / y;
 
            print(f"Wynik: {wynik}")
        
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
                print(f"{temp}°C = {wynik:.2f}°F")
            elif operacja == "f":
                wynik = naCelcjusz(temp)
                print(f"{temp}°F = {wynik:.2f}°C")
            
        case "3":
            ileOcen = int(input("Podaj liczbe ocen: "))
            srednia = 0
            
            for x in range(0, ileOcen):
                ocena = float(input(f"Podaj ocene {x+1}: "))
                while ocena not in range(1, 7):
                    ocena = float(input("Nieprawidlowa ocena, podaj ponownie: "))
                srednia = srednia + ocena
            srednia = srednia / ileOcen
            
            print(f"Srednia: {srednia:.2f}")
            if srednia < 3:
                print("Uczen nie zdal.")
            else:
                print("Uczen zdal.")

if __name__ == "__main__": 
    main()
