import justmagic
import json

justmagic.install(strict=False)


def multiply(x: str, y: int) -> str:
    return x * y


print("ciao".multiply(3))

{"a": 1}.json.dumps().print()