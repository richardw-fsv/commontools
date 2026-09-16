from datetime import datetime, timedelta

def difftime(dt_from:datetime, dt_to:datetime) -> int:
    duration:timedelta = dt_to - dt_from
    return duration.days * (24 * 3600) + duration.seconds

def formattime(secs:int) -> str:
    hours = secs // 3600
    minutes = (secs % 3600) // 60
    seconds = secs % 60
    return f"{hours}:{minutes}:{seconds}"

def test():
    print("Testing the functions")
    sunrise:datetime =  datetime.fromisoformat("2026-09-15T07:59:52+02:00")
    sunset:datetime = datetime.fromisoformat("2026-09-15T20:25:22+02:00")
    print(f"Calculated day duration: {formattime(difftime(sunrise, sunset))}")