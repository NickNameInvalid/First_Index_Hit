from preprocess.query_spliter import query_spliter
import re
import os
from itertools import permutations, combinations

qs = query_spliter('data/aol.clean', 'postings/train_queries_original.txt', 'postings/test_queries_original.txt')
qs.query_split(10000)
qs.enumerate_grams_disk('postings')
qs.generate_sort_command('e', 'PISA/First_Index_Hit/postings')