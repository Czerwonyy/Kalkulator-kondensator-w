quest = input('szeregowe czy równoległe?\n>')

if quest == "szeregowe":
    suma = float(0)
    while True:
        quest = float(input('wpisz wartość\n>'))
        if quest != 0.0:
            suma += 1/quest
        else:
            print(f'wynik wynosi {round(suma, 3)} [F]')
            break
elif quest == "równoległe":
    suma = float(0)
    while True:
        quest = float(input('wpisz wartość\n>'))
        if quest != 0.0:
            suma += quest
        else:
            print(f'pojemność zastępcza wynosi {round(suma, 3)} [F]')
            break