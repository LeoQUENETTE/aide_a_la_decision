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
    
    print("")
    # print("")
    # print("CLASSEMENT")
    # print("")
    # classementSatisfaction(result,n,school_ranks, candidate_ranks, 0)
    # print("")
    # print("ECHELLE")
    # print("")
    # naiveSatisaction(result,n,school_ranks, candidate_ranks)
    # print("")
    print("PONDERE")
    print("")
    echelle(result,n,school_ranks, candidate_ranks)
    
    