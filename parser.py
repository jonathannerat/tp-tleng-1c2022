#!/usr/bin/env python3
# -*- coding=utf-8 -*-

from sys import stdin
import ply.yacc as yacc

from lexer import tokens

def random_count():
    return 3

# definicion de tipo
class PTypedef:
    def __init__(self, name, type):
        self.name = name
        self.type = type

# tipo array, tiene un subtipo
class PTypeArray:
    def __init__(self, type):
        self.type = type

    def random_value(self, type_resolver):
        return [
			type_resolver(self.type).random_value(type_resolver) for _ in range(1, random_count())
		]

# tipo array, tiene una lista de pares (nombre, tipo)
class PTypeStruct:
    def __init__(self, props):
        self.props = props

    def random_value(self, type_resolver):
        random_dict = {}
        for (name, type) in self.props:
            random_dict[name] = type_resolver(type).random_value(type_resolver)

        return random_dict

class PTypeBool:
    def random_value(self, _):
        return True

class PTypeFloat:
    def random_value(self, _):
        return 4.3

class PTypeInt:
    def random_value(self, _):
        return 17

class PTypeString:
    def random_value(self, _):
        return "random"


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
