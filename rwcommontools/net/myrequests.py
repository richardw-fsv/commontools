import requests
import json

def getrequest(url:str, args:dict = {}, format="json") -> str:
    response = requests.get(url, args)
    if response.status_code == 200:
        data:str = response.text
        if (format == "json"):
            return json.loads(data)
        else:
            return data
    else:
        raise SystemError(f"Failed to retieve data. Status code {response.status_code}")