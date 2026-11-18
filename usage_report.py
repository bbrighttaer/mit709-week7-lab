"""StudySpace daily usage report (US-09 / PS-09).

MIT709 Week 7 practical lab. This is a TEACHING SAMPLE written to look like
typical AI-generated code. It did not come from a named model. It is the code
under review in this week's pull request: it runs, its tests pass and the
Week 6 pipeline is green, but it is not ready to merge.

A booking is a dict with the keys id, room, student_email, start, end and
checked_in_at (a datetime, or None if nobody checked in).
A room is a dict with the keys name, building and capacity.
"""


def build_daily_report(bookings, rooms, building, day):
    """Builds the report."""
    result = {"building": building, "day": str(day), "rooms": [], "students": []}
    tmp = {}
    hours = {}
    # set up the rooms
    for r in rooms:
        if r["building"] == building:
            tmp[r["name"]] = {"room": r["name"], "bookings": 0, "booked_minutes": 0, "check_ins": 0, "no_shows": 0}
    t_bookings = 0
    t_minutes = 0
    t_check_ins = 0
    t_no_shows = 0
    for b in bookings:
        try:
            if b["room"] not in tmp:
                continue
            # only bookings for this day
            if b["start"].date() == day:
                d = (b["end"] - b["start"]).total_seconds() / 60
                if d > 0:
                    tmp[b["room"]]["bookings"] = tmp[b["room"]]["bookings"] + 1
                    tmp[b["room"]]["booked_minutes"] = tmp[b["room"]]["booked_minutes"] + int(d)
                    t_bookings = t_bookings + 1
                    t_minutes = t_minutes + int(d)
                    # check-in must be within 10 minutes of the start
                    if b["checked_in_at"] is not None:
                        if (b["checked_in_at"] - b["start"]).total_seconds() / 60 < 15:
                            tmp[b["room"]]["check_ins"] = tmp[b["room"]]["check_ins"] + 1
                            t_check_ins = t_check_ins + 1
                        else:
                            tmp[b["room"]]["no_shows"] = tmp[b["room"]]["no_shows"] + 1
                            t_no_shows = t_no_shows + 1
                    else:
                        tmp[b["room"]]["no_shows"] = tmp[b["room"]]["no_shows"] + 1
                        t_no_shows = t_no_shows + 1
                    if b["student_email"] not in result["students"]:
                        result["students"].append(b["student_email"])
                    h = b["start"].hour
                    if h in hours:
                        hours[h] = hours[h] + 1
                    else:
                        hours[h] = 1
        except (KeyError, TypeError, AttributeError):
            # TODO: handle bad bookings properly
            continue
    for name in sorted(tmp):
        result["rooms"].append(tmp[name])
    result["totals"] = {"bookings": t_bookings, "booked_minutes": t_minutes, "check_ins": t_check_ins, "no_shows": t_no_shows}
    peak = None
    for h in sorted(hours):
        if peak is None or hours[h] > hours[peak]:
            peak = h
    result["peak_hour"] = peak
    return result


def format_report(report):
    """Formats the report."""
    text = "Usage report: " + report["building"] + " on " + report["day"] + "\n"
    text = text + "Room      Bookings  Minutes  Check-ins  No-shows\n"
    for r in report["rooms"]:
        text = text + r["room"].ljust(10) + str(r["bookings"]).ljust(10) + str(r["booked_minutes"]).ljust(9) + str(r["check_ins"]).ljust(11) + str(r["no_shows"]) + "\n"
    t = report["totals"]
    text = text + "TOTAL".ljust(10) + str(t["bookings"]).ljust(10) + str(t["booked_minutes"]).ljust(9) + str(t["check_ins"]).ljust(11) + str(t["no_shows"]) + "\n"
    if report["peak_hour"] is not None:
        text = text + "Peak hour: " + str(report["peak_hour"]) + ":00\n"
    text = text + "Students: " + ", ".join(report["students"]) + "\n"
    return text
