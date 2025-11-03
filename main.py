from random import sample, seed
from math import floor, ceil

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
        classement[c] = int((1 - step * dist) * 100)
        
        rank = school_ranks[s][c]
        dist =  (rank+1) - classement[s]
        classement[s] = int((1 - step * dist) * 100)
    for i,v in classement.items():
        print(f"La satisfaction de {i} est de {v}%")
    return classement
def naiveSatisaction(
    result : dict[str,str],
    n : int,
    school_ranks : dict[str,dict[str,int]],
    candidate_ranks : dict[str,dict[str,int]])->None:
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
def weightedSatisfaction(result : dict[str,str],
    n : int,
    school_ranks : dict[str,dict[str,int]],
    candidate_ranks : dict[str,dict[str,int]])->None:
    s_satisfactions : dict[str,float]= {}
    c_satisfactions : dict[str,float]= {}
    s_satif_total = 1
    c_satif_total = 1
    step : float = 1 / n
    for s, c in result.items():
        if school_ranks[s][c] < n//2:
            s_satisfaction = 1 + step * (n//2 - school_ranks[s][c])
        elif school_ranks[s][c] > n//2:
            s_satisfaction = 1 - step * ((school_ranks[s][c]+ 1) - n//2)
        else:
            s_satisfaction = 1
        s_satisfactions[s] = s_satisfaction
        if candidate_ranks[c][s] < n//2:
            c_satisfaction = 1 + step * (n//2 - candidate_ranks[c][s])
        elif candidate_ranks[c][s] > n//2:
            c_satisfaction = 1 - step * ((candidate_ranks[c][s] + 1 )- n//2)
        else :
            candidate_ranks[c][s] = 1
        c_satisfactions[c] = c_satisfaction
        s_satif_total *= s_satisfaction
        c_satif_total *= c_satisfaction
    for key, value in sorted(s_satisfactions.items(), key=lambda item: item[1], reverse=True):
        print(f"Satisfaction de {key} : {"{:.2f}".format(value)}")
    print("")
    for key, value in sorted(c_satisfactions.items(), key=lambda item: item[1], reverse=True):
        print(f"Satisfaction de {key} : {"{:.2f}".format(value)}")
    print("")
    print(f"Moyenne des satisfactions : \nEcoles : {"{:.2f}".format(s_satif_total)}\nEtudiants : {"{:.2f}".format(c_satif_total)}")
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
    n : int = 10
    s = 42
    alphabet = generateAlphabet(n)
    numbers = generateNumbers(n)
    
    school_dict = generateDict(len(alphabet),alphabet)
    candidate_dict = generateDict(len(numbers),numbers)
    
    school_dict = addRandomValueFromList(school_dict, numbers, s)
    candidate_dict = addRandomValueFromList(candidate_dict, alphabet, s)
    
    school_dict = {
        "a":["0","1","2"],
        "b":["0","1","2"],
        "c":["1","2","0"],
    }
    candidate_dict = {
        "0":["a","b","c"],
        "1":["a","b","c"],
        "2":["b","c","a"],
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
    
    print("")
    classementSatisfaction(result,n,school_ranks, candidate_ranks, 1)
    print("")
    naiveSatisaction(result,n,school_ranks, candidate_ranks)
    print("")
    weightedSatisfaction(result,n,school_ranks, candidate_ranks)
    
    