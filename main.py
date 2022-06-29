import sys
import json
from parser import parser
from sample_generator import SampleGenerator


def main():
    input = get_input()
    typedefs = parser.parse(input)
    sample = SampleGenerator(typedefs).generate()
    sample_json = json.dumps(sample)

    write_output(sample_json)


def get_input():
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as input:
            return input.read()
    else:
        return sys.stdin.read()


def write_output(json):
    if len(sys.argv) > 2:
        with open(sys.argv[2], "w") as output:
            output.write(json)
    else:
        sys.stdout.write(json)


if __name__ == "__main__":
    main()
