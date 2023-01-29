from enum import Enum
# from typing import Optional
from dataclasses import dataclass
from random import randint


class ControlName(Enum):
    COMBO_A = "loc_combo_a"
    COMBO_B = "loc_combo_b"
    COMBO_C = "loc_combo_c"
    BUTTON_X = "loc_button_x"
    BUTTON_Y = "loc_button_y"
    BUTTON_Z = "loc_button_z"
    TEXT_F = "loc_text_f"

@dataclass
class ControlRecord:
    loc: str
    value: int = -1
    use_cache: bool = True
    update_count: int = 0
    hit_count: int = 0


class Control:
    # cache to keep track of all created controls
    cache: dict[str, ControlRecord] = {}

    @classmethod
    def add_control(cls, control_name: ControlName, value: int) -> ControlRecord:
        # print(f'Adding cache entry: {name}:"{value}"')
        # cls.cache[name] = value
        control = ControlRecord(loc=control_name.value, value=value)
        cls.cache[control_name.name] = control
        print(f"Cache entry created for {control_name.name}: {control}")
        return control

    @classmethod
    def show_cache(cls):
        print(f"Cache ({len(cls.cache)} entries):")
        for control_id, control in cls.cache.items():
            print(f"\t{control_id}: {control}")

    @classmethod
    def get_control_value(cls, control_name: ControlName, use_cache: bool = True) -> int:
        control = cls.cache.get(control_name.name, None)

        if control is not None:
            if use_cache and control.use_cache:
                control.hit_count += 1
                return control.value
            else:       
                control.value = randint(0, 1056)
                control.update_count += 1
                return control.value
        
        control_value = randint(0, 1056)
        cls.add_control(control_name, control_value)
        return control_value
