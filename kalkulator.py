print("Witaj w kalkulatorze kondensatorów")     # Powitanie i Autor
print("Made by: CZERWONY")

print("")
print("Jakie ma to być połączenie", '\n', "1-równoległe", '\n', "2-szeregowe")  # Pytanie
question = input()

if question == "1":                             # Obliczanie równoległe
    print("podaj wartość 1 kondensatora: ")
    a = int(input())
    print("podaj wartość 2 kondensatora: ")
    b = int(input())
    
    print(a + b,"F")
    
if question == "2":                             # Obliczanie szeregowe
    print("podaj wartość 1 kondensatora: ")
    a = int(input())
    print("podaj wartość 2 kondensatora: ")
    b = int(input())
    
    c = (1/a) + (1/b)
    
    print(1/c,"F")
    
# Cześć, jestem kodem :D
