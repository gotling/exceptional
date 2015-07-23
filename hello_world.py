from exceptional import *


def main():
    try:
        hello()
        raise NoException()
    except StringException as e:
        print e.message


def hello():
    raise StringException('Hello world!')


if __name__ == "__main__":
    main()