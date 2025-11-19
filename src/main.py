from satisfaction import *
from stats import *
from mariage_stable import *

def print_classement(x_ranks, y_satif, y_name : str):
    above, equal, below, classement = classementSatisfaction(school_ranks, satif_by_candidate)
    print(f"========== Statistiques {y_name} ==========")
    print("")
    for key, value in classement.items():
        print(f"Le classement de {key} est de {value}")
    print("")
    print(f"Affectation supérieur au rang : {above}")
    print(f"Affectation égale au rang : {equal}")
    print(f"Affectation inférieur au rang : {below}")

def print_dict(dictionnary: dict):
    for i in dictionnary.keys():
        print(f"{i} : {dictionnary[i]}")
def print_dict_str_list(dictionnary: dict):
    for i in dictionnary.keys():
        print(f"{i} : ",end="")
        if len(dictionnary[i]) != 0:
            for e in dictionnary[i]:
                print(f'{e} ', end="")   
        print("\n",end="")

if __name__ == "__main__":
    n : int = 3
    s = 42
    alphabet = generateData(n,"etab")
    numbers = generateData(n, "etu")
    
    school_dict = generateDict(len(alphabet),alphabet)
    candidate_dict = generateDict(len(numbers),numbers)
    
    school_dict = addRandomValueFromList(school_dict, numbers, s)
    candidate_dict = addRandomValueFromList(candidate_dict, alphabet, s)
    
    school_ranks, candidate_ranks = calculate_rankings(school_dict,candidate_dict)
    
    print_dict_str_list(candidate_ranks)
    print("")
    print_dict_str_list(school_ranks)
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
    print("========== BIEN ETRE ==========")
    print("")
    print(f"Bien être des candidats : {bien_etre(satif_by_candidate)}")
    print(f"Bien être des écoles : {bien_etre(satif_by_school)}")
    print("")
    print("========== EQUITE ==========")
    print("")
    print(f"Equité entre les écoles et les candidats : {equite(satif_by_candidate, satif_by_school)}")
    print("")
    print("========== CLASSEMENT ==========")
    print("")
    print_classement(school_ranks, satif_by_school, "Candidats")
    print("")
    print_classement(candidate_ranks, satif_by_school, "Ecole")
    print("")
    print("========== ECHELLE ==========")
    print("")
    echelle(result, n, school_ranks, candidate_ranks)
    print("")
    print("========== AUTRE STATISTIQUES ==========")
    print("")
    med_x = mediane(list_satif_x)
    med_y = mediane(list_satif_y)
    print("========== Mediane ==========")
    print("")
    print("La position de l'affectation médiane :")
    print(f"Ecoles : {med_x}")
    print(f"Etudiants : {med_y}")
    print("")
    print("========== Moyenne ==========")
    print("")
    moy_x = moyenne_lineaire(list_satif_x)
    moy_y = moyenne_lineaire(list_satif_y)
    print("La position de l'affectation moyenne :")
    print(f"Ecoles : {med_x}")
    print(f"Etudiants : {med_y}")
    print("")
    print("========== Ecart Type ==========")
    print("")
    print(f"Ecart type ecole : {ecart_type(list_satif_x)}")
    print(f"Ecart type candidats : {ecart_type(list_satif_y)}")
    print("")
    #TODO revoir le min max pour voir comment l'utiliser et pourquoi
    # print("========== Max - Min ==========")
    # print("")
    # print(f"Affectation max ecole: {max(list_satif_x)}")
    # print(f"Affectation min ecole: {min(list_satif_x)}")
    # print("")
    # print(f"Affectation max candidats: {max(list_satif_y)}")
    # print(f"Affectation min candidats: {min(list_satif_y)}")