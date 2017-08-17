""" Invertex Index Implementation.
"""
from collections import defaultdict

def create_index (data):
    index = defaultdict(list)
    for i, tokens in enumerate(data):
    	print('i', i)
        for token in tokens:
            index[token].append(i)
    return index

index = create_index([['a', 'b'], ['a', 'c']])

print(index.keys())
print(index['a'])
print(index['b'])
print(index['c'])