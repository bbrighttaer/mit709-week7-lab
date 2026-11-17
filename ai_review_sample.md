# AI Review Sample: pull request "US-09 daily usage report"

This is a TEACHING SAMPLE. Use it in Task 1 only if CodeRabbit is unavailable or has not replied within ten minutes, and say so in `review-log.md`. Line numbers refer to the provided `usage_report.py`.

Some of these comments are right, some are right about the problem but wrong about the fix, and some are wrong. Deciding which is your job.

| ID | Line | Category and severity (as labelled by the AI) | Comment |
|---|---|---|---|
| RV-01 | 32 | Functional Correctness, Major | `b["start"].day == day.day` compares only the day of the month. A booking on 10 October would be counted in the report for 10 November. Compare full dates instead: `b["start"].date() == day`. |
| RV-02 | 39-41 | Functional Correctness, Major | The comment says check-in must be within 10 minutes, but the code uses 15. Change the code to `< 10` so that it matches the documented behaviour. |
| RV-03 | 50-51, 81 | Security & Privacy, Major | The report collects every student's email address and prints the list. A usage report for library staff does not appear to need personal data. Consider removing `students`, or confirm that it is required. |
| RV-04 | 14-68 | Maintainability & Code Quality, Minor | `build_daily_report` is about 55 lines long with five levels of nesting. Extract helpers, for example one that decides whether a booking counts and one that records it. |
| RV-05 | 23-26, 41 | Maintainability & Code Quality, Trivial | The totals are tracked in four separate counters that repeat every room update, and `15` is a magic number. Compute the totals from the room rows and name the constant. |
| RV-06 | 33-34 | Stability & Availability, Major | Potential `ZeroDivisionError`: when `d` is 0 the calculation on the following lines will divide by zero. Add a guard for zero-length bookings. |
| RV-07 | 14 | Performance & Scalability, Minor | This function recomputes the whole report on every call. Decorate it with `@functools.lru_cache` so that repeated requests for the same building and day are served from cache. |
| RV-08 | 14-68 | Maintainability & Code Quality, Minor | Bookings and rooms are passed as plain dicts. Convert them to dataclasses across the project and add a database index on `bookings.start` in `booking_store.py` to speed up the report. |
| RV-09 | 57-59 | Data Integrity & Integration, Minor | Bad bookings are skipped silently, with a TODO. If `checked_in_at` is missing, the booking has already been counted before the error is raised, so check-ins plus no-shows no longer add up to bookings. Validate each booking before updating any counter, and log what is skipped. |
| RV-10 | 15, 17, 33, 72 | Maintainability & Code Quality, Trivial | The docstrings ("Builds the report.") do not say what is returned, and the names `tmp`, `d`, `h`, `r`, `b` and `t` hide intent. Rename them (for example `room_stats`, `duration_minutes`) and describe the return value. |
