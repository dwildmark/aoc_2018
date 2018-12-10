import difflib
def process_id(id_string):
    map = {}
    two_times = 0
    three_times = 0
    for char in id_string:
        if char in map:
            map[char] += 1
        else:
            map[char] = 1

    for key in map:
        if map[key] == 2:
            two_times = 1
        elif map[key] == 3:
            three_times = 1

    return (two_times, three_times)


with open("input.txt", 'r') as file:
    tup = []
    two_times = 0
    three_times = 0
    for line in file:
        tup = process_id(line)
        two_times += tup[0]
        three_times += tup[1]

    print two_times * three_times


with open("input.txt", "r") as file:
    lines = []
    for line in file:
        lines.append(line)

sm = difflib.SequenceMatcher(None, "", "")
for line in lines:
    sm.set_seq1(line)
    for line2 in lines:
        sm.set_seq2(line2)
        if sm.ratio() < 0.963 and sm.ratio() > 0.960:
            print line
            print line2


string_1 = "tjxmoewpqkyaiqvmndgflunszc"
string_2 = "tjxmoewwqkyaiqvmndgflunszc"

sm.set_seqs(string_1, string_2)

print "SKA VARA"
print sm.ratio()
