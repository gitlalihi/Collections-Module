#Python program to merge more than one dictionary into a single expression.
from collections import ChainMap


dict1 = {'a': 1, 'b': 2}

dict2={'b': 3, 'c': 4}

dict3 = {'d': 5}


merged_dict = dict(ChainMap(dict1, dict2, dict3))


print("Merged Dictionary:", merged_dict)
