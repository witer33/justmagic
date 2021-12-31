# justmagic

Use a function like a static method with this mystic script, as in Nim.
<br />

# Just an example

```python
import justmagic

justmagic.inject()


class Person:

    def __init__(self, name: str) -> None:
        self.name = name


def hello(who: Person, prefix: str):
        print(f"Hello {prefix} {who.name}")

me = Person("John")

me.hello("mr.")
```
