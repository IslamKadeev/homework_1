from itertools import combinations

def bananas(s) -> set:
    result = set()
    
    for combination in combinations(range(len(s)), len(s)-6):
        word = list(s)
        for i in combination:
            word[i] = '-'
        word = ''.join(word)
        if word.replace('-', '') == 'banana':
            result.add(word)

    return result

assert bananas("banann") == set()
assert bananas("banana") == {"banana"}
assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
                     "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
                     "-ban--ana", "b-anana--"}
assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}
