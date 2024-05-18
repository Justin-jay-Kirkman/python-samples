#Given two strings, A and B, find all permutations of A within B
import itertools
#input A, B
test_cases = [
    ["dasd","sadasdasdfaasdasdfaasdfaasdads"], #output array []
    ["a", ""],
    ["a", "a"],
    ["", "sdsa"],
    ["dad","asdasdaasdsadad"]
]
# create permutations for A as an array of strings
# compair A array to substring B 1:A length - then increment 1 down the line <--don't need this, just compair string in
# ---- note optimization: also check if new character not in string A, then skip, increment by length A? or remove letter from string...
# if found ->  write the result to array
# are we going to add duplicates? if no, remove from results array
# break if A array is empty
#error check that A length < B length : If not don't start

class Permutations:
    def __init__(self, string):
        self.string = string

     # input string A, output dictionary
    # use permutations library, otherwise can be created by recursive function
    def get_permutations(self):
        return [''.join(p) for p in itertools.permutations(self.string)]


def permutations_string(a,b):
    result = []
    if len(a) > len(b):
        return result
    perm = Permutations(a)
    a_perm = perm.get_permutations()

    for perm in a_perm:
        if perm in b:
            result.append(perm)
    return result

for test_case in test_cases:
    print(permutations_string(test_case[0],test_case[1]))

