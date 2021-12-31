import inspect
import gc

def _explore_frame(stack, name):
    for frame_info in stack:
        var = frame_info.frame.f_locals.get(name)
        if var:
            return var
    return None


def _custom_getattr(self, attr: str):
    if attr.startswith("_"):
        raise AttributeError(f"name {attr} is not defined")
    f = _explore_frame(inspect.stack()[1:], attr)
    if not f:
        raise AttributeError(f"name {attr} is not defined")
    return lambda *args, **kwargs : f(self, *args, **kwargs)

def inject():
    refs = gc.get_referents(object.__dict__)
    refs[0]["__getattr__"] = _custom_getattr
