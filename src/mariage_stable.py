from random import sample, seed
def mariageStable(pref_A: dict[str,list[str]], pref_B: dict[str,list[str]], school_ranks: dict[str,dict[str,int]]) -> dict[str,str]:
    # Initialisation : tous les candidats sont libres et aucune école n'est attribuée
    free_candidates = list(pref_B.keys())
    result = {a: None for a in pref_A.keys()}
    
    # Liste des propositions faites par chaque candidat
    proposals_made = {candidate: 0 for candidate in pref_B.keys()}
    
    while free_candidates:
        candidate = free_candidates[0]
        if proposals_made[candidate] >= len(pref_B[candidate]):
            free_candidates.pop(0)
            continue
        school = pref_B[candidate][proposals_made[candidate]]
        proposals_made[candidate] += 1
        
        current_match = result[school]
        if current_match is None:
            result[school] = candidate
            free_candidates.pop(0)
        else:
            # Si l'école préfère le nouveau candidat
            if school_ranks[school][candidate] < school_ranks[school][current_match]:
                result[school] = candidate
                free_candidates.pop(0)
                free_candidates.append(current_match)
    
    return result
def generateData(n: int, prec : str) -> list[str]:
    result : list[str] = []
    
    while len(result) < n:
        result.append(prec+str(len(result)))
    return result
def addRandomValueFromList(target : dict[str,list[str]], src : list[str], s : int = 42) -> dict[str,list[str]]:
    seed(s)
    for i in target.keys():
        target[i] = sample(src, len(src))
    return target

def generateNumbers(n : int)->list[int]:
    new_list : list[int] = []
    for i in range(n):
        new_list.append(i)
    return new_list
def generateDict(n : int, keys : list[str]):
    new_dict : dict[str,list[str]] = {}
    for i in range(n):
        new_dict[keys[i]] = []
    return new_dict
def calculate_rankings(school_dict : dict[str,str], candidate_dict : dict[str,str]):
    school_ranks = {
        school: {candidate: rank for rank, candidate in enumerate(candidates)}
        for school, candidates in school_dict.items()
    }
    candidate_ranks = {
        candidate: {school: rank for rank, school in enumerate(schools)}
        for candidate, schools in candidate_dict.items()
    }
    return school_ranks, candidate_ranks