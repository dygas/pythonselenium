while True:
    try:
        print("podaj pierwszą niczbe")
        pierwsza_liczba = int(input())
        print('podaj druga liczbe')
        druga_liczba = int(input())
        print(pierwsza_liczba + druga_liczba)
        break
    except ValueError:
        print('podaj poprawna cyfre!');
        print('sprubuj jeszcze raz')
        continue