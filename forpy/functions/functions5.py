from itertools import permutations 
def p_permutations(s):
    perms = permutations(s)
    for p in perms:
        print("".join(p))

s=input()
p_permutations(s)
