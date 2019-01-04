import builtins
import itertools
import random
import distance

bool_like_names = [''.join(i) for i in itertools.chain(itertools.product("truefals", repeat=4),
                                                       itertools.product("truefals", repeat=5))]

threshold = 5
bool_truthiness = {}
for name in bool_like_names:
    distance_sum = distance.levenshtein(name, 'true') + distance.levenshtein(name, 'false')
    if distance_sum < threshold and name not in ['true', 'false']:
        bool_truthiness[name] = distance.levenshtein(name, 'false') / (threshold - 1)

for name in bool_truthiness:
    setattr(builtins, name.title(), random.random() < bool_truthiness[name])
