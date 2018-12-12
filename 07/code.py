import string

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

def get_job_time(job):
    index = string.ascii_uppercase.index(job["tag"])
    return 60 + index + 1


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


def part_two():
    worker_pool = [
        dict(time_left =  0, current_work = dict()),
        dict(time_left =  0, current_work = dict()),
        dict(time_left =  0, current_work = dict()),
        dict(time_left =  0, current_work = dict()),
        dict(time_left =  0, current_work = dict())]

    busy_workers = []

    q_instr = parse_instructions()
    ip_instr = []
    a_instr = []
    e_instr = []

    seconds = 0



    while True:
        for worker in busy_workers[:]:
            if worker["time_left"] == 0:
                print "Worker", worker, "done with job"
                busy_workers.remove(worker)
                execute_instruction(worker["current_work"], q_instr)
                worker["current_work"] = dict()
                worker_pool.append(worker)


        get_available_instructions(q_instr, a_instr)
        a_instr.sort()
        while a_instr and worker_pool:
            worker = worker_pool.pop()
            job = a_instr.pop(0)
            worker["time_left"] = get_job_time(job)
            worker["current_work"] = job
            busy_workers.append(worker)

        for worker in busy_workers:
            worker["time_left"] -= 1

        if not busy_workers and not a_instr:
            print "Part two took", seconds, "seconds."
            return
        seconds += 1


part_one()
part_two()

