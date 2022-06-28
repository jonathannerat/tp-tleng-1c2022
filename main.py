import sys
from parser import parser


def main():
    input = get_input()

    result = parser.parse(input)

    for typedef in result:
        write_output(str(typedef))


def get_input():
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as input:
            return input.read()
    else:
        return sys.stdin.read()


def write_output(s):
    if (len(sys.argv) > 2):
        with open(sys.argv[2]) as output:
            output.write(s)
    else: 
        sys.stdout.write(s)

if __name__ == "__main__":
    main()
