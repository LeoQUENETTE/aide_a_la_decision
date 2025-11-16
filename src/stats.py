
def moyenne(data : list[float], geo : bool = 0):
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
    return total / n 
def moyenne_geometrique(data : list[float]):
    if data == None or len(data) == 0:
        return None
    n = len(data)
    produit = 1
    for nb in data:
        produit *= nb
    return produit ** (1/ n)
def mediane(data):
    if data == None or len(data) == 0:
        return None
    pos = len(data)//2
    return ((1-data[pos])/len(data))
def ecart_type(data):
    if data == None or len(data) == 0:
        return None
    n = len(data)
    moy = moyenne_lineaire(data)
    somme = 0
    for nb in data:
        somme += (nb - moy)**2
    return somme / (n-1)
def max(data):
    if data == None or len(data) == 0:
        return None
    return max(data)
def min(data):
    if data == None or len(data) == 0:
        return None
    return min(data)