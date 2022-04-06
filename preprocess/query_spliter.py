import re
from itertools import permutations, combinations

class query_spliter:

    def __init__(self, query_path, train_file, test_file):
        self.query_path = query_path
        self.train_file = train_file
        self.test_file = test_file
        self.train_list = []
        self.test_list = []
        self.enum_queries_train = [[], [], [], []]
        self.enum_queries_test = [[], [], [], []]

    def query_split(self, pivot):
        # index = 0
        data_list = []
        f = open(self.query_path, 'r', encoding='utf-8')
        # train_output = open(self.train_file, 'w', encoding='utf-8')
        # test_output = open(self.test_file, 'w', encoding='utf-8')
        for line in f:
            data_list.append(line)
            # train_output.write(line) if index >= pivot else test_output.write(line)
            # index += 1

        f.close()
        self.train_list = data_list[:-pivot]
        self.test_list = data_list[-pivot:]
        # train_output.close()
        # test_output.close()

    def save_reduced_query(self, output_dir):
        self.enumerate_grams(self.train_list, self.enum_queries_train)
        self.enumerate_grams(self.test_list, self.enum_queries_test)
        train_list = [open(output_dir + '/train/single_reduced.txt', 'w+', encoding='utf-8'),
                  open(output_dir + '/trian/duplets_reduced.txt', 'w+', encoding='utf-8'),
                  open(output_dir + '/train/triplets_reduced.txt', 'w+', encoding='utf-8'),
                  open(output_dir + '/train/quadruplets_reduced.txt', 'w+', encoding='utf-8')]

        test_list = [open(output_dir + '/test/single_reduced.txt', 'w+', encoding='utf-8'),
                  open(output_dir + '/test/duplets_reduced.txt', 'w+', encoding='utf-8'),
                  open(output_dir + '/test/triplets_reduced.txt', 'w+', encoding='utf-8'),
                  open(output_dir + '/test/quadruplets_reduced.txt', 'w+', encoding='utf-8')]

        for i in range(0, len(self.enum_queries_train)):
            self.save_single_reduced_query(train_list[i], self.enum_queries_train[i])

        for i in range(0, len(self.enum_queries_test)):
            self.save_single_reduced_query(test_list[i], self.enum_queries_test[i])

    def save_single_reduced_query(self, f, input_list):
        for i in input_list:
            f.write(i + '\n')
        f.close()

    def enumerate_grams(self, input_list, enum_list):
        index = 0
        for line in input_list:
            self.gram_combinations(line, enum_list)
            if index % 500000 == 0:
                print(index)
            index += 1
        for i in range(0, len(enum_list)):
            enum_list[i] = sorted(list(set(enum_list[i])))

    def gram_combinations(self, line, enum_list):
        grams = re.split(':| ', line.strip())[1:]
        if len(grams) > 12:
            return
        for i in range(0, min(len(grams), 4)):
            combs = combinations(grams, i + 1)
            for j in combs:
                enum_list[i].append(" ".join(j))

    def enumerate_grams_disk(self, output_dir):
        train_list = [open(output_dir + '/train/single.txt', 'w+', encoding='utf-8'),
                  open(output_dir + '/train/duplets.txt', 'w+', encoding='utf-8'),
                  open(output_dir + '/train/triplets.txt', 'w+', encoding='utf-8'),
                  open(output_dir + '/train/quadruplets.txt', 'w+', encoding='utf-8')]
        index = 0
        for line in self.train_list:
            self.gram_combinations_disk(line, train_list)
            if index % 500000 == 0:
                print(index)
            index += 1
        for f in train_list:
            f.close()

    def gram_combinations_disk(self, line, f_list):
        grams = re.split(':| ', line.strip())[1:]
        if len(grams) > 12:
            return
        for i in range(0, min(len(grams), 4)):
            combs = combinations(grams, i + 1)
            for j in combs:
                f_list[i].write(" ".join(j) + '\n')

