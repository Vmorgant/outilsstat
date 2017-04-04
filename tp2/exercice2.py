def ascii (mot):
    valeur=0
    for i in range(0,len(mot)) :
                   valeur+=ord(mot[i])*256**(len(mot)-(i+1))
    print(valeur)
    
def h (mot):
    valeur=0
    for i in range(0,len(mot)) :
                   valeur+=ord(mot[i])*256**(len(mot)-(i+1))
    valeur=valeur%255
    print(valeur)

ascii("toto")
h("toto")
h("ttoo")
h("otot")
