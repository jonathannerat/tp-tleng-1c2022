#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import ply.yacc as yacc

from lexer import tokens


def p_start_decl(p):
    "start : decl decllist"
    p[0] = [p[1]] + p[2]


def p_decl(p):
    "decl : TYPE ID type"
    p[0] = {
        "name": p[2],
        "type": p[3],
    }


def p_decllist_decl(p):
    "decllist : decl decllist"
    p[0] = [p[1]] + p[2]


def p_decllist_empty(p):
    "decllist : empty"
    p[0] = []


def p_type_array(p):
    "type : ARRAY type"
    p[0] = {"kind": "array", "of": p[2]}


def p_type_struct(p):
    "type : STRUCT '{' prop proplist '}'"
    props = [p[3]] + p[4]
    p[0] = {"kind": "struct", "props": props}


def p_type_id(p):
    "type : ID"
    p[0] = p[1]


def p_prop(p):
    "prop : ID type"
    p[0] = {"name": p[1], "type": p[2]}


def p_proplist_prop(p):
    "proplist : prop proplist"
    p[0] = [p[1]] + p[2]


def p_proplist_empty(p):
    "proplist : empty"
    p[0] = []


def p_empty(_):
    "empty :"
    pass


def p_error(p):
    print("Syntax error on input: %s" % p)


parser = yacc.yacc()

data = """
type persona struct {
    nombre  string
    edad    int
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

result = parser.parse(data)
print(result)
