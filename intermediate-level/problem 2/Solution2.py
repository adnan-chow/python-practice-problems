from collections import defaultdict

def group_anagrams(words):
    groups = defaultdict(list)
    for w in words:
        groups[''.join(sorted(w))].append(w)    # canonical key
    return list(groups.values())

print(group_anagrams(["bat","tab","cat","act"]))
# Output: [['bat', 'tab'], ['cat', 'act']]