d={}
d["bleu"]="blue"
d["rouge"]="red"
d["rose"]="pink"
d["vert"]="green"
d["jaune"]="yellow"
d["oiseau"]="animal à plume nb: sauf les sioux et les velociraptor "

def ajoute(mot1,mot2,d) :
        if mot1 not in d :
                d[mot1]=mot2
            
def affiche(d) :
        liste=list(d.keys())
        for i in range (0,len(liste)):
                mot=liste[i] 
                print(mot , "  ",d[mot] )
        print('\n')
                
def delete(char,dict) :
        liste=list(d.keys())
        for i in range (0,len(liste)):
                mot=liste[i]
                if char in mot :
                        del(d[mot])

affiche(d)                 
ajoute("lapin","rabbit",d)
affiche(d)
delete('e',d)
affiche(d)
delete('z',d)
affiche(d)
