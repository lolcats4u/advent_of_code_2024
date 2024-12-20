import os
def main():
    HOME = os.path.expanduser("~")
    WDIR = "advent_2024/day_2"
    INPUT = "input.txt"
    data = read_input_file(f"{HOME}/{WDIR}/{INPUT}")
    reports = objectify(data)
    validate_report(reports)
    enumerate_optional_configurations(reports)
    problem_dampener(reports)
    count_not_unsafe(reports)

def read_input_file(file):
    reports = []
    with open (file, "r", encoding="utf-8") as input_file:
        for line in input_file:
            reports.append([int(x) for x in line.split()])
    return reports

def check_one_way(reports):

    for report in reports:
        for distance in report.distances:
            if report.neg_distance and distance > 0:
                report.safety = False
            if not report.neg_distance and distance < 0:
                report.safety = False

def calculate_distances(reports):
    for report in reports:
        distances = []
        last_index = len(report.data) - 1
        for index, num in enumerate(report.data):
            if index == last_index:
                break
            distance = num - report.data[index + 1]
            distances.append(distance)
            if index == 0 and distance < 1:
                report.neg_distance = True
        report.distances = distances

def check_adjacent_distances(reports):
    for report in reports:
        for num in report.distances:
            abs_int = abs(num)
            if abs_int < 1 or abs_int > 3:
                report.safety = False
        
def validate_report(reports):
    calculate_distances(reports)
    check_one_way(reports)
    check_adjacent_distances(reports)

def count_not_unsafe(reports):
    count = 0
    for report in reports:
        if report.safety is not False:
            count += 1
    print(count)

def objectify(data:list):
    return [Report(x) for x in data]

def enumerate_optional_configurations(reports):
    for report in reports:
        new_configurations = []
        last_index = len(report.data)-1
        for index, _ in enumerate(report.data):
            if index == 0: 
                str_slice = report.data[1:]
            elif index > 0 and index < last_index:
                str_slice = report.data[:index] + report.data[(index+1):]
            else:
                str_slice = report.data[:-1]
            new_configurations.append(str_slice)
        report.additional_configs = new_configurations
        
def problem_dampener(reports):
    for report in reports:
        additional_objects = objectify(report.additional_configs)
        validate_report(additional_objects)
        for additional_report in additional_objects:
            if additional_report.safety is not False:
                report.safety = True
                break

class Report:
    def __init__(self, data):
        self.data = data
        self.safety = None
        self.distances = None
        self.neg_distance = None
        self.index_remove_for_safe = None
        self.additional_configs = None
    
if __name__ == "__main__":
    main()
