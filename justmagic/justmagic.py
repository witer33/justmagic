import inspect
import fishhook


def _explore_frame(stack, name):
    for frame_info in stack:
        var = frame_info.frame.f_locals.get(name)
        if var:
            return var
    return None


def inject():
    @fishhook.hook(object)
    def __getattr__(self, attr: str = "_"):
        if attr.startswith("_"):
            raise AttributeError(f"name {attr} is not defined")
        f = _explore_frame(inspect.stack()[1:], attr)
        if not f:
            raise AttributeError(f"name {attr} is not defined")
        return lambda *args, **kwargs: f(self, *args, **kwargs)
