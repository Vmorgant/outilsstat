def fact(n): 
    if n<2:
        return 1
    else:
        return n*fact(n-1)

def anniversaire(nombre):
    valeur=( 1-( (fact(365)/fact(365-nombre)) / 365**nombre))
    print(valeur*100)
    
anniversaire(23)
anniversaire(10)
anniversaire(32)
    
                    
