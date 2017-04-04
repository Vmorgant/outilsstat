
import numpy

def perso() :
    nb_perso=int(input("Entrez un nombre de personnages: "))
    for i in range(0,nb_perso) :
        poids =  int(numpy.random.normal(70, 20,1))
        taille = int(numpy.random.normal(170, 30,1))
        print(poids)
        print(taille)
perso()
