#!/usr/bin/env python3
# -*- coding=utf-8 -*-

from sys import stdin
import ply.yacc as yacc

from mylexer import tokens, find_column
from myast import BasicTypeNode, TypedefNode, ArrayTypeNode, StructTypeNode, basic_types
from myerror import TPError


def p_decllist(p):
    """decllist : decl
    | decl decllist"""
    p[0] = [p[1]]
    if len(p) > 2:
        p[0].extend(p[2])


def p_decl(p):
    "decl : TYPE ID type"
    p[0] = TypedefNode(p[2], p[3])


def p_type(p):
    """type : ID
    | ARRAY type
    | STRUCT '{' proplist '}'"""
    if len(p) == 2:
        type_name = p[1]
        p[0] = BasicTypeNode(type_name) if type_name in basic_types else type_name
    elif len(p) == 3:
        p[0] = ArrayTypeNode(p[2])
    elif len(p) == 5:
        p[0] = StructTypeNode(p[3])


def p_prop(p):
    "prop : ID type"
    p[0] = (p[1], p[2])


def p_proplist(p):
    """proplist : prop
    | prop proplist"""
    p[0] = [p[1]]
    if len(p) > 2:
        p[0].extend(p[2])


def p_error(p):
    raise TPError(
        "Error: token inválido '%s' en la linea %s, columna %s"
        % (p.value, p.lineno, find_column(p))
    )


parser = yacc.yacc()
