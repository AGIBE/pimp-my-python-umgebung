# type checking (ty) warnt wenn eine Variable (x) möglicherweise nicht definiert ist


def main():

    try:
        # Cannot divide object of type `Literal[1]` by zero
        result: float = 1 / 0
        x = 0
    except Exception as e:
        # Name `x` used when possibly not defined
        print(f"Caught an exception: {e} with {x}")

    # Name `result` used when possibly not defined
    print(result)


if __name__ == "__main__":
    main()
