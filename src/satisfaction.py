from math import floor, ceil

def classementSatisfaction(
    result : dict[str,str],
    n : int,
    school_ranks : dict[str,dict[str,int]],
    candidate_ranks : dict[str,dict[str,int]],
    optimist : bool = 0)->None:
    s_satisfactions : dict[str,float]= {}
    c_satisfactions : dict[str,float]= {}
    s_satif_total = 0
    c_satif_total = 0
    moy_s = 0
    moy_c = 0
    step = 1 / n
    
    classement : dict[str, any] = {}
    for c_rank in school_ranks.values():
        for c, rank in c_rank.items():
            if classement.get(c) != None:
                classement[c] += rank + 1
            else:
                classement[c] = rank + 1
    for s_rank in candidate_ranks.values():  
        for s, rank in s_rank.items():
            if classement.get(s) != None:
                classement[s] += rank + 1
            else:
                classement[s] = rank + 1
    for i, v in classement.items():
        float_value = v/ n
        true_value = float_value
        
        if optimist:
            true_value = floor(float_value)
        else:
            true_value = ceil(float_value)
        
        classement[i] = int(true_value)
        print(f"Le classement de {i} est de {classement[i]}")
    print("")
    for s, c in result.items():
        rank = candidate_ranks[c][s]
        dist =  (rank+1) - classement[c]
        classement[c] = 1 - step * dist
        
        rank = school_ranks[s][c]
        dist =  (rank+1) - classement[s]
        classement[s] = 1 - step * dist
    for i,v in classement.items():
        print(f"La satisfaction de {i} est de {v}%")
    return classement

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