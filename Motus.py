import random
from colorama import init
from colorama import Fore, Back, Style
init()

print("bienvenu au jeu Motus, un mot va etre désigné aléatoirement.")

motPossible=["carton","europe","manger","courir","joyeux","angles","bonbon","cancre","zephyr","zygote" ]#declaration des mots que l'on peut trouver
motATrouver=motPossible[random.randint(1,len(motPossible)-1)]#choisit un mot a trouver aleatoire
couleur=False
motTrouve=False
tabCouleur=["*","*","*","*","*","*"]
compteurEssai=8#compteur d'essai

while (motTrouve!=True and compteurEssai!=0):#boucle de jeu principale
    tabCouleur=["*","*","*","*","*","*"]
    print(motATrouver)
    print(Back.BLACK +"rentrer un mot de 6 lettres")
    motCandidat=input()
    for i in range(len(motATrouver)):#on parcourt une première fois pour recenser tous les rouges
        if (motATrouver[i] == motCandidat[i]):
            tabCouleur[i]="rouge"
            
    for i in range(len(motATrouver)):#deuxième parcourt pour les bleu et jaune
        couleur=False
        compteurIdentiqueMotATrouve=0
        compteurIdentique=0
        for j in range(len(motATrouver)):#compte le nombre d'occurence dans le mot a trouver
            if (motCandidat[i]==motATrouver[j]):
                if (tabCouleur[j]!="rouge"):
                    compteurIdentiqueMotATrouve=compteurIdentiqueMotATrouve+1
                    
        for j in range(len(motCandidat)-(6-i)):#compte le nombre d'occurence dans le mot que l'on ecrit
            if (motCandidat[i]==motCandidat[j]):
                compteurIdentique=compteurIdentique+1
                
        for j in range(len(motATrouver)):    
            if (motCandidat[i]==motATrouver[j] and compteurIdentique<compteurIdentiqueMotATrouve and tabCouleur[i]=="*"):

                tabCouleur[i]="yellow"
                
        if (tabCouleur[i]=="*"):
            tabCouleur[i]="blue"

    for i in range(len(motCandidat)):#affichage du mot que l'on a essaye avec indication
        if (tabCouleur[i]=="rouge"):
            print(Back.RED +motCandidat[i] , end=" ")
        if (tabCouleur[i]=="yellow"):
            print(Back.YELLOW +motCandidat[i] , end=" ")
        if (tabCouleur[i]=="blue"):
            print(Back.BLUE +motCandidat[i] , end=" ")
            
    if (motATrouver == motCandidat):#condition de victoire
        motTrouve=True
        print("Bravo vous avez gagne")
            
    compteurEssai=compteurEssai-1
    print("il vous reste ",compteurEssai," essais.")
    if (compteurEssai==0):#condition de defaite
        print("vous avez perdu")
    
