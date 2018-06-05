#!/user/bin/python3
# maListe = [4, 8, 415, 1, 25, 75, 6]
import math

# for i in maListe:
#     if i>i+1:
#         print("réordonner")


# minimun= min(maListe)
# print("min value= ",minimun)
#
# print("Ma liste avant tri  ", maListe)

# tri = True
# while tri:
#     tri = False
#     for i, x in enumerate(maListe):
#         if i < len(maListe)-1:
#             if maListe[i] > maListe[i + 1]:
#                  # permuter les deux valeurs
#                  tmp=maListe[i]
#                  maListe[i]=maListe[i+1]
#                  maListe[i+1]=tmp
#                  tri=True
#
#
# print("Ma liste après tri  ", maListe)

# m = 500
# i = 0
# while i <= m:
#     print(i, ")", "Je dois faire des sauvegardes régulières de mes fichiers")
#     i = i+1
#   programme qui écrit les nombres impaires de 0, à 10000

# m = 1000
# i: int = 0
# mesImpairs = []
# while i <= m:
#     # if i/2 != 0:
#     if i % 2 == 1:
#         mesImpairs.append(i)
# print(mesImpairs)

# def exo7():
# print ("donner un nombre entier")
# nbr = (input("donner un nombre entier"))
# nbr = int(nbr)
# # print(type(nbr))
#
# # for i = nbr i < nbre +10 :
# i = nbr
# while i < nbr + 10:
#     print(i)
#     i = i + 1

# nbrarticle = int(5)
# prixUnitaire = float(42.5)
# tva = float(0.2)
# prixHT = nbrarticle * prixUnitaire
# print("Nombre Article :", nbrarticle)
# print("Prix HT", prixHT)
# prixTTC = prixHT*1.2
# print("Prix TTX ", prixTTC)

# def factoriel():
#     nbr = int(input("donner un nombre : "))
#     fact = 1
#     i = 1
#     while i <= nbr:
#         fact = fact*i
#         i = i + 1
#     print("le factoriel de " + str(nbr) + " = " + str(fact))
# factoriel()


# def exo13():
#     nbr = int(input("Donner un nombre :"))
#     chainebinaire = []
#     reste=0
#
#     while nbr:
#         reste = nbr % 2
#         nbr = nbr // 2
#         chainebinaire.append(reste)
#     print(chainebinaire)
#
# exo13()

#
# def exo14():
#     somme=0
#     for i in range(1,1000):
#         if i % 3 == 0 and i % 5 == 0:
#             somme = somme + i
#     print(somme)
#
#
# exo14()


# def exo15():
#     a = 0
#     b = 11
#     c = 1
#
#     nombre = int(input("donner un nombre: "))
#     for x in range(nombre):
#         # print(a)
#         print(a, b)
#         c = a+b
#         a = b
#         b = c
#     print(c)
#
#
# exo15()

#
# def exo16():
#     val=0
#     count = []
#     while True:
#         val = val + 1
#         for i in range(1,20):
#             if val % i == 0:
#                 if val % i == 0:
#                     count.append(i)
#         if len(count) >= 19:
#             print(val)
#             break
#         print(len(count))
#         count = []
#
# exo16()


import random

# import emoji
def exo17():
    life = 9
    rand = random.randint(1, 100)
    # i =  1
    # while i < 10:
    print("randomize == " + str(rand))
    while life >= 0:
        life = life - 1
        valeur = int(input("entrer un nombre "))
        if valeur > rand:
            print("plus petit ")
        elif valeur < rand :
            print("plus grand")
        else:
            print("vous avez gagné")
            break
        # i = i + 1
    print("vous avez dépassé le nombre de tentatives")


exo17()







