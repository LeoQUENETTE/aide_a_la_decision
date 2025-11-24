from satisfaction import *
from stats import *
from mariage_stable import *

def print_classement(x_ranks, y_satif, y_name : str):
    above, equal, below, classement = classementSatisfaction(x_ranks, y_satif, 1)
    print(f"========== Statistiques {y_name} ==========")
    print("")
    for key, value in classement.items():
        print(f"La moyenne des classements de {key} est de {value}")
    print("")
    print(f"Affectations supérieures au rang : {above}")
    print(f"Affectations égales au rang : {equal}")
    print(f"Affectations inférieures au rang : {below}")

def print_dict(dictionnary: dict):
    for i in dictionnary.keys():
        print(f"{i} : {dictionnary[i]}")
def print_dict_str_list(dictionnary: dict):
    #TODO ajouter des >
    for i in dictionnary.keys():
        print(f"{i} : ",end="")
        c = 0
        if len(dictionnary[i]) != 0:
            for e in dictionnary[i]:
                if (c < len(dictionnary) - 1):
                    print(f'{e} ', end="> ")
                else:   
                    print(f'{e} ', end="")
                c += 1
        print("\n",end="")

if __name__ == "__main__":
    n : int = 3
    s = 46
    print("")
    alphabet = generateData(n,"etab")
    numbers = generateData(n, "cand")
    
    school_dict = generateDict(len(alphabet),alphabet)
    candidate_dict = generateDict(len(numbers),numbers)
    
    school_dict = addRandomValueFromList(school_dict, numbers, s)
    candidate_dict = addRandomValueFromList(candidate_dict, alphabet, s*2)
    
    # school_dict = {
    #     "a":[3,1,5,4,2],
    #     "b":[2,1,5,4,3],
    #     "c":[5,2,3,4,1],
    #     "d":[2,1,5,4,3],
    #     "e":[3,2,5,4,1]
    # }
    
    # candidate_dict = {
    #     1 : ["b","a","c","e","d"],
    #     2 : ["a","c","b","e","d"],
    #     3 : ["c","a","e","b","d"],
    #     4 : ["c","b","e","d","a"],
    #     5 : ["a","b","c","d","e"]
    # }    
    school_ranks, candidate_ranks = calculate_rankings(school_dict,candidate_dict)
    
    
    
    print("========== PREFERENCES ==========")
    print("")
    print_dict_str_list(candidate_ranks)
    print("")
    print_dict_str_list(school_ranks)
    print("")
    print("========== MARIAGE STABLE ==========")
    print("")
    result = mariageStable(school_dict, candidate_dict, school_ranks)
    print_dict(result)
    satif_by_school = {}
    satif_by_candidate = {}
    for (key, value) in result.items():
        satif_by_school[key] = school_ranks[key][value]
        satif_by_candidate[value] = candidate_ranks[value][key]
    list_satif_x = list(satif_by_school.values())
    list_satif_y = list(satif_by_candidate.values())
    list_satif_x = sorted(list_satif_x)
    list_satif_y = sorted(list_satif_y)
    print("")
    print("========== MOYENNE ==========")
    print("")
    moy_x = moyenne(satif_by_school)
    moy_y = moyenne(satif_by_candidate)
    print(f"Moyenne des satisfactions des candidats : {round(moy_y,2)}")
    print(f"Moyenne des satisfactions des écoles : {round(moy_x,2)}")
    print("")
    print("========== EQUITE ==========")
    print("")
    print(f"Equité entre les écoles et les candidats : {equite(satif_by_candidate, satif_by_school)}")
    print("")
    print("")
    print("========== CLASSEMENT ==========")
    print("")
    print_classement(school_ranks, satif_by_candidate, "Candidats")
    print("")
    print_classement(candidate_ranks, satif_by_school, "Ecole")
    print("")
    print("========== ECHELLE ==========")
    print("")
    echelle(result, n, school_ranks, candidate_ranks)
    print("")
    print("========== AUTRES STATISTIQUES ==========")
    print("")
    med_x = mediane(list_satif_x)
    med_y = mediane(list_satif_y)
    print("========== Mediane ==========")
    print("")
    print("Médiane des affectations :")
    print(f"Candidats : {med_y}e choix")
    print(f"Ecoles : {med_x}e choix")
    print("")
    print("========== Ecart-Type ==========")
    print("")
    print("Ecart-type des satisfactions :")
    print(f"Candidats : {ecart_type(list_satif_y)}")
    print(f"Ecole : {ecart_type(list_satif_x)}")
    print("")
    print("========== Cardinalité Ecole ========")
    print("")
    cardinalite = {}
    for i in range(n):
        cpt = 0
        for e in list_satif_x:
            if e == i:
                cpt += 1
        if cpt != 0:
            cardinalite[i+1] = cpt
    for k,v in cardinalite.items():
        print(f"{k} : {v}")
    print("")
    print("========== Cardinalité Etudiant ========")
    print("")
    cardinalite = {}
    for i in range(n):
        cpt = 0
        for e in list_satif_y:
            if e == i:
                cpt += 1
        if cpt != 0:
            cardinalite[i+1] = cpt
    for k,v in cardinalite.items():
        print(f"{k} : {v}")
    
    
    
    #TODO revoir le min max pour voir comment l'utiliser et pourquoi
    # print("========== Max - Min ==========")
    # print("")
    # print(f"Affectation max ecole: {max(list_satif_x)}")
    # print(f"Affectation min ecole: {min(list_satif_x)}")
    # print("")
    # print(f"Affectation max candidats: {max(list_satif_y)}")
    # print(f"Affectation min candidats: {min(list_satif_y)}")