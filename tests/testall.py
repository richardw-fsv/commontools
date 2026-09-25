from datetime import datetime
from rwcommontools import mydate

def test_datetools():
    print("Testing the functions")
    t1:str = "2026-09-15T07:59:52+02:00"
    t2:str = "2026-09-15T20:25:22+02:00"
    dt1:datetime =  datetime.fromisoformat(t1)
    dt2:datetime = datetime.fromisoformat(t2)
    print(f"Datetime1: {dt1.strftime("%X")}")
    print(f"Datetime2: {dt2.strftime("%X")}")
    print(f"Time difference: {mydate.formattime(mydate.difftime(dt1, dt2))}")

test_datetools()