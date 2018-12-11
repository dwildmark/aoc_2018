def parse_instructions():
    instruction_set = dict()
    with open("input.txt", "r") as file:
        for line in file:
            tag = line[36]
            tag_2 = line[5]
            if tag_2 not in instruction_set:
                instruction_set[tag_2] = dict(tag = tag_2, requirements = [])
            if tag not in instruction_set:
                instruction_set[tag] = dict(tag = tag, requirements = [line[5]])
            else:
                instruction_set[tag]["requirements"].append(line[5])

    instruction_list = []
    for instr in instruction_set:
        instruction_list.append(instruction_set[instr])

    return instruction_list


def get_available_instructions(queued_instr, avail_instr):
    for instr in queued_instr:
        if not instr["requirements"]:
            avail_instr.append(instr)

    for moved_instr in avail_instr:
        if moved_instr in queued_instr:
            queued_instr.remove(moved_instr)

def execute_instruction(instr, queued_instr):
    for i in queued_instr:
        if instr["tag"] in i["requirements"]:
            i["requirements"].remove(instr["tag"])


def part_one():
    queued_instructions = parse_instructions()
    available_instructions = []
    get_available_instructions(queued_instructions, available_instructions)
    executed_instructions = []

    while available_instructions:
        available_instructions.sort()
        execute_instruction(available_instructions[0], queued_instructions)
        executed_instructions.append(available_instructions[0]["tag"])
        available_instructions.remove(available_instructions[0])
        get_available_instructions(queued_instructions, available_instructions)

    print executed_instructions

part_one()
