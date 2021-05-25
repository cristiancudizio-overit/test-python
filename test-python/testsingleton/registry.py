"""help, try: from testsingleton import registry
 why import testsingleton.registry doesn't work?
 you can use 'import testsingleton.registry as myreg'
 see https://docs.python.org/3/reference/simple_stmts.html#the-import-statement"""

_registry = []
def register(name):
    _registry.append(name)

def registered_names():
    return iter(_registry)