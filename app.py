"""Calculate how many cartons an order needs and the space left in the final carton."""

import argparse


def positive(text):
    value = int(text)
    if value < 1:
        raise argparse.ArgumentTypeError("Expected an integer of at least 1")
    return value


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("units", type=positive)
    parser.add_argument("capacity", type=positive)
    args = parser.parse_args()
    try:
        full, leftover = divmod(args.units, args.capacity)
        print(f"Cartons required: {full + bool(leftover)}")
        print(f"Unused spaces: {(-args.units) % args.capacity}")
    except ValueError as error:
        parser.exit(1, f"{error}\n")


if __name__ == "__main__":
    main()
