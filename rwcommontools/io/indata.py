from typing import Final
from inputimeout import inputimeout

DEFAULT_TIMEOUT:Final[int] = 30

def get_int(pr:str = "Enter an integer", timeout:int=DEFAULT_TIMEOUT) -> int:
    while True:
        data:str = timed_input(f"{pr}: ", timeout)
        if data.isnumeric():
            return int(data)
        print("Input must be an integer ... try again")

def get_float(pr:str = "Enter a float value: ", timeout:int=DEFAULT_TIMEOUT) -> float:
     while True:
        data:str = timed_input(f"{pr}: ", timeout)
        if is_float(data):
            return float(data)
        print("Input must be a decimal value ... try again", end="\n\n")

def is_float(val:str) -> bool:
    try:
        float(val)
        return True
    except ValueError:
        return False

def timed_input(pr:str, timeout:int=DEFAULT_TIMEOUT) -> str:
    try:
        val:str = inputimeout(pr, timeout)
        return val
    except Exception: 
        raise TimeoutError("Keyboard entry timed out")  

