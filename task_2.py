import logging

logging.basicConfig(level=logging.DEBUG, format="%(message)s")

def user_initial():
    print("Napisz gotowe, gdy wszystkie liczby do większego zadania zostały podane")
    x = input(
        "Podaj działanie, posługując się odpowiednią liczbą:"
        "\n"
        "1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
    
    return x

x = user_initial()

def user_in():
    try:
        a = float(input("Wpisz składnik 1: "))
        b = float(input("Wpisz składnik 2: "))
    except ValueError:
        print("to nie liczba")
        exit()
        
    return a, b

def user_in_extended():
    z = ""
    my_list = []
    my_list.clear()
    while z != "gotowe":
        z = input("Dalsza liczba: ")
        my_list.append((z))

        try:
            float(z)
        except ValueError:
            if z == "gotowe":
                my_list.remove("gotowe")
                break
            print("to nie liczba")
            exit()

    return my_list

def add():
    in_values = [float(i) for i in user_in()]
    in_values_extended = [float(i) for i in user_in_extended()]
    logging.debug(f"Dodaję {in_values[0]} i {in_values[1]}")
    if len(in_values_extended) > 0:
        logging.debug(f"i dodaję {in_values_extended[::]} ")
        
    return f"Wynik to {sum(in_values_extended)+in_values[0]+in_values[1]}"

def sub():
    in_values = [float(i) for i in user_in()]
    logging.debug(f"Odejmuję {in_values[0]} i {in_values[1]}")
    diff = in_values[0] - in_values[1]

    return f"Wynik to {diff}"

def mul():
    prod = 1
    in_values = [float(i) for i in user_in()]
    in_values_extended = [float(i) for i in user_in_extended()]
    logging.debug(f"Multiplikuję {in_values[0]} i {in_values[1]}")
    if len(in_values_extended) > 0:
        logging.debug(f"i multiplikuję {in_values_extended[::]} ")
    for x in in_values_extended:
        prod = prod * x

    return f"Wynik to {prod*in_values[0]*in_values[1]}"

def div():
    in_values = [float(i) for i in user_in()]
    logging.debug(f"Dzielę {in_values[0]} i {in_values[1]}")
    quo = in_values[0] / in_values[1]
    
    return f"Wynik to {quo}"

calculator = {"1": add, "2": sub, "3": mul, "4": div}

print(calculator[x]())
