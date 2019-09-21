graph = {
    'a': [('c', 22), ('d', 32)],
    'b': [('d', 28), ('e', 36), ('f', 27)],
    'c': [('d', 31), ('g', 47)],
    'd': [('g', 30)],
    'e': [('g', 26)],
    'f': [],
    'g': [],
    'i': [('a', 35), ('b', 45)],
}
visited = {
    'i': False,
    'a': False,
    'b': False,
    'c': False,
    'd': False,
    'e': False,
    'f': False,
    'g': False
}

heuristic = {
    'i': 80,
    'a': 55,
    'b': 42,
    'c': 34,
    'd': 25,
    'e': 20,
    'f': 17,
    'g': 0
}

