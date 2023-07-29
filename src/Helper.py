from functools import partial


def convert_to_unit(source_value: float, source_unit: str, target_unit: str) -> float:
    exp = {"p": -12, "n": -9, "µ": -6, "m": -3, "": 0}
    try:
        source_exp: int = exp[source_unit]
        target_exp: int = exp[target_unit]
        calc_exp: int = source_exp - target_exp
        if calc_exp == 0:
            return source_value
        return source_value * pow(base=10, exp=calc_exp)
    except KeyError as ex:
        raise ValueError(f"Invalid unit '{source_unit}', valid units are: {exp.keys()}") from ex


convert_to_micro = partial(convert_to_unit, target_unit="µ")
convert_to_nano = partial(convert_to_unit, target_unit="n")
convert_to_pico = partial(convert_to_unit, target_unit="p")
convert_to_milli = partial(convert_to_unit, target_unit="m")
