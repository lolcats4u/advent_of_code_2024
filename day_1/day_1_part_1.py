def main():
    left, right = read_input()
    distance = sort_and_add(left, right)


def sort_and_add(left, right):
    left.sort()
    right.sort()
    distance = 0
    for pair in zip(left, right):
        distance = distance + abs(pair[0] - pair[1])
    print(distance)
    return distance

def read_input():
    left = []
    right = []
    with open("input.txt", "r", encoding="utf-8") as input_file:
        for line in input_file:
            split = line.split()
            left.append(int(split[0]))
            right.append(int(split[1]))
    return left, right



if __name__ == "__main__":
    main()