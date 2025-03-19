
from random import randint
from time import *




############ (Outils pour les listes).
######################### Objectifs : construire des fonctions utiles pour manipuler
##################################### les listes d’entiers dans les activités suivantes.

def addition(liste1 , liste2) :
    assert len(liste1)==len(liste2), "les deux listes douvent être de même longueur"
    somme=[]
    for k in range(len(liste1)):
        s=liste1[k]+liste2[k]
        somme.append(s%100)
    return somme

#########Test de la fonction addition
#assert addition([1,2,3,4,5,6],[1,1,1,98,98,98])==[2,3,4,2,3,4]

def est_plus_petit(liste , liste_max) :
    assert len(liste)>=len(liste_max), "longueur de liste doit être supérieure ou égale à celle de liste_max"
    n=len(liste_max)
    for k in range(n):
        if liste[k]>liste_max[k]:
            return False
    return True
################"Test de la fonction est_plus_petit
#assert est_plus_petit([0,0,1,2,3,4] ,[0,0,5])==True
#assert est_plus_petit([0,10,0,1,1], [0,0,5])==False

def phrase_vers_liste(phrase):
    assert isinstance(phrase,str)==True, "L'argument doit être une chaine de caractères"
    if len(phrase)%6==0:
        liste=[]
    else:
        r=6-len(phrase)%6
        liste=r*[0]
    for c in phrase:
        liste.append(ord(c) % 100)
    return liste
############"test de la fonction phrase_vers_liste
#assert phrase_vers_liste("Vive moi !")==[0, 0, 86, 5, 18, 1, 32, 9, 11, 5, 32, 33]
#assert phrase_vers_liste("abcdef")==[97,98,99,0,1,2]

#########################################(Fonction de hachage).
##############################################################Objectifs : créer une fonction de hachage.
##########################################################################À partir d’un long message nous calculons une courte empreinte.
##########################################################################Il est difficile de trouver deux messages différents ayant la même empreinte.

def un_tour(bloc):
    assert isinstance(bloc,list)==True
    assert len(bloc)==6, "bloc doit être une liste de longueur 6"
    b0, b1, b2, b3, b4, b5 = bloc[0], bloc[1], bloc[2], bloc[3], bloc[4], bloc[5]
    b0, b1, b2, b3, b4, b5 = b0, b0+b1, b2, b2+b3, b4, b4+b5
    b0, b1, b2, b3, b4, b5 = 7*b0+1, 11*b1+1, 13*b2+1, 17*b3+1, 19*b4+1, 23*b5+1
    b0, b1, b2, b3, b4, b5 = b5, b0, b1, b2, b3, b4
    b0, b1, b2, b3, b4, b5 = b0%100, b1%100, b2%100, b3%100, b4%100, b5%100
    return [b0, b1, b2, b3, b4, b5]
###########test de la fonction un_tour
#assert un_tour([1, 1, 2, 3, 4, 5])==[8, 8, 23, 27, 86, 77]

def dix_tours(bloc):
    for k in range(10):
        bloc=un_tour(bloc)
    return bloc
############test de la fonction dix_tour
#assert dix_tours([0, 1, 2, 3, 4, 5])==[98, 95, 86, 55, 66, 75]
#assert dix_tours([1, 1, 2, 3, 4, 5])== [18, 74, 4, 42, 77, 42]

def hachage(liste):
    nbBlocs=len(liste)//6
    listeBlocs=[liste[6*k:6*(k+1)] for k in range(nbBlocs)]

    k=0
    A=listeBlocs[k]
    while k < nbBlocs-1:
        A=addition(dix_tours(A),listeBlocs[k+1])
        k=k+1
    return dix_tours(A)
##########test de la fonction de hachage
#assert hachage([0, 1, 2, 3, 4, 5, 1, 1, 1, 1, 1, 1, 10, 10, 10, 10, 10, 10])==[77, 91, 5, 91, 89, 99]

#######################################"(Preuve de travail - Minage).
######################################## Objectifs : construire un mécanisme de preuve de travail à l’aide de notre fonction de hachage.
Max = [0,0,7]

def verification_preuve_de_travail(liste,preuve):
    A=hachage(liste+preuve)
    return est_plus_petit(A[0:len(Max)],Max)

###############test de vérification de la fonction verification_preuve_de_travail
#assert verification_preuve_de_travail([0,1,2,3,4,5],[12,3,24,72,47,77])==True
#assert verification_preuve_de_travail([0,1,2,3,4,5],[0,0,2,0,61,2])==True
#assert verification_preuve_de_travail([0,1,2,3,4,5],[97,49,93,87,89,47])==False


def preuve_de_travail(liste):
    preuve=[randint(0,99) for k in range(6)]

    while verification_preuve_de_travail(liste,preuve)==False:
        preuve=[randint(0,99) for k in range(6)]
    return preuve

#############"test de la fonction preuve_travail
#assert verification_preuve_de_travail([0,1,2,3,4,5],preuve_de_travail([0,1,2,3,4,5]))==True


#################### Temps de calcul

#Max=[0,0,50]

#debut=time()
#preuve_de_travail([0,1,2,3,4,5])
#temps=time()-debut

#print("Pour Max=[0,0,50] le temps de calcul est de ",temps, "secondes")

#Max=[0,0,5]

#debut=time()
#preuve_de_travail([0,1,2,3,4,5])
#temps=time()-debut

#print("Pour Max=[0,0,5] le temps de calcul est de ",temps, "secondes")

#Max=[0,0,0]

#debut=time()
#preuve_de_travail([0,1,2,3,4,5])
#temps=time()-debut

#print("Pour Max=[0,0,0] le temps de calcul est de ",temps, "secondes")

























