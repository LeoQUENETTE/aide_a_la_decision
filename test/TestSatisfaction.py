import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
from mariage_stable import calculate_rankings
from satisfaction import *

def balanced_distrib():
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
    result = {
        "a":"0",
        "b":"1",
        "c":"2"
    }
    school_ranks, candidate_ranks = calculate_rankings(school_dict,candidate_dict)
    satif_by_x = {}
    satif_by_y = {}
    for (key, value) in result.items():
        satif_by_x[key] = school_ranks[str(key)][str(value)]
        satif_by_y[value] = candidate_ranks[str(value)][str(key)]
    return satif_by_x, satif_by_y
def unbalanced_distrib():
    x_dict = {
            "a":["1","0","2"],
            "b":["2","1","0"],
            "c":["0","2","1"],
        }
    y_dict = {
        "0":["b","a","c"],
        "1":["c","b","a"],
        "2":["a","c","b"],
    }
    result = {
        "a":"1",
        "b":"2",
        "c":"0"
    }
    x_ranks, y_ranks = calculate_rankings(x_dict,y_dict)
    satif_by_x = {}
    satif_by_y = {}
    for (key, value) in result.items():
        satif_by_x[key] = x_ranks[str(key)][str(value)]
        satif_by_y[value] = y_ranks[str(value)][str(key)]
    return satif_by_x, satif_by_y


class TestSatisfaction(unittest.TestCase):
    def test_bien_etre_to_zero_one(self):
        satif_by_school, satif_by_candidate = unbalanced_distrib()
        self.assertEqual(moyenne(satif_by_candidate),0,"La valeur devrait être à zéro")
        self.assertEqual(moyenne(satif_by_school),1,"La valeur devrait être à un")
    def test_bien_etre_to_half_one(self):
        satif_by_school, satif_by_candidate = balanced_distrib()
        self.assertEqual(moyenne(satif_by_school),0.5, "La valeur devrait être à 0.5")
        self.assertEqual(moyenne(satif_by_candidate),0.5, "La valeur devrait être à 0.5")
    def test_equite_zero(self):
        x_satif, y_satif = unbalanced_distrib()
        self.assertEqual(equite(x_satif,y_satif), 0, "L'equite devrait être à zéro")
    def test_equite_un(self):
        x_satif, y_satif = balanced_distrib()
        self.assertEqual(equite(x_satif,y_satif), 1, "L'equite devrait être à un")
if __name__ == "__main__":
    unittest.main()