import dateutil.parser as dp
import dateutil
from datetime import timedelta as td
from collections import defaultdict

def parse_input():
    event_array = []
    with open("input.txt", "r") as file:
        for line in file:
            date = line[1:17]
            parsed_date = dp.parse(date)
            event = line[19:]
            event_array.append((parsed_date, event))


    return event_array

def determine_nisse_sleeptimes(event_array):
    nisse_sleepsum = defaultdict(int)
    nisse_individual_sleep_sched = dict()
    nisse_fell_asleep = dict()
    nisse = ""
    for event in event_array:
        if "Guard" in event[1]:
            current_nisse = int(event[1].split("#")[1].split(" ")[0])
            if current_nisse not in nisse_individual_sleep_sched:
                nisse_individual_sleep_sched[current_nisse] = defaultdict(int)
        elif "falls" in event[1]:
            nisse_fell_asleep[current_nisse] = event[0]
        elif "wakes" in event[1]:
            delta_time = int((event[0] - nisse_fell_asleep[current_nisse]).total_seconds() / 60)
            print delta_time
            nisse_sleepsum[current_nisse] += delta_time
            for minute in range(delta_time):
                nisse_individual_sleep_sched[current_nisse][(nisse_fell_asleep[current_nisse] + td(minutes=minute)).minute] += 1
        else:
            raise NisseException("Input error")

    print nisse_sleepsum
    max_nisse, _ = max(nisse_sleepsum.items(), key=lambda x:x[1])
    max_minute, _ = max(nisse_individual_sleep_sched[max_nisse].items(), key=lambda x:x[1])

    print "Nisse #", max_nisse, "minute", max_minute
    print max_nisse * max_minute


    strat_2_max_minutes = 0
    strat_2_leading_nisse = 0
    strat_2_leading_minute = 0
    for nisse in nisse_individual_sleep_sched:
        print nisse
        print nisse_individual_sleep_sched[nisse]
        try:
            best_minute_of_nisse, nof_minutes = max(nisse_individual_sleep_sched[nisse].items(), key=lambda x:x[1])
        except ValueError:
            continue
        if nof_minutes > strat_2_max_minutes:
            strat_2_max_minutes = nof_minutes
            strat_2_leading_nisse = nisse
            strat_2_leading_minute = best_minute_of_nisse

    print "Nisse #", strat_2_leading_nisse, "minute", strat_2_leading_minute
    print strat_2_leading_nisse * strat_2_leading_minute

events = parse_input()
events.sort()

determine_nisse_sleeptimes(events)
