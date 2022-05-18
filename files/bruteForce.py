import binascii
import hmac
import hashlib
import base64
from tqdm import tqdm

def JWT_brute_force(msg, digest, wordlist):
    """
    return: Password if found else None
    """
    password = None
    with open(wordlist) as file:
        lines = file.readlines()
        for line in tqdm(lines):
            line = line.rstrip()
            dig = hmac.new(line.encode('utf-8'), msg=msg, digestmod=hashlib.sha256).digest()
            dig64 = str(base64.b64encode(dig).decode('utf-8')).replace("=","").replace("+","-").replace("/","_")
            if dig64==digest:
                password = str(line)
                break
    return password

