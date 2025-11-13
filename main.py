from analyze import *
def ln(x):
    EPS = 10**5
    NMAX = 100
    fact = (x-1.0) / (x+1)
    terme = fact
    somme = fact
    den = 1
    nbTermes = 1
    while abs(fact) >= EPS and nbTermes < NMAX:
        nbTermes += 1
        den += 2 
        fact *= fact ** 2
        terme = fact / den
        somme += terme
    return 2*somme

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
    alphabet = generateAlphabet(n)
    numbers = generateNumbers(n)
    
    school_dict = generateDict(len(alphabet),alphabet)
    candidate_dict = generateDict(len(numbers),numbers)
    
    school_dict = addRandomValueFromList(school_dict, numbers, s)
    candidate_dict = addRandomValueFromList(candidate_dict, alphabet, s)
    
    school_dict = {
        "a":["1","0","2"],
        "b":["0","1","2"],
        "c":["1","2","0"],
    }
    candidate_dict = {
        "0":["a","b","c"],
        "1":["b","a","c"],
        "2":["a","c","b"],
    }
    
    school_ranks = {
        school: {candidate: rank for rank, candidate in enumerate(candidates)}
        for school, candidates in school_dict.items()
    }
    candidate_ranks = {
        candidate: {school: rank for rank, school in enumerate(schools)}
        for candidate, schools in candidate_dict.items()
    }
    
    print_dict_str_list(candidate_ranks)
    print("")
    print_dict_str_list(school_ranks)
    
    print("")
    
    result = mariageStable(school_dict, candidate_dict, school_ranks)
    print_dict(result)
    
    # print("")
    # print("CLASSEMENT")
    # print("")
    # classementSatisfaction(result,n,school_ranks, candidate_ranks, 0)
    # print("")
    # print("NAIVE")
    # print("")
    # naiveSatisaction(result,n,school_ranks, candidate_ranks)
    # print("")
    print("PONDERE")
    print("")
    weightedSatisfaction(result,n,school_ranks, candidate_ranks)
    
    