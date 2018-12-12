from __future__ import print_function

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class CircularDoublyLinkedList:
    def __init__(self):
        self.first = None

    def get_node(self, index):
        current = self.first
        for i in range(index):
            current = current.next
            if current == self.first:
                return None
        return current

    def insert_after(self, ref_node, new_node):
        new_node.prev = ref_node
        new_node.next = ref_node.next
        new_node.next.prev = new_node
        ref_node.next = new_node

    def insert_before(self, ref_node, new_node):
        self.insert_after(ref_node.prev, new_node)

    def insert_at_end(self, new_node):
        if self.first is None:
            self.first = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            self.insert_after(self.first.prev, new_node)

    def insert_at_beg(self, new_node):
        self.insert_at_end(new_node)
        self.first = new_node

    def remove(self, node):
        if self.first.next == self.first:
            self.first = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            if self.first == node:
                self.first = node.next

    def display(self):
        if self.first is None:
            return
        current = self.first
        while True:
            print(current.data, " ", end="")
            current = current.next
            if current == self.first:
                print()
                break




def parse_input_to_game_rules():
    with open("input.txt", "r") as file:
        inpt = file.read()
        num_players = int(inpt.split(";")[0].split(" ")[0])
        num_balls = int(inpt.split(";")[1].split(" ")[5])

    return (num_players, num_balls)


def play_game(num_players, num_balls):
    curr_player = 0
    players = [0] * num_players

    circle = CircularDoublyLinkedList()
    first_node = Node(0)
    circle.insert_at_beg(first_node)
    circle.display()
    curr_marble_in_circ = circle.get_node(0)

    percentage = num_balls / 100
    if not percentage:
        percentage = 1

    completion_percent = 0
    for ball in range(1, num_balls + 1):
        current_ball = ball
        if current_ball % percentage == 0:
            completion_percent += 1
            print(completion_percent, "%")

        if current_ball % 23 == 0:
            players[curr_player] += current_ball
            for i in range(7):
                curr_marble_in_circ = curr_marble_in_circ.prev

            players[curr_player] += curr_marble_in_circ.data
            new_node = curr_marble_in_circ.next
            circle.remove(curr_marble_in_circ)
            curr_marble_in_circ = new_node
        else:
            new_node = Node(current_ball)
            circle.insert_after(curr_marble_in_circ.next, new_node)
            curr_marble_in_circ = new_node

        curr_player = (ball - 1) % num_players
        #circle.display()

    print(max(players))

def part_one():
    num_players, num_balls = parse_input_to_game_rules()
    play_game(num_players, num_balls)

def part_two():
    print("Starting calculations")
    num_players, num_balls = parse_input_to_game_rules()
    play_game(num_players, num_balls * 100)


#part_one()
part_two()
