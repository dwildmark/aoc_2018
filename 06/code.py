from collections import defaultdict
import sys

def parse_input_to_list():
    output = []
    with open("input.txt", "r") as file:
        for i, line in enumerate(file):
            x, y = line.split(", ")
            output.append(dict(x = int(x), y = int(y)))

    return output

def manhattan_dist(point_a, point_b):
    return abs(point_a["x"] - point_b["x"]) + abs(point_a["y"] - point_b["y"])

def find_closest_point(point_list, coordinate):
    min = sys.maxsize
    min_point = dict()
    min_index = sys.maxsize
    min_occurence = 1
    for i, point in enumerate(point_list):
        distance = manhattan_dist(point, coordinate)
        if distance < min:
            min = distance
            min_index = i
            min_point = point
            min_occurence = 1
        elif distance == min:
            min_occurence += 1

    if min_occurence > 1:
        #print coordinate, "is equally close to", min_point
        return -1

    #print coordinate, "is closest to", min_point
    return min_index

def point_is_neighbor_with_infinity(point, xmax, ymax):
    if point["x"] >= xmax or point["x"] <= 0 or point["y"] >= ymax or point["y"] <= 0:
        return True

    return False

def part_one():
    points = parse_input_to_list()

    xmax = max(points, key=lambda x:x["x"])["x"] + 1

    ymax = max(points, key=lambda x:x["y"])["y"] + 1
    grid = [[-1 for y in range(ymax)] for x in range(xmax)]

    points_score = defaultdict(int)

    for x, row in enumerate(grid):
        for y, col in enumerate(row):
            index = find_closest_point(points, dict(x = x, y = y))
            if index == -1:
                continue
            elif points_score[index] != -1:
                if point_is_neighbor_with_infinity(dict(x = x, y = y), xmax, ymax):
                    points_score[index] = -1
                else:
                    points_score[index] += 1

    print "Part 1 solution:"
    print max(points_score.items(), key=lambda x:x[1])

def calc_total_dist(points_list, coordinate):
    total_distance = 0
    for point in points_list:
        total_distance += manhattan_dist(point, coordinate)

    return total_distance

def part_two():
    coords = parse_input_to_list()
    xmax = max(coords, key=lambda x:x["x"])["x"] + 1
    ymax = max(coords, key=lambda x:x["y"])["y"] + 1

    area = 0
    for x in range(xmax):
        for y in range(ymax):
            distance = calc_total_dist(coords, dict(x = x, y = y))
            if distance <= 10000:
                area += 1

    print "Part 2 solution:"
    print area

part_one()
part_two()


