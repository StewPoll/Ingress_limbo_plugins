"""!checkpoint or !cycle will return time of the next Ingress checkpoint (and cycle end date), should be working in AEST due to time. """
import re
from datetime import datetime, timedelta
from time import mktime

def on_message(msg, server):
    text = msg.get("text", "")
    match = re.findall(r"!(?:checkpoint|cycle)", text)
    if not match:
        return

    # time zero, a reference point for a cycle's beginning
    t0 = datetime.strptime('2015-06-24 20', '%Y-%m-%d %H')  # In AEST timezone
    hours_per_cycle = 175
    hours_per_cp = 5
    t = datetime.utcnow() + timedelta(hours=10)  # converting to AEST timezone

    seconds_from_t0 = mktime(t.timetuple()) - mktime(t0.timetuple())
    cycles_from_t0 = seconds_from_t0 // (3600 * hours_per_cycle)
    cycle_start = t0 + timedelta(hours=cycles_from_t0 * hours_per_cycle)
    cycle_end = cycle_start + timedelta(hours=hours_per_cycle)

    seconds_from_cycle_start = mktime(t.timetuple()) - mktime(cycle_start.timetuple())
    next_cp_num = (seconds_from_cycle_start // (3600 * hours_per_cp)) + 1   # +1 -- rounding up
    next_cp = cycle_start + timedelta(hours=(next_cp_num) * hours_per_cp)

    #print ("Next CP#{!s} in: {!s}, at: {:%H:%M} \r\nCycle ends in {!s} at {:%Y-%m-%d %H:%M}".format(
    #    int(next_cp_num), ':'.join(str(next_cp - t).split(':')[:2]), next_cp, ':'.join(str(cycle_end - t).split(':')[:2]), cycle_end))

    rem_cycle = cycle_end - t
    rem_hours = rem_cycle.seconds//3600
    rem_minutes = (timedelta(seconds=rem_cycle.seconds) - timedelta(hours=rem_hours)).seconds//60

    return ("Next CP#{!s} in: {!s}, at: {:%H:%M} \r\nCycle ends in {!s} days {!s} hours {!s} mins at {:%Y-%m-%d %H:%M}".format(
    int(next_cp_num), ':'.join(str(next_cp - t).split(':')[:2]), next_cp, rem_cycle.days, rem_hours, rem_minutes, cycle_end))
