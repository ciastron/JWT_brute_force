import binascii
import hmac
import hashlib
import base64
import sys
from os.path import exists
from optparse import OptionParser


parser = OptionParser()
parser.add_option("-t", "--token", dest="JWT", type="string",
                  help="JWT Token")
parser.add_option("-w", "--wordlist", dest="wordlist", type="string",
                  help="Word List file")
(options, args) = parser.parse_args()

if not (options.JWT and options.wordlist):
    print("Insert JWT or Wordlist")
    exit(0)


try: 
    JWT = options.JWT
    msg = (JWT.split(".")[0] + "." + JWT.split(".")[1]).encode('utf-8')
    digest = JWT.split(".")[2]
except Exception as e:
    print("Format of JWT wrong")
    exit(0)

file_exists = exists(options.wordlist)
if not file_exists:
    print("File does not exist")
    exit(0)

with open(options.wordlist) as file:
    lines = file.readlines()
    for line in lines:
        line = line.rstrip()
        dig = hmac.new(line.encode('utf-8'), msg=msg, digestmod=hashlib.sha256).digest()
        dig64 = str(base64.b64encode(dig).decode('utf-8')).replace("=","").replace("+","-").replace("/","_")
        if dig64==digest:
            print("Password found: " + str(line))
            break


