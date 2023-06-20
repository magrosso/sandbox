class Laser:
    _config = {}
    print("Config Init")

    @classmethod
    def save_config(cls) -> None:
        cls._config["fixed"] = True
        cls._config["name"] = "Diode 450"
        cls._config["wl"] = (450, 450)

    @classmethod
    def clear_config(cls) -> None:
        cls._config = {}

    @classmethod
    def print_config(cls) -> None:
        print(Laser._config)
