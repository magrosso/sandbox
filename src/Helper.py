from enum import Enum
from functools import partial


class Exponent(Enum):
    ONE = 0
    MILLI = -3
    MICRO = -6
    NANO = -9
    PICO = -12


def convert_to_unit(source_value: float, source_exp: str, target_exp: str) -> float:
    # exp = {"p": -12, "n": -9, "µ": -6, "m": -3, "": 0}
    exp = {
        "p": Exponent.PICO,
        "n": Exponent.NANO,
        "µ": Exponent.MICRO,
        "m": Exponent.MILLI,
        "": Exponent.ONE,
    }
    try:
        calc_exp: int = exp[source_exp].value - exp[target_exp].value
        if calc_exp == 0:
            return source_value
        return source_value * pow(base=10, exp=calc_exp)
    except KeyError as ex:
        raise ValueError(f"Invalid unit '{source_exp}', valid units are: {Exponent}") from ex


convert_to_micro = partial(convert_to_unit, target_exp="µ")
convert_to_nano = partial(convert_to_unit, target_exp="n")
convert_to_pico = partial(convert_to_unit, target_exp="p")
convert_to_milli = partial(convert_to_unit, target_exp="m")
