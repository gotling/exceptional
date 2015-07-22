from exceptional import *


def main():
    try:
        hello()
        raise NoException()
    except Exception as e:
        if type(e) == StringException:
            print e.message


def hello():
    raise StringException('Hello world!')


if __name__ == "__main__":
    main()