from preprocess.query_spliter import query_spliter
import re
import os
from itertools import permutations, combinations

qs = query_spliter('data/aol.clean', 'postings/train_queries_original.txt', 'postings/test_queries_original.txt')
qs.query_split(10000, 10000)
qs.enumerate_grams_disk('postings')
qs.generate_sort_command('e', 'PISA/First_Index_Hit/postings')

# def filter_empty(s):
#     return s and s.strip()
#
# grams = list(filter(filter_empty, re.split(r":|[ ]+", "3698603: Assuming the value of terrier.home from the corresponding system property.".strip())))
# print(grams)