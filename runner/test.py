import importlib.util
spec = importlib.util.spec_from_file_location("schema1test123", "/home/stas/Work/ZaryaTech/drknengine/runner/db/scenario/schema1/schema1test.py")

mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

val="B3"

setattr(mod, "B3", 1)

from multiprocessing import Value
import ctypes

val = Value(ctypes.c_int)
setattr(mod, "I1", val)


fn = getattr(mod, "set_I1")

fn(4)
print(val.value)
