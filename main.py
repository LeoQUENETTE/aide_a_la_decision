from random import sample, seed

def mariageStable(pref_A : dict[str,list[str]], pref_B : dict[str,list[str]])->dict[str,str]:  
    found_school = {a : False for a in pref_B.keys()}
    result = {a: None for a in pref_A.keys()}
    school_ranks = {
        school: {candidate: rank for rank, candidate in enumerate(candidates)}
        for school, candidates in pref_A.items()
    }
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

def naiveSatisaction(result : dict[str,str],pref_A : dict[str,list[str]], pref_B : dict[str,list[str]], n : int)->None:
    school_ranks = {
        school: {candidate: rank for rank, candidate in enumerate(candidates)}
        for school, candidates in pref_A.items()
    }
    candidate_ranks = {
        candidate: {school: rank for rank, school in enumerate(schools)}
        for candidate, schools in pref_B.items()
    }
    s_satisfactions : dict[str,float]= {}
    c_satisfactions : dict[str,float]= {}
    s_satif_total = 0
    c_satif_total = 0
    for s, c in result.items():
        s_satisfaction = (n - school_ranks[s][c]) / n
        c_satisfaction = (n - candidate_ranks[c][s]) / n
        s_satisfactions[s] = s_satisfaction
        c_satisfactions[c] = c_satisfaction
        
        s_satif_total += s_satisfaction
        c_satif_total += c_satisfaction
    for key, value in sorted(s_satisfactions.items(), key=lambda item: item[1], reverse=True):
        print(f"Satisfaction de {key} : {"{:.2f}".format(value)}")
    print("")
    for key, value in sorted(c_satisfactions.items(), key=lambda item: item[1], reverse=True):
        print(f"Satisfaction de {key} : {"{:.2f}".format(value)}")
    print("")
    print(f"Moyenne des satisfactions : \nEcoles : {"{:.2f}".format((s_satif_total/n)*100)}%\nEtudiants : {"{:.2f}".format((c_satif_total/n)*100)}%")
    pass

def addRandomValueFromList(target : dict[str,list[str]], src : list[str], s : int = 42) -> dict[str,list[str]]:
    seed(s)
    for i in target.keys():
        target[i] = sample(src, len(src))
    return target
def generateAlphabet(n: int) -> list[str]:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = []
    
    length = 1
    while len(result) < n:
        from itertools import product
        combinations = product(alphabet, repeat=length)
        
        for combo in combinations:
            if len(result) >= n:
                break
            result.append(''.join(combo))
        
        length += 1
    
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
    n : int = 30
    s = 43
    alphabet = generateAlphabet(n)
    numbers = generateNumbers(n)
    
    alphabet_dict = generateDict(len(alphabet),alphabet)
    numbers_dict = generateDict(len(numbers),numbers)
    
    
    
    alphabet_dict = addRandomValueFromList(alphabet_dict, numbers, s)
    numbers_dict = addRandomValueFromList(numbers_dict, alphabet, s)
    
    print_dict_str_list(numbers_dict)
    print("")
    print_dict_str_list(alphabet_dict)
    
    print("")
    
    result = mariageStable(alphabet_dict, numbers_dict)
    print_dict(result)
    
    print("")
    naiveSatisaction(result,alphabet_dict,numbers_dict, n)