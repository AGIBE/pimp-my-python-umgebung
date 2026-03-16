def main():
    print("\nBeispiel mit String")
    print(f"{no_types('Hans')=}")
    print(f"{arg_types('Sepp')=}")
    print(f"{typed('Ueli')=}")

    print("\nBeispiel mit falschem Type")
    print(f"{no_types(Person('Hans'))=}")
    print(f"{arg_types(Person('Sepp'))=}")
    print(f"{typed(Person('Ueli'))=}")

    # print("\nBeispiel wie mit returns weitergearbeitet werden kann")
    no_types("Hans") + 123
    arg_types("Sepp") + 123
    typed("Ueli") + 123

    print("\n")


def no_types(person_name):
    # Kein Autocomplete für person_name, da kein Type angegeben ist
    return f"Sälü {person_name}"


def arg_types(person_name: str):
    # Autocomplete für person_name verfügbar, da Type angegeben ist
    return f"Sälü {person_name}"


def typed(person_name: str) -> str:
    return f"Sälü {person_name}"


class Person:
    def __init__(self, name: str):
        self.name: str = name

    def __str__(self):
        return self.name


if __name__ == "__main__":
    main()
