"""Verify the worked examples for the Amos 1243 Identity."""

from fractions import Fraction


def amos_1243(x: Fraction) -> Fraction:
    if x == 0:
        raise ValueError("The Amos 1243 Identity is undefined at zero.")

    return x / (x / 1028) + 215


if __name__ == "__main__":
    for example in ("7", "83", "-19", "3.5", "2003"):
        result = amos_1243(Fraction(example))
        if result != 1243:
            raise AssertionError(f"Expected 1243 for {example}, got {result}")
        print(f"f({example}) = {result}")