import os
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
import binascii
import json
#salt = os.urandom(16)
salt = b'6s\xa5\x90\xac|M-K?\x9c\xba\x92}1\xee'
#with same salt we got same key
print(salt.hex())
print(bytes.fromhex('3673a590ac7c4d2d4b3f9cba927d31ee'))
# derive
kdf = Scrypt(
    salt=salt,
    length=32,
    n=2**14,
    r=8,
    p=1,
)
key = kdf.derive(b"my great password")
print(key)
print("Key: ",binascii.hexlify(bytearray(key)))
# verify
kdf = Scrypt(
    salt=salt,
    length=32,
    n=2**14,
    r=8,
    p=1,
)
kdf.verify(b"my great password", key)
salt_encoded = base64.urlsafe_b64encode(salt)
key_encoded = base64.urlsafe_b64encode(key)
print('salt encoded: ', salt_encoded)
print('key encoded: ',key_encoded)
print('key encoded decoded: ' ,key_encoded.decode())
f = Fernet(key_encoded)
token = f.encrypt(b"macaco2")
print(token)
token_enc = token.decode()
print(token_enc)
msg = f.decrypt(bytes(token_enc,'ascii'))
print(msg.decode())
print(bytes('a21$'+token_enc,'ascii'))
