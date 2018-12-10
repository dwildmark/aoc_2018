
def parse_squares():
    squares = []
    with open("input.txt", "r") as file:
        for line in file:
            data = line.split("@")[1].replace(" ", "").replace("\n", "").split(":")
            start_point = [int(i) for i in data[0].split(",")]
            size = [int(i) for i in data[1].split("x")]
            squares.append([start_point, size])

    return squares


def place_square(fabric, square):
    for x in range(square[0][0], square[0][0] + square[1][0]):
        for y in range(square[0][1], square[0][1] + square[1][1]):
            fabric[x][y] += 1

    return fabric

def check_intact_square(fabric, square):
    for x in range(square[0][0], square[0][0] + square[1][0]):
        for y in range(square[0][1], square[0][1] + square[1][1]):
            if fabric[x][y] is not 1:
                return False

    return True

fabric = [[0] * 1000 for i in range(1000)]
for square in parse_squares():
    place_square(fabric, square)

for i, square in enumerate(parse_squares()):
    if check_intact_square(fabric, square):
        print "#", i + 1, square

count = 0
for row in fabric:
    for col in row:
        if col > 1:
            count += 1

print count
