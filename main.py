from random import sample, seed

def mariageStable(pref_A : dict[str:list[str]], pref_B : dict[str:list[str]])->dict[str:str]:  
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

def addRandomValueFromList(target : dict[str:list[str]], src : list[str], s : int = 42) -> dict[str:list[str]]:
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
    new_dict : dict[str:list(str)] = {}
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
    n : int = 20
    seed = 42
    alphabet = generateAlphabet(n)
    numbers = generateNumbers(n)
    
    alphabet_dict = generateDict(len(alphabet),alphabet)
    numbers_dict = generateDict(len(numbers),numbers)
    
    alphabet_dict = addRandomValueFromList(alphabet_dict, numbers, seed)
    numbers_dict = addRandomValueFromList(numbers_dict, alphabet, seed)
    
    print_dict_str_list(numbers_dict)
    print("")
    print_dict_str_list(alphabet_dict)
    
    print("")
    
    result = mariageStable(alphabet_dict, numbers_dict)
    print_dict(result)