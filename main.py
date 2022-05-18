import sys
from os.path import exists
from optparse import OptionParser
from files.bruteForce import JWT_brute_force

parser = OptionParser()
parser.add_option("-t", "--token", dest="JWT", type="string",
                  help="JWT Token")
parser.add_option("-w", "--wordlist", dest="wordlist", type="string",
                  help="Word List file")
(options, args) = parser.parse_args()

if not (options.JWT):
    print("Insert JWT")
    exit(0)


try: 
    JWT = options.JWT
    msg = (JWT.split(".")[0] + "." + JWT.split(".")[1]).encode('utf-8')
    digest = JWT.split(".")[2]
except Exception as e:
    print("Format of JWT wrong")
    exit(0)

if not(options.wordlist):
    wordlist = "./wordlist"
else:
    file_exists = exists(options.wordlist)
    if not file_exists:
        print("File does not exist")
        exit(0)
    wordlist = options.wordlist

res = JWT_brute_force(msg, digest, wordlist)
if res:
    print("Password found: " + res)
else:
    print("Password not found")
