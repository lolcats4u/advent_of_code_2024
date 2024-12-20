import os
import re


def main():
    HOME = os.path.expanduser("~")
    WDIR = "advent_2024/day_3"
    INPUT = "input.txt"
    data = read_input_file(f"{HOME}/{WDIR}/{INPUT}")
    muls = Match("mul\(\d{1,3},\d{1,3}\)", data)
    muls.clean_mul()
    dos = Match("do\(\)", data)
    donts = Match("don't\(\)", data)
    ordered_list = merge_and_sort([muls,dos,donts])
    valid_muls = execute_on_off(ordered_list)
    print(multiply_then_add_int_list(valid_muls))


def read_input_file(file):
    data = ""
    with open(file, "r", encoding="utf-8") as input_file:
        for line in input_file:
            data += line
    return data

def merge_and_sort(regex_iteritems:list):
    whole_list = []
    for match_object in regex_iteritems:
        zipped_values = zip([int(x[0]) for x in match_object.indecies],match_object.matches)
        for pair in zipped_values:
            whole_list.append(pair)
    whole_list.sort()
    return whole_list

def execute_on_off(sorted_entries:list):
    values_to_multiply = []
    append_switch = True
    for entry in sorted_entries:
        if entry[1] == "don't()":
            append_switch = False
            continue
        if entry[1] == "do()":
            append_switch = True
            continue
        if append_switch:
            values_to_multiply.append(entry[1])

    return values_to_multiply

def multiply_then_add_int_list(int_list):
    addition = 0
    for mul in int_list:
        addition += (mul[0] * mul[1])
    return addition

class Match:
    def __init__(self, regex_filter, data):
        self.data = data
        self.regex_filter = regex_filter
        self.indecies = [x.span() for x in re.finditer(self.regex_filter, data)]
        self.matches = self._0_correction_slicer()

    def _0_correction_slicer(self):
        slices = [self.data[x[0]: x[1]] for x in self.indecies]
        if self.indecies[0][0] == 0:
            slices[0]= self.data[:self.indecies[0][1]]
        return slices
    
    def clean_mul(self):
        int_list = []
        for item in self.matches:
            front = ((item[4:])[:-1]).split(",")
            int_list.append([int(x) for x in front])
        self.matches = int_list

    


if __name__ == "__main__":
    main()
