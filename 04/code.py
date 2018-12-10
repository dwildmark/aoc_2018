import dateutil.parser as dp

def parse_input():
    event_array = []
    with open("input.txt", "r") as file:
        for line in file:
            date = line[1:17]
            parsed_date = dp.parse(date)
            event = line[19:]
            print parsed_date, event
            event_array.append((parsed_date, event))


    return event_array

def determine_nisse_schedules(event_array):
    nisse_schedules = {}
    current_nisse = ""
    for event in event_array:
        if "Guard" in event[1]:
            current_nisse = int(event[1].split("#")[1].split(" ")[0])
            print current_nisse


events = parse_input()
events.sort()

determine_nisse_schedules(events)
