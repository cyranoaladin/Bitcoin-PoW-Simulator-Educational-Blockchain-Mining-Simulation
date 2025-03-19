from Bitcoin import *


#################### Tes bitcoins

Livre = [ [0,0,0,0,0,0] ]

def ajout_transaction(transaction):
    assert isinstance(transaction,str)==True
    global Livre
    Livre.append(transaction)

def minage():
    global Livre
    transaction=Livre[-1]
    transaction=phrase_vers_liste(transaction)
    prec_preuve=Livre[-2]
    liste=prec_preuve+transaction
    preuve=preuve_de_travail(liste)
    Livre.append(preuve)

def verification_livre():
    global Livre
    liste=Livre[-3]+phrase_vers_liste(Livre[-2])
    preuve=Livre[-1]
    return verification_preuve_de_travail(liste,preuve)


