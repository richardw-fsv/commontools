import datetime

def difftime(dt_from:datetime.datetime, dt_to:datetime.datetime) -> int:
    duration:datetime.timedelta = dt_to - dt_from
    return duration.days * (24 * 3600) + duration.seconds

def formattime(secs:int) -> str:
    hours = secs // 3600
    minutes = (secs % 3600) // 60
    seconds = secs % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
