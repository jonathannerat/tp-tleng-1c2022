import ply.lex as lex
from myerror import TPError

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
    raise TPError("Error sintáctico: caractér ilegal '%s' en la linea %s, columna %s" % (t.value[0], t.lineno, t.lexpos + 1))


lexer = lex.lex()
