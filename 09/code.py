def parse_input_to_game_rules():
    with open("input.txt", "r") as file:
        inpt = file.read()
        num_players = int(inpt.split(";")[0].split(" ")[0])
        num_balls = int(inpt.split(";")[1].split(" ")[5])

    return (num_players, num_balls)


def play_game(num_players, num_balls):
    curr_player = 0
    curr_marble_index = 0
    players = [0] * num_players

    circle = []
    circle.append(0)

    percentage = num_balls / 100

    completion_percent = 0
    for ball in range(1, num_balls + 1):
        current_ball = ball
        if current_ball % percentage == 0:
            completion_percent += 1
            print completion_percent, "%"

        if current_ball % 23 == 0:
            players[curr_player] += current_ball
            curr_marble_index = ((curr_marble_index - 7) % len(circle))
            players[curr_player] += circle.pop(curr_marble_index)
        else:
            curr_marble_index = ((curr_marble_index + 1) % len(circle)) + 1
            circle.insert(curr_marble_index, current_ball)

        curr_player = (ball - 1) % num_players

    print max(players)

def part_one():
    num_players, num_balls = parse_input_to_game_rules()
    play_game(num_players, num_balls)

def part_two():
    print "Starting calculations"
    num_players, num_balls = parse_input_to_game_rules()
    play_game(num_players, num_balls * 100)


#part_one()
part_two()
