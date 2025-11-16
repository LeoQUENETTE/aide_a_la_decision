from satisfaction import *
from stats import *
from mariage_stable import *

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
        "b":["2","1","0"],
        "c":["0","2","1"],
    }
    candidate_dict = {
        "0":["b","a","c"],
        "1":["c","b","a"],
        "2":["a","c","b"],
    }
    
    school_ranks, candidate_ranks = calculate_rankings(school_dict,candidate_dict)
    
    print_dict_str_list(candidate_ranks)
    print("")
    print_dict_str_list(school_ranks)
    print("")
    
    result = mariageStable(school_dict, candidate_dict, school_ranks)
    # result = {
    #     "a":"0",
    #     "b":"1",
    #     "c":"2"
    # }
    print_dict(result)
    satif_by_school = {}
    satif_by_candidate = {}
    for (key, value) in result.items():
        satif_by_school[key] = school_ranks[str(key)][str(value)]
        satif_by_candidate[value] = candidate_ranks[str(value)][str(key)]
       
    print("")
    
    print(bien_etre(satif_by_candidate))
    print(bien_etre(satif_by_school))
    print(equite(satif_by_candidate, satif_by_school))
    # print("")
    # print("CLASSEMENT")
    # print("")
    # classementSatisfaction(result,n,school_ranks, candidate_ranks, 0)
    # print("")
    # print("ECHELLE")
    # print("")
    # naiveSatisaction(result,n,school_ranks, candidate_ranks)
    # # print("")
    # print("PONDERE")
    # print("")
    # echelle(result,n,school_ranks, candidate_ranks)
    
    