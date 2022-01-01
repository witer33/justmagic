import inspect
import fishhook
from typing import Callable, List, Union, Any
import builtins


def _explore_frame(stack: List[inspect.FrameInfo], name: str) -> Callable:
    for frame_info in stack:
        var = frame_info.frame.f_locals.get(name)
        if var:
            return var
    var = builtins.__dict__.get(name, None)
    return var


class JustACallable:

    def __init__(self, obj: Any, func: Union[Callable, Any]):
        self.obj = obj
        self.func = func

    def __call__(self, *args, **kwargs):
        return self.func(self.obj, *args, **kwargs)

    def __getattr__(self, name: str):
        self.func = self.func.__dict__.get(name, None)
        if not self.func:
            raise AttributeError(name)
        return self


def inject() -> None:
    @fishhook.hook(object)
    def __getattr__(self, attr: str = "_"):
        if attr.startswith("_"):
            raise AttributeError(f"function {attr} is not defined")
        f = _explore_frame(inspect.stack()[1:], attr)
        if not f:
            raise AttributeError(f"function {attr} is not defined")
        return JustACallable(self, f)


inject()