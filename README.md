# justmagic

Use a [function as a method](https://en.wikipedia.org/wiki/Uniform_Function_Call_Syntax) with this mystic script, just like in Nim.
<br />

# Just an example

```python

import justmagic

justmagic.install(strict=False)

class Person:

    def __init__(self, name: str) -> None:
        self.name = name


def hello(who: Person, prefix: str):
    return f"Hello {prefix} {who.name}"


me = Person("John")

me.hello("mr.").print()
```
<br />
<i>Strict mode enables types checking.</i>

# Installation

```
pip3 install justmagic
```
