def main():
    reports = read_input_file()
    safe_reports = 0
    for report in reports:
        if (validate_report(report)) == "Safe":
            safe_reports += 1
    print(safe_reports)
    return safe_reports

def read_input_file():
    reports = []
    with open ("input.txt", "r", encoding="utf-8") as input_file:
        for line in input_file:
            reports.append(line.split())
    return reports

def check_one_way(report):
    neg = False
    distances = []
    report_length = len(report)
    last_index = report_length - 1
    unsafe = None
    for index, num in enumerate(report):
        if index == last_index:
            break
        distance = int(num) - int(report[index + 1])
        distances.append(distance)
        if index == 0:
            if distance < 1:
                neg = True
        if neg:
            if distance > 0:
                unsafe = "Unsafe"
        else:
            if distance < 0:
                unsafe = "Unsafe"
    if unsafe:
        return unsafe, distances
    else:
        return "Safe", distances

def check_adjacent_distances(distances):
    for num in distances:
        abs_int = abs(int(num))
        if abs_int < 1:
            return "Unsafe", distances
        if abs_int > 3:
            return "Unsafe", distances
    return "Safe", distances
        
def validate_report(report):
    one_way = check_one_way(report)
    adjacent = check_adjacent_distances(one_way[1])

    if one_way[0] == "Unsafe" or adjacent[0] == "Unsafe":
        return "Unsafe"
    
    return "Safe"



if __name__ == "__main__":
    main()
