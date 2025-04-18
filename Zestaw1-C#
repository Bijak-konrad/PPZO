using System;
class Program
{
    static double PodajLiczbe()
    {
        double x;
        while (!double.TryParse(Console.ReadLine(), out x))
        {
            Console.Write("Nieprawidlowa liczba, sprobuj ponownie: ");
        }
        return x;
    }

    static void Main(string[] args)
    {
        string program, operacja;
        int ileOcen, ocena;
        double x, y, temp, wynik = 0, srednia = 0;

        do
        {
            Console.Write("Wybierz program: kalkulator [1], konwerter [2], srednia [3]\n");
            program = Console.ReadLine();
        } while (program != "1" && program != "2" && program != "3" && program != "/");

        switch (program)
        {
            case "1":

                do
                {
                    Console.Write("Podaj operacje: [+], [-], [*], [/]: ");
                    operacja = Console.ReadLine();
                } while (operacja != "+" && operacja != "-" && operacja != "*" && operacja != "/");

                Console.Write("Podaj pierwsza liczbe: ");
                x = PodajLiczbe();
                Console.Write("Podaj druga liczbe: ");
                y = PodajLiczbe();

                if (operacja == "+")
                {
                    wynik = x + y;
                }
                else if (operacja == "-")
                {
                    wynik = x - y;
                }
                else if (operacja == "*")
                {
                    wynik = x * y;
                }
                else if (operacja == "/")
                {
                    while (y == 0)
                    {
                        Console.WriteLine("Nie mozna dzielic przez 0, podaj drugą liczbe:");
                        y = PodajLiczbe();
                    }
                    wynik = x / y;
                }

                Console.WriteLine($"Wynik: {wynik}");
                break;

            case "2":
                {
                    do
                    {
                        Console.Write("Celsjusz -> Fahrenheit [c], Fahrenheit -> Celsjusz [f]: ");
                        operacja = Console.ReadLine();
                    } while (operacja != "c" && operacja != "f");

                    Console.Write("Podaj temperature do przeliczenia: ");
                    temp = PodajLiczbe();

                    if (operacja == "c")
                    {
                        wynik = temp * 1.8 + 32;
                        Console.WriteLine($"{temp}°C = {wynik:F2}°F");
                    }
                    else
                    {
                        wynik = (temp - 32) / 1.8;
                        Console.WriteLine($"{temp}°F = {wynik:F2}°C");
                    }
                    break;
                }

            case "3":
                {
                    Console.Write("Podaj liczbe ocen: ");
                    while (!int.TryParse(Console.ReadLine(), out ileOcen) || ileOcen <= 0)
                    {
                        Console.Write("Nieprawidlowa liczba, sprobuj ponownie: ");
                    }

                    for (int i = 1; i <= ileOcen; i++)
                    {
                        Console.Write($"Podaj ocene {i}: ");
                        while (!int.TryParse(Console.ReadLine(), out ocena) || ocena < 1 || ocena > 6)
                        {
                            Console.Write("Nieprawidlowa ocena, podaj ponownie: ");
                        }
                        srednia += ocena;
                    }

                    srednia /= ileOcen;
                    Console.WriteLine($"Srednia: {srednia:F2}");

                    if (srednia < 3)
                        Console.WriteLine("Uczen nie zdal.");
                    else
                        Console.WriteLine("Uczen zdal.");

                    break;
                }
        }
    }
}
