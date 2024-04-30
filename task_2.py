import logging

logging.basicConfig(level=logging.DEBUG, format="%(message)s")

def user_initial():
    x = input(
        "Podaj działanie, posługując się odpowiednią liczbą:"
        "\n"
        "1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
    
    return x


def user_in():
    try:
        a = float(input("Wpisz składnik 1: "))
        b = float(input("Wpisz składnik 2: "))
    except ValueError:
        print("to nie liczba")
        exit()
        
    return a, b


def user_in_extended():
    z = input("Dalsze liczby: ")
    z=z.split()
    try:
        for element in z:
            float(element)
            
    except ValueError:
        print("to nie liczba")
        exit()
    
    return z 


def add(a,b,*numbers_list):
    logging.debug(f"Dodaję {a} i {b}")
    
    logging.debug(f"i dodaję {numbers_list}")
    sum=a+b
    for element in numbers_list:
        sum+=float(element)
        
    return sum


def sub(a,b,*numbers_list):
    logging.debug(f"Odejmuję {a} i {b}")
    sub=a-b

    return sub


def mul(a,b,*numbers_list):
    logging.debug(f"Multiplikuję {a} i {b}")
    
    logging.debug(f"i multiplikuję {numbers_list}")
    prod=1
    for element in numbers_list:
        prod=prod*float(element)
        
    return prod*a*b


def div(a,b,*numbers_list):
    logging.debug(f"Dzielę {a} i {b}")
    quo=a/b

    return quo


calculator = {"1": add, "2": sub, "3": mul, "4": div}


if __name__ == "__main__":
    x = user_initial()
    a,b=user_in()
    numbers_list=[]
    if x=="1" or x=="3":
        numbers_list=user_in_extended()
        
    print(f"Wynik to {calculator[x](a,b,*numbers_list)}")
