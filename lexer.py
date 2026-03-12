import ply.lex as lex # type: ignore

reserved = {
    'var': 'VAR',
    'let': 'LET',
    'const': 'CONST',
    'function': 'FUNCTION',
    'if': 'IF',
    'else': 'ELSE',
    'for': 'FOR',
    'while': 'WHILE',
    'return': 'RETURN',
    'true': 'TRUE',
    'false': 'FALSE'
}

tokens = [
    'IDENTIFIER', 'NUMBER', 'STRING',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'ASSIGN', 'SEMICOLON', 'COMMA',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE',
    'LBRACKET', 'RBRACKET',
    'GT', 'LT', 'GTE', 'LTE', 'EQEQ', 'NEQ'
] + list(reserved.values())

t_PLUS       = r'\+'
t_MINUS      = r'-'
t_TIMES      = r'\*'
t_DIVIDE     = r'/'
t_ASSIGN     = r'='
t_SEMICOLON  = r';'
t_COMMA      = r','
t_LPAREN     = r'\('
t_RPAREN     = r'\)'
t_LBRACE     = r'\{'
t_RBRACE     = r'\}'
t_LBRACKET   = r'\['
t_RBRACKET   = r'\]'
t_GT    = r'>'
t_LT    = r'<'
t_GTE   = r'>='
t_LTE   = r'<='
t_EQEQ  = r'=='
t_NEQ   = r'!='

def t_IDENTIFIER(t):
    r'[A-Za-z_][A-Za-z0-9_$]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'\"([^\\\n]|(\\.))*?\"'
    return t

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()