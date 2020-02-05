import pprint

import svn.local
#settare variabili per trovare comando svn... il modulo è solo un wrapper
r = svn.local.LocalClient('C:\OVERIT\geocall61\SCMIta-10.25\overit')
r.update()
info = r.info()
#pprint.pprint(info)
#for x in info:
#    print(x)
print(info['commit_revision'] )
print(info['entry_revision'] )
