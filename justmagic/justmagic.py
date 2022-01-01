import inspect
import fishhook
from typing import Callable, List, Union, Any, get_type_hints
import builtins


def _explore_frame(stack: List[inspect.FrameInfo], name: str) -> Callable:
    for frame_info in stack:
        var = frame_info.frame.f_locals.get(name)
        if var:
            return var
    var = builtins.__dict__.get(name, None)
    return var


class JustACallable:

    def __init__(self, obj: Any, func: Union[Callable, Any], strict: bool = False):
        self.obj = obj
        self.func = func
        self.strict = strict
        self._check_types()

    def __call__(self, *args, **kwargs):
        return self.func(self.obj, *args, **kwargs)

    def _check_types(self) -> None:
        if self.strict and isinstance(self.func, Callable):
            hints_types = list(get_type_hints(self.func).values())
            if not (len(hints_types) >= 1 and isinstance(self.obj, hints_types[0])):
                raise TypeError(f"type mismatch: {self.obj} is not an instance of "
                                f"{hints_types[0] if len(hints_types) > 0 else '<unknown>'}")

    def __getattr__(self, name: str):
        self.func = self.func.__dict__.get(name, None)
        self._check_types()
        if not self.func:
            raise AttributeError(name)
        return self


def install(strict: bool = False) -> None:
    @fishhook.hook(object)
    def __getattr__(self, attr: str = "_"):
        if attr.startswith("_"):
            raise AttributeError(f"function {attr} is not defined")
        f = _explore_frame(inspect.stack()[1:], attr)
        if not f:
            raise AttributeError(f"function {attr} is not defined")
        return JustACallable(self, f, strict)