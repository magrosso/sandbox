from src.Helper import convert_to_unit, convert_to_micro

import pytest


@pytest.mark.parametrize(
    "value, src_unit, result, target_unit",
    [
        (1, "", 1_000_000, "µ"),  # 1 to micro
        (1, "n", 0.001, "µ"),  # nano to micro
        (1, "p", 0.000001, "µ"),  # pico to micro
        (1, "m", 1_000, "µ"),  # milli to micro
        (1, "", 1_000_000_000, "n"),  # 1 to nano
        (1, "n", 1, "n"),  # nano to nano
        (1, "p", 0.001, "n"),  # pico to nano
        (1, "m", 1_000_000, "n"),  # milli to nano
        (1, "", 1_000_000_000_000, "p"),  # 1 to pico
        (1, "n", 1_000, "p"),  # nano to pico
        (1, "p", 1, "p"),  # pico to pico
        (1, "m", 1_000_000_000, "p"),  # milli to pico
    ],
)
def test_convert_to_unit(value: float, src_unit: str, result: float, target_unit: str) -> None:
    result_as_target_unit: float = convert_to_unit(source_value=value, source_unit=src_unit, target_unit=target_unit)
    assert (
        result_as_target_unit == result
    ), f"Failed to convert {value} {src_unit} to {result_as_target_unit} {target_unit}, expected {result} {target_unit}"


@pytest.mark.parametrize(
    "value, unit, result",
    [
        (1, "nm", 0.000001),
        (1, "N", 1_000),
        (1, "P", 1_000_000),
        (1, "M", 0.001),
    ],
)
def test_convert_to_micro_raises_ValueError(value: float, unit: str, result) -> None:
    with pytest.raises(ValueError) as ex_info:
        result_micro: float = convert_to_micro(source_value=value, source_unit=unit)
    print(f"{ex_info.type}: {ex_info.value}")
