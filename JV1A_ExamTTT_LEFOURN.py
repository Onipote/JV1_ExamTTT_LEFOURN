#exercice 1 : fonction permettant d’afficher la grille de jeu

#def affichageGrille(ligne1, ligne2, ligne3):

ligne1 = ["-", "-", "-"]
ligne2 = ["-", "-", "-"]
ligne3 = ["-", "-", "-"]
#    return ligne1+ligne2+ligne3


#exercice 2 : fonction permettant de jouer un O ou un X
def symbole(joueur1, joueur2):
    joueur1 = "X"
    joueur2 = "O"
    return joueur1+joueur2


#exercice 3 : fonctions vérifiant si oui ou non l’un des joueurs a réussi à aligner 3 symboles sur une ligne verticale, horizontale, diagonale

#def nonAligneeLigne():
#    nonAlignee=True
#    while(nonAlignee):
#        nonAlignee=False
#        if
#

#def nonAligneColonne():
#nonAligneeColonne=True
#while(nonAligneeColonne):
#    nonAligneeColonne=False
#    if

#def nonAligneeDiagonale():
#nonAligneeDiagonale=True
#while(nonAligneeDiagonale):
#    nonAligneeDiagonale=False
#    if


#exercice 4 : fonction vérifiant si la grille est complète
#complet = False

#if ligne1[0]+ligne1[1]+ligne1[2] != "-": #si ligne 1 complete
#    complet = True
#    print("C'est complet !")

#if ligne2[0]+ligne2[1]+ligne2[2] != "-": #si ligne 2 complete
#    complet = True
#    print("C'est complet !")


#if ligne3[0]+ligne3[1]+ligne3[2] != "-": #si ligne 3 complete
#    complet = True
#    print("C'est complet !")


#exercice 5 : TTT complet
joueur1 = str(input("Joueur 1 (X), quel est votre nom ?\n"))
joueur2 = str(input("Joueur 2 (O), quel est votre nom ?\n"))


choixLigne = int(input("Sur quelle ligne souhaitez-vous placez le symbole ?\n"))
choixPosition = int(input("Choisissez la colonne : 1, 2 ou 3. \n"))

for i in range(1):
    #changement ligne 1
    if (choixLigne == 1) and (choixPosition == 1) :
        ligne1.insert(0,symbole)
        ligne1.pop()

    if (choixLigne == 1) and (choixPosition == 2) :
        ligne1.insert(1,symbole)
        ligne1.pop()

    if (choixLigne == 1) and (choixPosition == 3) :
        ligne1.insert(2,symbole)
        ligne1.pop()

    #changement ligne 2
    if (choixLigne == 2) and (choixPosition == 1) :
        ligne2.insert(0,symbole)
        ligne2.pop()

    if (choixLigne == 2) and (choixPosition == 2) :
        ligne2.insert(1,symbole)
        ligne2.pop()

    if (choixLigne == 2) and (choixPosition == 3) :
        ligne2.insert(2,symbole)
        ligne2.pop()

    #changement ligne 3
    if (choixLigne == 3) and (choixPosition == 1) :
        ligne3.insert(0,symbole)
        ligne3.pop()

    if (choixLigne == 3) and (choixPosition == 2) :
        ligne3.insert(1,symbole)
        ligne3.pop()

    if (choixLigne == 3) and (choixPosition == 3) :
        ligne3.insert(2,symbole)
        ligne3.pop()

print(ligne1)
print(ligne2)
print(ligne3)


#exercice 6 :
#Il faudrait :
#- augmenter la grille
#- mettre une fonction où la condition pour gagner doit atteindre 4 pour completer une ligne/colonne ou diagonale