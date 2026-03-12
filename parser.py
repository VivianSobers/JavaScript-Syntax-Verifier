import ply.yacc as yacc # type: ignore
from lexer import tokens

had_error = False

def p_program(p):
    '''program : statement_list'''
    pass

def p_statement_list(p):
    '''statement_list : statement_list statement
                      | statement'''
    pass

def p_statement(p):
    '''statement : var_decl
                 | array_decl
                 | func_def
                 | selection
                 | iteration
                 | return_stmt
                 | assignment
                 | empty'''
    pass

def p_var_decl(p):
    '''var_decl : VAR IDENTIFIER SEMICOLON
                | VAR IDENTIFIER ASSIGN expression SEMICOLON
                | LET IDENTIFIER SEMICOLON
                | LET IDENTIFIER ASSIGN expression SEMICOLON
                | CONST IDENTIFIER ASSIGN expression SEMICOLON'''
    pass


def p_array_decl(p):
    '''array_decl : VAR IDENTIFIER ASSIGN LBRACKET array_elements RBRACKET SEMICOLON'''
    pass

def p_array_elements(p):
    '''array_elements : array_elements COMMA expression
                      | expression
                      | empty'''
    pass

def p_func_def(p):
    '''func_def : FUNCTION IDENTIFIER LPAREN param_list RPAREN LBRACE statement_list RBRACE'''
    pass

def p_param_list(p):
    '''param_list : param_list COMMA IDENTIFIER
                  | IDENTIFIER
                  | empty'''
    pass

def p_selection(p):
    '''selection : IF LPAREN expression RPAREN statement
                 | IF LPAREN expression RPAREN LBRACE statement_list RBRACE
                 | IF LPAREN expression RPAREN statement ELSE statement
                 | IF LPAREN expression RPAREN LBRACE statement_list RBRACE ELSE LBRACE statement_list RBRACE
                 | IF LPAREN expression RPAREN LBRACE statement_list RBRACE ELSE selection'''
    pass


def p_iteration(p):
    '''iteration : FOR LPAREN var_decl expression SEMICOLON assignment RPAREN LBRACE statement_list RBRACE
                 | WHILE LPAREN expression RPAREN LBRACE statement_list RBRACE'''
    pass

def p_return_stmt(p):
    '''return_stmt : RETURN expression SEMICOLON'''
    pass

def p_assignment(p):
    '''assignment : IDENTIFIER ASSIGN expression SEMICOLON'''
    pass

def p_expression(p):
    '''expression : expression PLUS term
                  | expression MINUS term
                  | expression GT term
                  | expression LT term
                  | expression EQEQ term
                  | expression NEQ term
                  | term'''
    pass

def p_term(p):
    '''term : NUMBER
            | IDENTIFIER
            | STRING'''
    pass

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    global had_error
    had_error = True
    if p:
        print(f"Syntax error at '{p.value}' (line {p.lineno})")
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()