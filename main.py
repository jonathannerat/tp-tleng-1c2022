import sys
from parser import parser


def main():
    input = get_input()
    result = parser.parse(input)

    write_output(result)


def get_input():
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as input:
            return input.read()
    else:
        return sys.stdin.read()


def write_output(typedefs):
    if len(sys.argv) > 2:
        with open(sys.argv[2], "r+") as output:
            # limpiar el archivo
            output.seek(0)
            output.truncate()
            for typedef in typedefs:
                output.write(str(typedef))
    else:
        for typedef in typedefs:
            sys.stdout.write(str(typedef))


if __name__ == "__main__":
    main()
