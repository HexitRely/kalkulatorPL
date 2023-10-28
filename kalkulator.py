#kalkualtor

#funkcja dodawania
def dodawanie(x, y):
    return x + y

#funkcja odejmowania
def odejnowanie(x, y):
    return x - y

#funkcja mnożenia
def mnożenie(x, y):
    return x * y

#funkcja dzielenia
def dzielenie(x, y):
    if y == 0:
        return "Błąd Dzielenie przez 0"
    return x / y

#menu kalkulatora

while True:
    print("Wybierz opcje: ")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. mnożenie")
    print("4. dzielenie")
    print("5. zakończ")

    wybor = input ("podaj numer operacji: ")

    if wybor == '5':
        print("kalkulator zakończy działanie")
        break

    if wybor not in ('1' , '2' , '3' , '4'):
        print("nie prawidłowy numer operacji.")
        continue

    liczba1 = float(input("podaj pierwsza liczbę: "))
    liczba2 = float(input("podaj druga liczbę: "))

    if wybor == '1':
        print("Wynik: ", dodawanie(liczba1, liczba2))
    elif wybor == '2':
        print("wynik: ", odejmowanie(liczba1, liczba2))
    elif wybor == '3':
        print("wynik: ", mnożenie(liczba1, liczba2))
    elif wybor == '4':
        print("Wybik: ", dzielenie(liczba1, liczba2))

