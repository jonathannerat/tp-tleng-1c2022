from random import random, randrange
from myerror import TPError


basic_types = ["string", "int", "bool", "float64"]


class Node:
    """Representación basica de un nodo del AST"""

    def generate_json(self):
        """Genera el elemento JSON correspondiente al nodo"""
        pass

    def get_deps(self):
        """Obtiene la lista de tipos no resueltos (dependencias) del nodo"""
        pass

    def resolve(self, _):
        """Resuelve las dependencias del nodo, utilizando el diccionario de parametro"""
        pass


# Definicion de un tipo
class TypedefNode(Node):
    """Nodo Typedef, asigna un nombre a un tipo"""

    def __init__(self, name, type):
        if name in basic_types:
            raise TPError(
                "Error: nombre de tipo inválido, '%s' representa un tipo básico." % name
            )
        self.name = name
        self.type = type

    def generate_json(self):
        return self.type.generate_json()

    def get_deps(self):
        if isinstance(self.type, str):
            return {self.type: True}
        else:
            return self.type.get_deps()

    def resolve(self, resolve_dict):
        if isinstance(self.type, str):
            self.type = resolve_dict[self.type]

        self.type.resolve(resolve_dict)


# tipo array, tiene un subtipo
class ArrayTypeNode(Node):
    """Nodo Array, declara un array de un tipo"""

    def __init__(self, type):
        self.type = type

    def generate_json(self):
        json_list = []

        for _ in range(randrange(0, 5, 1)):
            json_list.append(self.type.generate_json())

        return "[%s]" % ",".join(json_list)

    def get_deps(self):
        if isinstance(self.type, str):
            return {self.type: True}
        else:
            return self.type.get_deps()

    def resolve(self, resolve_dict):
        if isinstance(self.type, str):
            self.type = resolve_dict[self.type]

        self.type.resolve(resolve_dict)


# tipo array, tiene una lista de pares (nombre, tipo)
class StructTypeNode(Node):
    """Nodo Struct, declara un nodo con propiedades, cada una con un nombre y un tipo"""

    def __init__(self, props):
        self.props = props

    def generate_json(self):
        json_props = []

        for prop in self.props:
            json_props.append('"%s":%s' % (prop[0], prop[1].generate_json()))

        return "{%s}" % ",".join(json_props)

    def get_deps(self):
        deps = {}

        for prop in self.props:

            if isinstance(prop[1], str):
                deps[prop[1]] = True
            else:
                for k in prop[1].get_deps().keys():
                    deps[k] = True

        return deps

    def resolve(self, resolve_dict):
        for i, prop in enumerate(self.props):
            proptype = prop[1]

            if isinstance(proptype, str):
                proptype = resolve_dict[proptype]
                self.props[i] = (prop[0], proptype)

            proptype.resolve(resolve_dict)


def rand_string():
    chardic = "abcdefghijklmnñopqrstuvwxyz"
    chardiclen = len(chardic)
    res = ""

    for _ in range(randrange(0, 20)):
        res += chardic[randrange(0, chardiclen)]

    return '"' + res + '"'


class BasicTypeNode(Node):
    """Nodo Basico, declara un tipo basico (string/int/bool/float)"""

    def __init__(self, type):
        if type not in basic_types:
            raise Exception("type debe ser un tipo básico: " + ",".join(basic_types))

        self.type = type

    def generate_json(self):
        if self.type == "string":
            return rand_string()
        elif self.type == "int":
            return str(randrange(0, 1000))
        elif self.type == "float64":
            return str(round(random() * 1000, 2))
        elif self.type == "bool":
            return "false" if randrange(0, 2) == 0 else "true"

    def get_deps(self):
        return {}
