import requests
from Crypto.Cipher import AES
import hashlib
import random

BASE_URL = "https://aes.cryptohack.org/passwords_as_keys/"

r = requests.get(f"{BASE_URL}/encrypt_flag")
data = r.json()
ciphertext = data["ciphertext"]
print("ciphertext", ciphertext)

#password = "password"
ciphertext = 'c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66'
ciphertext = bytes.fromhex(ciphertext)

with open("/usr/share/dict/words") as f:
    words = [w.strip() for w in f.readlines()]
keyword = random.choice(words)
#print(keyword)
#print(words)

KEY = hashlib.md5(keyword.encode()).digest()

ciphertext = '0adfe41f596b4f2f05a2935d399b5a93811b1fb539cdfb33e6e5348f8d245641'
ciphertext = bytes.fromhex(ciphertext)
#print(KEY)


for word in words:
    password = hashlib.md5(word.encode()).digest()
    cipher = AES.new(password, AES.MODE_ECB)
    
    try:
        decrypted = cipher.decrypt(ciphertext)
    except:
        pass
    
    try:
        print("flag", bytearray.fromhex(decrypted.hex()).decode())
    except:
        pass
print(decrypted)
print("flag", bytearray.fromhex(decrypted.hex()).decode())
