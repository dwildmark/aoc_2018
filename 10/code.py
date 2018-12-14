import copy
def parse_input_to_list():
    points_list = []
    with open("input.txt", "r") as file:
        for line in file:
            stripped = line.replace("position=", "").replace("velocity=", "")
            pos = stripped.split("<")[1].strip("<> ")
            vel = stripped.split("<")[2].strip("<> \n")
            posx = int(pos.split(", ")[0])
            posy = int(pos.split(", ")[1])
            velx = int(vel.split(", ")[0])
            vely = int(vel.split(", ")[1])
            points_list.append(dict(x = posx, y = posy, velx = velx, vely = vely))

    return points_list


def paint_canvas(points):
    xmin = min([min(points, key = lambda x: x["x"])["x"], 0])
    xmax = max([max(points, key = lambda x: x["x"])["x"], 0])
    ymin = min([min(points, key = lambda x: x["y"])["y"], 0])
    ymax = max([max(points, key = lambda x: x["y"])["y"], 0])

    canvas = [[" " for i in range(xmin - 1, xmax + 1)] for i in range(ymin - 1, ymax + 1)]
    for point in points:
        canvas[point["y"]][point["x"]] = "#"


    for row in canvas:
        print ''.join(row)

    print "---------------------------------------------"


def move_points(points):
    for point in points:
        point["x"] += point["velx"]
        point["y"] += point["vely"]

def get_area(points):
    xmin = min(points, key = lambda x: x["x"])["x"]
    xmax = max(points, key = lambda x: x["x"])["x"]
    ymin = min(points, key = lambda x: x["y"])["y"]
    ymax = max(points, key = lambda x: x["y"])["y"]
    area = abs(xmax - xmin) * abs(ymax - ymin)
    return area

def part_one_and_two():
    seconds = 0
    points = parse_input_to_list()
    last_points = copy.deepcopy(points)
    last_area = get_area(points)
    while True:
        move_points(points)
        if last_area < get_area(points):
            paint_canvas(last_points)
            print seconds
            exit()
        last_area = get_area(points)
        last_points = copy.deepcopy(points)
        seconds += 1

part_one()


