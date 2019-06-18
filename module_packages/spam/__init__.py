from . import foo
from . import bar

__all__ = []

# create a decorator to add a function or
# method to the globals of the module
def export(defn):
    # returns dictionary for all the names in scope
    globals()[defn.__name__] = defn

    # add the function or method to __all__
    # to control the names that will be exported at top level
    __all__.append(defn.__name__)
    return defn

