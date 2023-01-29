from Control import Control, ControlName

def test_case() -> None:
    for control in ControlName:
        Control.get_control_value(control)
    
    Control.show_cache()
