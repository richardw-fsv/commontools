import sys
from typing import Final
import keyring
 
DEFAULT_KEYNAME:Final[str] = "api-key"

def get_api_key(site: str, keyname=DEFAULT_KEYNAME, exit_if_not_found:bool=True) -> str:
    """
    If the parameter 'exit_if_not_found' is false, this function returns an empty string
    """
    try:
        key: str | None = keyring.get_password(site, keyname)
        if key is None:
            raise SystemError(f"Unable to find api key for site {site}")
        return key
    except SystemError as ex:
        if (exit_if_not_found):
            sys.exit(f"Program terminated abnormally: {str(ex)}")
        else:
            print(str(ex))
            return ""