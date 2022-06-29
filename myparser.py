#!/usr/bin/env python3
# -*- coding=utf-8 -*-

from sys import stdin
import ply.yacc as yacc

from mylexer import tokens
from myast import BasicTypeNode, TypedefNode, ArrayTypeNode, StructTypeNode, basic_types


def p_start_decl(p):
    "decllist : decl decllist"
    p[0] = [p[1]] + p[2]


def p_decllist_decl(p):
    "decllist : decl"
    p[0] = [p[1]]


def p_decl(p):
    "decl : TYPE ID type"
    p[0] = TypedefNode(p[2], p[3])


def p_type_array(p):
    "type : ARRAY type"
    p[0] = ArrayTypeNode(p[2])


def p_type_struct(p):
    "type : STRUCT '{' proplist '}'"
    p[0] = StructTypeNode(p[3])


def p_type_id(p):
    "type : ID"
    type_name = p[1]
    p[0] = BasicTypeNode(type_name) if type_name in basic_types else type_name


def p_prop(p):
    "prop : ID type"
    p[0] = (p[1], p[2])


def p_proplist_prop(p):
    "proplist : prop proplist"
    p[0] = [p[1]] + p[2]


def p_proplist_empty(p):
    "proplist : prop"
    p[0] = [p[1]]


def p_error(p):
    print("Syntax error on input: %s" % p)


parser = yacc.yacc()
