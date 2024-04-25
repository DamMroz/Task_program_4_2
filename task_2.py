import sys
import logging
logging.basicConfig(level=logging.DEBUG, format='%(message)s')


print("Napisz gotowe, gdy wszystkie liczby do większego zadania zostały podane")
x=input("Podaj działanie, posługując się odpowiednią liczbą:""\n"
      "1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
def add(a,b):
    logging.debug(f"Dodaję {sys.argv[1]} i {sys.argv[2]}")
    sum=0
    
    
    z=""  
    while z!="gotowe":
        
       
        
                
            
        print("Wpisz dodatkową liczbę albo gotowe: ",end="")
        z=input()
        
        
        sys.argv.append(z)
        if z=="gotowe":
            break

        try:
            sum=sum+float(z)   
        except ValueError:
            print("To nie liczba")
            exit()
         
    
    sys.argv.pop()
    counter=2
    for x in range(0,len(sys.argv)-3):
        counter=counter+1 
        
        logging.debug(f"Dodaję {float(sys.argv[counter])}")  
             
    print(f"Wynik to {sum+a+b}")
def sub(a,b):
        
        
                
    logging.debug(f"Odejmuję {sys.argv[1]} i {sys.argv[2]}")
    diff=a-b
    print(f"Wynik to {diff}")
def mul(a,b):
    logging.debug(f"Multiplikuję {sys.argv[1]} i {sys.argv[2]}")
    prod=1
    z=""  
    
    while z!="gotowe":
        
        print("Wpisz dodatkową liczbę albo gotowe: ", end="")
        z=input()
        
        sys.argv.append(z)
        if z=="gotowe":
            break
        try:
            prod=prod*float(z)   
        except ValueError:
            print("To nie liczba")
            exit()
        
    
    
                
    sys.argv.pop()
    counter=2
    for x in range (0,len(sys.argv)-3):
        counter=counter+1  
        logging.debug(f"Multiplikuję {float(sys.argv[counter])}")  
                 
    print(f"Wynik to {prod*a*b}")
def div(a,b):
        
        
                
        logging.debug(f"Dzielę {sys.argv[1]} i {sys.argv[2]}")
        quo=a/b
        print(f"Wynik to {quo}") 
        
           




try:
    a=float(input("Wpisz składnik 1: "))
    b=float(input("Wpisz składnik 2: ")) 
except ValueError:
    print("to nie liczba")
    exit()
       
sys.argv.append(a)
sys.argv.append(b)

calculator={"1":add,
         "2":sub,
         "3":mul,
         "4": div}

result=calculator[x](a,b)