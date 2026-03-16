# ruff weiss auf suboptimales error handling hin
# mit allen regeln aktiviert wird zudem auf print statements hingewiesen (T201)
# soll eine warnung unterdrückt werden kann dies explizit vermerkt werden mit "# noqa: T201"


def main():
    try:
        print("Hello")  # noqa: T201
    except:
        print("Bye")


if __name__ == "__main__":
    main()
