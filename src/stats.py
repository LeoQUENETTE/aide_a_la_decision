from statistics import *
from math import sqrt
def moyenne_satif(data : list[float], geo : bool = 0):
    if geo:
        return moyenne_geometrique(data)
    return moyenne_lineaire(data)
def moyenne_lineaire(data : list[float]):
    if data == None or len(data) == 0:
        return None
    n = len(data)
    total = 0
    for nb in data:
        total += nb
    return round(total / n,2)
def moyenne_geometrique(data : list[float]):
    if data == None or len(data) == 0:
        return None
    n = len(data)
    produit = 1
    for nb in data:
        produit *= nb
    return round(produit ** (1/ n), 2)
def mediane(data):
    if data == None or len(data) == 0:
        return None
    pos = len(data)//2 + 1
    return data[pos]
def ecart_type(data):
    if data == None or len(data) == 0:
        return None
    n = len(data)
    somme = 0
    moy = mean(data)
    for nb in data:
        somme += (nb - moy)**2
    return round( sqrt(somme / n) ,2)
def max(data):
    if data == None or len(data) == 0:
        return None
    return max(data)
def min(data):
    if data == None or len(data) == 0:
        return None
    return min(data)