import ply.lex as lex

literals = "{}"

reserved = {
    "type": "TYPE",
    "struct": "STRUCT",
}

tokens = ["ARRAY", "ID"] + list(reserved.values())

t_ARRAY = r"\[\]"
t_ignore = " \t"


def t_ID(t):
    r"[a-z]\w*"
    t.type = reserved.get(t.value, "ID")
    return t


def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)


def t_error(t):
    raise Exception("Caracter ilegal: {0}. En linea: {1}".format(t.value[0], t.lineno))


lexer = lex.lex()

ejemplo = """
type persona struct {
    nombre string
    edad int
    nacionalidad pais
    ventas []float64
    activo bool
}

type pais struct {
    nombre string
    codigo struct {
        prefijo string
        sufijo string
    }
}
"""

lexer.input(ejemplo)
for tok in lexer:
    print(tok)
