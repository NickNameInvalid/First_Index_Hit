import re
from itertools import permutations, combinations

class query_spliter:

    def __init__(self, query_path, train_file, test_file):
        self.query_path = query_path
        self.train_file = train_file
        self.test_file = test_file
        self.train_list = []
        self.test_list = []
        self.validation_list = []
        self.enum_queries_train = [[], [], [], []]
        self.enum_queries_test = [[], [], [], []]

    def query_split(self, pivot1, pivot2):
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
        self.train_list = data_list[:-pivot1]
        self.validation_list = data_list[-pivot1 - pivot2:-pivot2]
        self.test_list = data_list[-pivot2:]
        # train_output.close()
        # test_output.close()

    def save_single_reduced_query(self, f, input_list):
        for i in input_list:
            f.write(i + '\n')
        f.close()

    def enumerate_grams_disk(self, output_dir):
        train_list = [open(output_dir + '/train/single.txt', 'w+', encoding='utf-8'),
                  open(output_dir + '/train/duplets.txt', 'w+', encoding='utf-8'),
                  open(output_dir + '/train/triplets.txt', 'w+', encoding='utf-8'),
                  open(output_dir + '/train/quadruplets.txt', 'w+', encoding='utf-8')]

        validation_list = [open(output_dir + '/validation/single.txt', 'w+', encoding='utf-8'),
                  open(output_dir + '/validation/duplets.txt', 'w+', encoding='utf-8'),
                  open(output_dir + '/validation/triplets.txt', 'w+', encoding='utf-8'),
                  open(output_dir + '/validation/quadruplets.txt', 'w+', encoding='utf-8')]

        test_list = [open(output_dir + '/test/single.txt', 'w+', encoding='utf-8'),
                  open(output_dir + '/test/duplets.txt', 'w+', encoding='utf-8'),
                  open(output_dir + '/test/triplets.txt', 'w+', encoding='utf-8'),
                  open(output_dir + '/test/quadruplets.txt', 'w+', encoding='utf-8')]

        # index = 0
        for line in self.train_list:
            self.gram_combinations_disk(line, train_list)
        for line in self.validation_list:
            self.gram_combinations_disk(line, validation_list)
        for line in self.test_list:
            self.gram_combinations_disk(line, test_list)

        for f in train_list:
            f.close()
        for f in validation_list:
            f.close()
        for f in test_list:
            f.close()

    def gram_combinations_disk(self, line, f_list):
        def filter_empty(s):
            return s and s.strip()
        grams = list(filter(filter_empty, re.split(r':|[ ]+|/|\.', line.strip())[1:]))
        if len(grams) > 12:
            return
        for i in range(0, min(len(grams), 4)):
            combs = combinations(grams, i + 1)
            for j in combs:
                f_list[i].write(" ".join(j) + '\n')


    def generate_sort_command(self, disk, abs_dir):
        print("cd /mnt/" + disk + "/" + abs_dir)
        print("sort train/single.txt |uniq -c > train/single_red.txt")
        print("sort train/duplets.txt |uniq -c > train/duplets_red.txt")
        print("sort train/triplets.txt |uniq -c > train/triplets_red.txt")
        print("sort train/quadruplets.txt |uniq -c > train/quadruplets_red.txt")

        print("sort validation/single.txt |uniq -c > validation/single_red.txt")
        print("sort validation/duplets.txt |uniq -c > validation/duplets_red.txt")
        print("sort validation/triplets.txt |uniq -c > validation/triplets_red.txt")
        print("sort validation/quadruplets.txt |uniq -c > validation/quadruplets_red.txt")

        print("sort test/single.txt |uniq -c > test/single_red.txt")
        print("sort test/duplets.txt |uniq -c > test/duplets_red.txt")
        print("sort test/triplets.txt |uniq -c > test/triplets_red.txt")
        print("sort test/quadruplets.txt |uniq -c > test/quadruplets_red.txt")