import re

class gram_intersection:

    def __init__(self, input_dir, output_dir):
        self.input_dir = input_dir
        self.output_dir = output_dir

    def get_intersection(self, f1, f2, output, length):
        gram_list1 = []
        gram_list2 = []

        for line1 in f1:
            grams = re.split(r"[ ]+", line1.strip(), maxsplit=1)
            if len(grams) != length:
                continue
            gram_list1.append()