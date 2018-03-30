#open
#filter tirar linhas em branco - filter
#map
#map remove new lines
#lower
#map remove punctuation


from functools import partial
from string import punctuation
from re import sub
from collections import Counter
#from multprocessing.dummy import Pool

def pipe(*funcs):
    def inner(arg):
        result = arg
        for func in funcs:
            result = func(result)
        return result
    return inner    

remove_blank_lines = partial(filter,lambda x: x != '\n')
remove_new_lines = partial(map, lambda x: str.strip(x, '\n'))
lower = partial(map, str.lower)
remove_punctuation  = partial(map, lambda x: sub(r'[.\,?!\-\();]','',x))
join = partial(str.join,' ☾ ')
split = partial(str.split, sep = ' ')
parse = pipe(open) 

parse = pipe (open, remove_blank_lines, lower, remove_punctuation,join, split)
count_parse = pipe(parse, Counter)

xpto = count_parse('vaimalandra.txt')



print(' '.join(xpto))





