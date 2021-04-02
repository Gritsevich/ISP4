# sum of two numbers
import logging


logging.basicConfig(level=logging.INFO, format="%(message)s")


def main():
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
    except ValueError:
        logging.error("error")
    else:
        logging.info("sum = %s", a + b)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logging.error("KeybordInputError")
