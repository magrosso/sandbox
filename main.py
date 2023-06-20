from Laser import Laser
import Test


def main():
    Laser.print_config()
    Laser.save_config()
    Test.run_tests()
    # Laser.clear_config()
    Laser.print_config()


if __name__ == "__main__":
    main()
