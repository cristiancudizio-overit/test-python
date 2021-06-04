import os
import base64
from cryptography.fernet import Fernet
from cryptography.fernet import InvalidToken
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
import binascii
import json
import getpass

v_newpassword = input('newpassword:  ')
v_password = getpass.getpass("password:")
with open('data3.txt') as json_file:
    data = json.load(json_file)
    #print(data['luca']['password'])
    salt_encoded = data['luca']['salt']
salt_decoded = base64.urlsafe_b64decode(salt_encoded)
kdf = Scrypt(
    salt=salt_decoded,
    length=32,
    n=2**14,
    r=8,
    p=1,
)
key = kdf.derive(v_password.encode('utf-8'))
#print("v_password encoded ",v_password.encode('utf-8'))
key_encoded = base64.urlsafe_b64encode(key)
#print(key_encoded)
f = Fernet(key_encoded)
try:
    msg = f.decrypt(bytes(data['luca']['password'],'ascii'))
except InvalidSignature as e:
        errorObj, = e.args
        print("Error Code:", errorObj.code)
        print("Error Message:", errorObj.message)
        print("EXIT signature in decrypt!!!")
        exit()
except InvalidToken as e:
        #errorObj, = e.args
        #print("Error Code:", errorObj.code)
        #print("Error Message:", errorObj.message)
        print(e)
        print("EXIT token during decrypt!!!")
        exit()
print(msg.decode())
#now save json with msg encoded with new password
kdf = Scrypt(
    salt=salt_decoded,
    length=32,
    n=2**14,
    r=8,
    p=1,
)
key = kdf.derive(v_newpassword.encode('utf-8'))
key_encoded = base64.urlsafe_b64encode(key)
f = Fernet(key_encoded)
token = f.encrypt(msg)
token_dec = token.decode()
data['luca']['password'] = token_dec
print(data)
with open('data3.txt','w') as outfile:
    json.dump(data, outfile,indent=4)
#now add a new element
v_newenv = input('newenv:  ')
v_newusername = input('newusername:  ')
v_newmsg = input('newpassword:  ')
#data[v_newenv]= {"username": v_newusername,"password":"newpassword", "salt":"newsalt"}
data[v_newenv][v_newusername]= {"password":"newpassword", "salt":"newsalt"}
#data[v_newenv]['salt'] = salt_encoded
data[v_newenv][v_newusername]['salt'] = salt_encoded
kdf = Scrypt(
    salt=salt_decoded,
    length=32,
    n=2**14,
    r=8,
    p=1,
)
key = kdf.derive(v_newpassword.encode('utf-8'))
token = f.encrypt(v_newmsg.encode('utf-8'))
#data[v_newenv]['password'] = token.decode()
data[v_newenv][v_newusername]['password'] = token.decode()
with open('data3.txt','w') as outfile:
    json.dump(data, outfile,indent=4)

#get a value:
v_env = input('env:  ')
v_username = input('username:  ')
with open('data3.txt') as json_file:
    data = json.load(json_file)
print(data[v_env][v_username])