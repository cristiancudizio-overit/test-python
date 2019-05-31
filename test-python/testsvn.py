import pprint

import svn.local

r = svn.local.LocalClient('C:\OVERIT\geocall61\Edelnor-1.0\overit')
info = r.info()
pprint.pprint(info)
