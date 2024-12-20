import os
import re
def main():
    HOME = os.path.expanduser("~")
    WDIR = "advent_2024/day_3"
    INPUT = "input.txt"
    data = read_input_file(f"{HOME}/{WDIR}/{INPUT}")
    stuff = regex_search_str(data)
    int_list = cast_to_int(stuff)
    addition = multiply_then_add_int_list(int_list)
    print(addition)


def read_input_file(file):
    data = ""
    with open (file, "r", encoding="utf-8") as input_file:
        for line in input_file:
            data += line
    return data

def regex_search_str(data:str):
    return re.findall("mul\(\d{1,3},\d{1,3}\)",data)

def cast_to_int(match_list):
    int_list = []
    for item in match_list:
        front = ((item[4:])[:-1]).split(",")
        int_list.append([int(x) for x in front])
    return int_list

def multiply_then_add_int_list(int_list):
    addition = 0
    for mul in int_list:
        addition += (mul[0] * mul[1])
    return addition

if __name__ == "__main__":
    main()
