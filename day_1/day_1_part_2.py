def main():
    left, right = read_input()
    similarity_score(left, right)


def similarity_score(left, right):
    num_dict = {}
    
    for left_num in left:
        count = 0
        for right_num in right:
            if left_num == right_num:
                count +=1
        num_dict[left_num] = count
    score = 0
    for key, value in num_dict.items():
        score = score + (key * value)
    print(score)
    return score



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