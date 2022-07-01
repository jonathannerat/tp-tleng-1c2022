#!/usr/bin/env python
import sys
from myparser import parser
from myerror import TPError


def main():
    input = get_input()

    try:
        result = parser.parse(input)
        maintype = resolve(result)
    except TPError as e:
        print(e.msg, file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        raise e
        sys.exit(1)
    else:
        write_output(maintype)


def resolve(result):
    """Chequea y resuelve las dependencias internas en result"""
    deps = {}
    maintype = result[0]

    for typedef in result:
        deps[typedef.name] = list(typedef.get_deps().keys())

    maybeloop = get_loop(deps, maintype.name, {})
    if maybeloop is not None:
        raise TPError(
            "Error semántico, se encontró una referencia circular en la definición de '%s', mediante el tipo '%s'"
            % maybeloop
        )

    resolve_dict = {}

    for typedef in result[1:]:
        resolve_dict[typedef.name] = typedef.type

    maintype.resolve(resolve_dict)

    return maintype


def get_loop(graph, start, visited):
    """Verifica si graph tiene loops, empezando por start y habiendo visitado visited"""
    visited[start] = True

    if start not in graph:
        raise TPError("Error: el tipo '%s' no esta definido." % start)

    for next in graph[start]:
        if next in visited and visited[next]:
            return (start, next)

        maybeloop = get_loop(graph, next, visited)
        if maybeloop is not None:
            return maybeloop

    return None


def get_input():
    """Obtiene el texto de entrada (stdin / 1er arg.)"""
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as input:
            return input.read()
    else:
        return sys.stdin.read()


def write_output(maintype):
    """Escribe a la salida (stdout / 2do arg) un json generado del tipo"""
    json = maintype.generate_json()

    if len(sys.argv) > 2:
        with open(sys.argv[2], "w") as output:
            # limpiar el archivo
            output.write(json)
    else:
        sys.stdout.write(json)


if __name__ == "__main__":
    main()
