import justmagic
import json

justmagic.install(strict=False)


def multiply(x: str, y: int) -> str:
    return x * y


def main():

    def add(x: int, y: int) -> int:
        return x + y

    print("ciao".multiply(3))
    print((4).add(3))


if __name__ == '__main__':
    main()

{"a": 1}.json.dumps().print()