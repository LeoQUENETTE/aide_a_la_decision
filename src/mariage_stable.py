from random import sample, seed
def mariageStable(pref_A : dict[str,list[str]], pref_B : dict[str,list[str]], school_ranks : dict[str,dict[str,int]])->dict[str,str]:  
    found_school = {a : False for a in pref_B.keys()}
    result = {a: None for a in pref_A.keys()}
    for pref_id in range(len(pref_B)):
        for candidate in pref_B.keys():
            if found_school.get(candidate):
                continue
            wanted_school = pref_B[candidate][pref_id]
            current_scholar = result.get(wanted_school)
            if current_scholar == None or school_ranks[wanted_school][current_scholar] > school_ranks[wanted_school][candidate]:
                result[wanted_school] = candidate
                found_school[candidate] = True
                if (current_scholar != None):
                    found_school[current_scholar] = False
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