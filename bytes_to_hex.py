import sys
import base64
from Crypto.Util.number import *
from pwn import xor

def XOR(a,b):
    str = ""
    for o in a:
        str += chr(ord(o) ^ b)
    return str  

string = ""

string = bytes.fromhex(string)
print(string)
