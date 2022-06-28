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
