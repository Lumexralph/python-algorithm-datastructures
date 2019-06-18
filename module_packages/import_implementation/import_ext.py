"""A minimal implementation of import from David Beazley
tutorial in pycon 2015
"""

import types

def import_module(modulename):
    # make it a python file
    sourcepath = modulename + '.py'
    
    with open(sourcepath, 'r') as file:
        sourcecode = file.read()
    # create a module
    mod = types.ModuleType(modulename)
    # set the source file attributes
    mod.__file__ = sourcepath
    
    code = compile(sourcecode, sourcepath, 'exec')
    exec(code, mod.__dict__)
    return mod