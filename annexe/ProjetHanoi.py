"""
Nom : LAURET
Prénom : Alexis 
Groupe : TDA/TP1

"""

from itertools import zip_longest

"""QUESTION 1 : INITIALISER LA TOUR DE HANOI"""
def initHanoi(n) : 
    listeInterne = []
    for cpt in range(n, 0, -1) : 
        listeInterne.append(cpt)
    TourHanoi = [listeInterne,[],[]]
    return TourHanoi

"""QUESTION 2 : AFFICHAGE DE LA TOUR DE HANOI """ 
def afficheHanoi(tours) :
    hauteurMax = len(max(tours, key=len))

    #On trie les élements de la liste  
    for cpt in tours : 
        cpt.sort()
    
    #Boucle pour rajouter des espaces à notre liste afin de par la suite pouvoir l'afficher verticalement 
    for cpt in range(3) : 
        if len(tours[cpt]) < hauteurMax : 
            #Variable pour calculer le nombre d'espace à rajouter
            différence = hauteurMax - len(tours[cpt])
            for cpt2 in range(différence) : 
                tours[cpt].insert(0, ' ')

    #zip de mettre les liste horinztalement, de la transposer
    listeAffichage = zip(tours[0], tours[1], tours[2])
    for cpt in listeAffichage:
        print(f"{cpt[0]}\t{cpt[1]}\t{cpt[2]}")
    print(f"[0]\t[1]\t[2]")
    #On retire les espaces engendrer par cette fonction car méthode modifie sur tout le script la liste "tours"
    for cpt2 in tours : 
        while ' ' in cpt2 : 
            cpt2.remove(' ')
    
    #On remet la tour dans le bon sens (sens inverse car j'ai fait la fonction d'initialisation en 1er, mais par la suite je me suis rendu compte que la manière donc j'ai construit BougeHanoi me posait problème)
    for cpt3 in tours : 
        cpt3.reverse()
    
"""QUESTION 3 : DEPLACER LES ELEMENTS """
def joueHanoi(tours) : 

    #On demarre la boucle et on lui demande de s'arrêter quand le 1er et le 2eme elements de la liste tours soient vide dans ce cas la on lui dit de continuer tant que les liste existent
    afficheHanoi(tours) 

    while tours[0] or tours[1] :
        #Uniquement pour un affichage joli 
        print('\n')

        #On supprime les espaces engendré par la fonctin afficheHanoi
        """VERIFICATION"""
        print(f"{tours} \n")


        source = int(input("Source : ")) 
        dest = int(input("Destination : "))

        #Condition pour vérifier si la tour source est bien remplie : 

        #Conditions pour remplir les tours destination vide :
        if not tours[source]  : 
            afficheHanoi(tours) 
            print(f"Erreur de saisie ou opérateur impossible. ".upper()) #Les fois ou la liste tour source ne possède aucun élement (Quand elle est vide)

        elif not tours[dest] : 
            tours[dest].append(tours[source][-1])
            tours[source].pop(-1)
            afficheHanoi(tours) 

        #Condition pour "déplacer" un élément qui peut être déplacer (1er element de la tours destination supérieur à celle de la tour source)
        elif tours[dest][0] > tours[source][0] : 
            tours[dest].append(tours[source][-1])
            tours[source].pop(-1)
            afficheHanoi(tours) 


        else : 
            afficheHanoi(tours) 
            print(f"Erreur de saisie ou opérateur impossible. ".upper())
    afficheHanoi(tours)
    print(f"\n")
    print(f"BRAVO VOUS AVEZ REUSSIS LA TOUR DE HANOI !") 


"""Question 3 : RESOLUTION DE LA TOUR DE HANOI"""

def bougeHanoi(tours, n, depuisTour, versTour):
    #Dans le cas ou il y a un seul disque à deplacer sur la tour depuisTour (pas d'appel recursif ici car pas nécessaire)
    if n == 1:  
        """On déplace l'unique la seule valeur présente dans liste de la tour depuisTours """   
        disqueDeplace = tours[depuisTour].pop() 
        tours[versTour].append(disqueDeplace) #On ajoute à la tour destination la seule valeur de la tours source puis le "pop" supprimera la derniere valeur, donc la seule valeur.
        afficheHanoi(tours)
        print("\n")

    # cas ou il y a plusieurs disque à deplacer 
    else:
        """On deplace les n-1 disque vers la tour intérmédiaire"""
        tourIntermediaire = 3 - depuisTour - versTour #oN DEtermine la tour intémédiaire (ex : si depuisTours = 0 et versTours= 1, tourIntermediaire)
        bougeHanoi(tours, n-1, depuisTour, tourIntermediaire) #Appel recursife 1

        """On déplace le disque restant sur la tour destination"""
        disqueDeplace = tours[depuisTour].pop() 
        tours[versTour].append(disqueDeplace)
    
        afficheHanoi(tours)
        
        """On déplace donc ce qu'il y a dans la toursIntermediaire vers la tour source """
        bougeHanoi(tours, n-1, tourIntermediaire, versTour)#Appel recursife 2
        print("\n")


# Exemple d'utilisation de la question 3
tailleTours = int(input(f"Quel taille votre tours ? "))
tours = initHanoi(tailleTours)
n = len(tours[0]) 
depuisTour = int(input(f"Quel tours source ? "))
versTours = int(input(f"Quel tours destination ? "))

bougeHanoi(tours, n, depuisTour, versTours)






