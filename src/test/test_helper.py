from src.Helper import convert_to_unit, convert_to_micro

import pytest


@pytest.mark.parametrize(
    "src_value, src_exp, result, target_exp",
    [
        (1.0, "", 1_000_000, "µ"),  # 1 to micro
        (1.0, "m", 1_000, "µ"),  # milli to micro
        (1.0, "µ", 1.0, "µ"),  # micro to micro
        (1.0, "n", 0.001, "µ"),  # nano to micro
        (1.0, "p", 0.000001, "µ"),  # pico to micro
        # to nano
        (1.0, "", 1_000_000_000, "n"),  # 1 to nano
        (1.0, "m", 1_000_000, "n"),  # milli to nano
        (1.0, "µ", 1_000, "n"),  # micro to nano
        (1.0, "n", 1, "n"),  # nano to nano
        (1.0, "p", 0.001, "n"),  # pico to nano
        # to pico
        (1.0, "", 1_000_000_000_000, "p"),  # to pico
        (1.0, "m", 1_000_000_000, "p"),  # milli to pico
        (1.0, "µ", 1_000_000, "p"),  # micro to pico
        (1.0, "n", 1_000, "p"),  # nano to pico
        (1.0, "p", 1, "p"),  # pico to pico
        # to micro
        (-1.9, "", -1_900_000, "µ"),  # 1 to micro
        (-1.9, "m", -1_900, "µ"),  # milli to micro
        (-1.9, "µ", -1.9, "µ"),  # micro to micro
        (-1.9, "n", -0.0019, "µ"),  # nano to micro
        (-1.9, "p", -0.0000019, "µ"),  # pico to micro
        # to nano
        (-1.9, "", -1_900_000_000, "n"),  # 1 to nano
        (-1.9, "m", -1_900_000, "n"),  # milli to nano
        (-1.9, "µ", -1_900, "n"),  # micro to nano
        (-1.9, "n", -1.9, "n"),  # nano to nano
        (-1.9, "p", -0.0019, "n"),  # pico to nano
        # to pico
        (-1.9, "", -1_900_000_000_000, "p"),  # to pico
        (-1.9, "m", -1_900_000_000, "p"),  # milli to pico
        (-1.9, "µ", -1_900_000, "p"),  # micro to pico
        (-1.9, "n", -1_900, "p"),  # nano to pico
        (-1.9, "p", -1.9, "p"),  # pico to pico
        # to micro
        (345.07, "", 345_070_000, "µ"),  # to micro
        (345.07, "m", 345_070, "µ"),  # milli to micro
        (345.07, "µ", 345.07, "µ"),  # micro to micro
        (345.07, "n", 0.34507, "µ"),  # nano to micro
        (345.07, "p", 0.00034507, "µ"),  # pico to micro
        # to nano
        (345.07, "", 345_070_000_000, "n"),  # 1 to nano
        (345.07, "m", 345_070_000, "n"),  # milli to nano
        (345.07, "µ", 345_070, "n"),  # micro to nano
        (345.07, "n", 345.07, "n"),  # nano to nano
        (345.07, "p", 0.34507, "n"),  # pico to nano
        # to pico
        (345.07, "", 345_070_000_000_000, "p"),  # 1 to pico
        (345.07, "m", 345_070_000_000, "p"),  # milli to pico
        (345.07, "µ", 345_070_000, "p"),  # micro to pico
        (345.07, "n", 345_070, "p"),  # nano to pico
        (345.07, "p", 345.07, "p"),  # pico to pico
    ],
)
def test_convert_one_to_target_exponent(src_value: float, src_exp: str, result: float, target_exp: str) -> None:
    result_as_target_unit: float = convert_to_unit(source_value=src_value, source_exp=src_exp, target_exp=target_exp)
    assert result_as_target_unit == pytest.approx(
        result
    ), f"Failed to convert {src_value} {src_exp} to {result_as_target_unit} {target_exp}, expected {result} {target_exp}"


@pytest.mark.parametrize(
    "value, source_exp",
    [
        (1, "k"),
        (1, "K"),
        (1, "N"),
        (1, "P"),
        (1, "M"),
        (1, "nm"),
    ],
)
def test_invalid_source_exponent_raises_ValueError(value: float, source_exp: str) -> None:
    with pytest.raises(ValueError) as ex_info:
        convert_to_unit(source_value=value, source_exp=source_exp, target_exp="")
    print(f"{ex_info.type}: {ex_info.value}")
