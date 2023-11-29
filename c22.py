#Python program to calculate the maximum aggregate from the list of tuples (pairs).
from collections import Counter

def max_aggregate(input_list):
   aggregate_counter = Counter()
   for pair in input_list:
        aggregate_counter[pair] += sum(pair)
   max_tuple = max(aggregate_counter, key=aggregate_counter.get)
   print(f'Tuple with maximum aggregate: {max_tuple}, Aggregate value: {aggregate_counter[max_tuple]}')


input_list = [(1, 2), (3, 4), (5, 6), (1, 2), (3, 4)]
max_aggregate(input_list)
