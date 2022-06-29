import sys
from myparser import parser


def main():
    input = get_input()
    result = parser.parse(input)
    maintype = resolve(result)
    write_output(maintype)


def get_input():
    """Obtiene el texto de entrada (stdin / 1er arg.)"""
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as input:
            return input.read()
    else:
        return sys.stdin.read()

def resolve(result):
    """Chequea y resuelve las dependencias internas en result"""
    deps = {}
    maintype = result[0]

    for typedef in result:
        deps[typedef.name] = list(typedef.get_deps().keys())

    if has_loops(deps, maintype.name, {}):
        raise Exception("La definicion tiene loops, corregir")

    resolve_dict = {}

    for typedef in result[1:]:
        resolve_dict[typedef.name] = typedef.type

    maintype.resolve(resolve_dict)

    return maintype


def has_loops(graph, start, visited):
    """Verifica si graph tiene loops, empezando por start y habiendo visitado visited"""
    visited[start] = True

    for next in graph[start]:
        if next in visited and visited[next]:
            return True
        elif has_loops(graph, next, visited):
            return True

    return False

def write_output(maintype):
    """Escribe a la salida (stdin / 2do arg) un json generado del tipo"""
    json = maintype.generate_json()

    if len(sys.argv) > 2:
        with open(sys.argv[2], "r+") as output:
            # limpiar el archivo
            output.seek(0)
            output.truncate()
            output.write(json)
    else:
        sys.stdout.write(json)


if __name__ == "__main__":
    main()
