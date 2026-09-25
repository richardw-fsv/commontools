from datetime import datetime, timedelta

def difftime(dt_from:datetime, dt_to:datetime) -> int:
    duration:timedelta = dt_to - dt_from
    return duration.days * (24 * 3600) + duration.seconds

def formattime(secs:int) -> str:
    hours = secs // 3600
    minutes = (secs % 3600) // 60
    seconds = secs % 60
    return f"{hours}:{minutes}:{seconds}"
