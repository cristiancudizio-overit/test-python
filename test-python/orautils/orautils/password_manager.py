import os
import sys
import base64
from cryptography import exceptions
from cryptography.fernet import Fernet
from cryptography.fernet import InvalidToken
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
import binascii
import json
from json import JSONDecodeError
import getpass

c_salt =  "NnOlkKx8TS1LP5y6kn0x7g=="
c_json_file = "db_passwords.json"
def _getFernet(*args):
    if len(args)==0:
        v_key_password = getpass.getpass("key password:")
    else:
        v_key_password = args[0]
    salt_decoded = base64.urlsafe_b64decode(c_salt)
    kdf = Scrypt(
        salt=salt_decoded,
        length=32,
        n=2**14,
        r=8,
        p=1,
    )
    key = kdf.derive(v_key_password.encode('utf-8'))
    key_encoded = base64.urlsafe_b64encode(key)
    f = Fernet(key_encoded)
    return f
def _getJSONData(*args):
    with open(c_json_file,'r') as json_file:
        try:
            l_data = json.load(json_file)
        except JSONDecodeError as e:
            print("empty file")
            l_data = {}
        return l_data
def _putJSONData(p_data):
    with open(c_json_file,'w') as json_file:
        json.dump(p_data, json_file,indent=4)
def addElement(*argv, **kwargs):
    #now add a new element
    v_newenv = kwargs.get('env') if kwargs.get('env') != None else input('env:  ')
    v_newusername = kwargs.get('username') if kwargs.get('username') != None else input('username:  ')
    v_newpassword = kwargs.get('password') if kwargs.get('password') != None else input('password:  ')
    f = _getFernet()
    token = f.encrypt(v_newpassword.encode('utf-8'))
    data = _getJSONData()
    if (v_newenv not in data):
        print('None')
        data[v_newenv] = {}
    data[v_newenv][v_newusername]= {"password":"newpassword", "salt":"newsalt"}
    data[v_newenv][v_newusername]['salt'] = c_salt
    data[v_newenv][v_newusername]['password'] = token.decode()
    _putJSONData(data)
def getElement(*args,**kwargv):
    print(args)
    print(kwargv)
    #get a value:
    v_env = input('env:  ')
    v_username = input('username:  ')
    data = _getJSONData()
    f = _getFernet()
    try:
        v_clear_password = f.decrypt(bytes(data[v_env][v_username]['password'],'ascii'))
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
    return v_clear_password.decode()
def changeMasterPassword(*argv):
    v_oldpassword = input('old password:  ')
    v_newpassword = input('newpassword:  ')
    data = _getJSONData()
    for i_env in data:
        for i_username in data[i_env]:
            l_pwd = data[i_env][i_username]['password']
            #decript with old master password
            df = _getFernet(v_oldpassword)
            v_clear_password = df.decrypt(bytes(data[i_env][i_username]['password'],'ascii'))
            #encrypt with new master password
            ef = _getFernet(v_newpassword)
            data[i_env][i_username]['password'] = ef.encrypt(v_newpassword.encode('utf-8')).decode()
    _putJSONData(data)       
if __name__ == "__main__":
   #changeMasterPassword()
   #addElement(sys.argv[1:])
   print(sys.argv)
   a = getElement(*sys.argv[1:],a=1)
   print(a)