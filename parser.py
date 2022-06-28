#!/usr/bin/env python3
# -*- coding=utf-8 -*-

from sys import stdin
import ply.yacc as yacc

from lexer import tokens


# definicion de tipo
class PTypedef:
    def __init__(self, name, type):
        self.name = name
        self.type = type

        if isinstance(type, PTypeStruct):
            type.set_level(0)

    def __str__(self):
        return "%s => %s\n" % (self.name, self.type)


# tipo array, tiene un subtipo
class PTypeArray:
    def __init__(self, type):
        self.type = type

    def __str__(self):
        return "[]" + self.type


# tipo array, tiene una lista de pares (nombre, tipo)
class PTypeStruct:
    level = 0

    def __init__(self, props):
        self.props = props

    def set_level(self, level):
        self.level = level
        for prop in self.props:
            if isinstance(prop[1], PTypeStruct):
                prop[1].set_level(level + 1)

    def __str__(self):
        indent = "\t" * self.level
        str = "{\n"
        for prop in self.props:
            str += indent + "\t%s %s\n" % prop

        return str + indent + "}"


def p_start_decl(p):
    "decllist : decl decllist"
    p[0] = [p[1]] + p[2]


def p_decllist_decl(p):
    "decllist : decl"
    p[0] = [p[1]]


def p_decl(p):
    "decl : TYPE ID type"
    p[0] = PTypedef(p[2], p[3])


def p_type_array(p):
    "type : ARRAY type"
    p[0] = PTypeArray(p[2])


def p_type_struct(p):
    "type : STRUCT '{' proplist '}'"
    p[0] = PTypeStruct(p[3])


def p_type_id(p):
    "type : ID"
    p[0] = p[1]


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
