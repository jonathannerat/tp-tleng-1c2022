import ply.lex as lex

tokens = (
    'TYPE',
    'STRUCT',
    'LBRACKET',
    'RBRACKET',
    'ARRAY', 
    'FLOAT', 
    'BOOL', 
    'INT', 
    'STRING',
    'ID' 
)
def t_TYPE(t):
    r'type'
    return t 

def t_STRUCT(t):
    r'struct'
    return t

def t_LBRACKET(t):
    r'\{'
    return t

def t_RBRACKET(t):
    r'\}'
    return t

def t_ARRAY(t):
    r'\[\]'
    return t

def t_FLOAT(t):
    r'float64'
    return t 

def t_BOOL(t):
    r'bool'
    return t

def t_INT(t):
    r'int'
    return t

def t_STRING(t):
    r'string'
    return t

def t_ID(t):
    r'[a-z]\w*'
    return t 

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print("Caracter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

ejemplo = '''
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
'''

lexer.input(ejemplo)
for tok in lexer: 
    print(tok)