import json
# così non funziona p nel ciclo for risulta una stringa
#with open('data2.txt') as json_file:
#    data = json.load(json_file)
#    for p in data['luca']:
#        #print('Userame: ' + p['username'])
#        print('hashpwd: ' + p['password'])
#        print('salt: ' + p['salt'])
#        print('')   
with open('data2.txt') as json_file:
    data = json.load(json_file)
    print(data['luca']['password'])
