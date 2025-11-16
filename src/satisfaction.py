from math import floor, ceil


'''
Il n'est pas forcément pertinent de noter la satisfaction des élèves par rapport à la position des autres élèves dans le classement des établissements car les élèves ne sont pas sensé avoir conscience de ce classement,
et donc leur satisfaction ne peut pas être impacté.
'''
def classementSatisfaction(
    y_rankings : dict[str,dict[str,int]],
    satif_x : dict[str, str],
    optimist : bool = 0)->None:
    # Comptage du rang de l'élément
    classement : dict[str, any] = {}
    for y_rank in y_rankings.values():  
        for s, rank in y_rank.items():
            if classement.get(s) != None:
                classement[s] += rank + 1
            else:
                classement[s] = rank + 1
    # Division par n, si optimiste valeur au dessus, sinon valeur en dessous 
    for i, v in classement.items():
        float_value = v/ len(satif_x)
        true_value = float_value
        if optimist:
            true_value = floor(float_value)
        else:
            true_value = ceil(float_value)
        classement[i] = int(true_value)
    above = 0
    equal = 0
    below = 0
    for key, rank in classement.items():
        diff =  rank - (satif_x[key]+1)
        if diff == 0:
            equal += 1
        elif diff > 0:
            above += 1
        else:
            below += 1
    return above, equal, below, classement

def echelle(result : dict[str,str],
    n : int,
    school_ranks : dict[str,dict[str,int]],
    candidate_ranks : dict[str,dict[str,int]])->None:
    s_satisfactions : dict[str,float]= {}
    c_satisfactions : dict[str,float]= {}
    step : float = 1 / n
    min_value = step * (n/2)
    max_value= 1.5
    max = max_value ** n 
    s_satif_total = 1
    c_satif_total = 1
    for s, c in result.items():
        s_satisfactions[s] = 1.5 - school_ranks[s][result[s]] * (1/(n-1))
        c_satisfactions[c] = 1.5 - candidate_ranks[c][s] * (1/(n-1))
        
        s_satif_total *= s_satisfactions[s]
        c_satif_total *= c_satisfactions[c]
    for key, value in sorted(s_satisfactions.items(), key=lambda item: item[1], reverse=True):
        print(f"Satisfaction de {key} : {"{:.2f}".format(value)}")
    print("")
    for key, value in sorted(c_satisfactions.items(), key=lambda item: item[1], reverse=True):
        print(f"Satisfaction de {key} : {"{:.2f}".format(value)}")
    print(f"Maximum : {max}")
    print("")
    print("Avec Logarithme")
    moy_log_s =  (s_satif_total ** (1/n) - min_value /  (max_value - min_value))
    moy_log_c =  (c_satif_total ** (1/n) - min_value /  (max_value - min_value))
    print(f"Moyenne des satisfactions : \nEcoles : {"{:.2f}".format(moy_log_s * 100)}%\nEtudiants : {"{:.2f}".format(moy_log_c* 100) }%")
    print("")
    print("Sans Logarithme")
    print(f"Moyenne des satisfactions : \nEcoles : {"{:.2f}".format((s_satif_total/  max) * 100)}%\nEtudiants : {"{:.2f}".format((c_satif_total / max)* 100) }%")
    
def bien_etre(
    satif : dict[str:int])->float:
    somme = 0
    n = len(satif)
    for key, value in satif.items():
        bien_etre_k = ((n-1)-value)/(n-1)
        somme+=bien_etre_k
    bien_etre_total : float = (1/n)*somme
    return bien_etre_total
def equite(satif_pop_x: dict[str:int], satif_pop_y: dict[str:int])->float:
    x = bien_etre(satif_pop_x)
    y = bien_etre(satif_pop_y)
    return 1 - (x-y)