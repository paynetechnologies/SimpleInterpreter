'''Ast.py '''
from Token import Token

class AST(object):
        
    def __str__(self):
        return ('AST {cn}'.format(cn=self.__class__.__name__))

        # return '<{class_name}(name={name}, parameters={params})>'.format(
        #     class_name=self.__class__.__name__,
        #     name=self.name,
        #     params=self.params,
        # )        


    def __repr__(self):
        return self.__str__()


class Assign(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right

class BinOp(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right

class Block(AST):
    def __init__(self, declarations, compound_statement):
        self.declarations = declarations
        self.compound_statement = compound_statement
        
class Compound(AST):
    """Represents a 'BEGIN ... END' block"""
    def __init__(self):
        self.children = []
   
class FunctionDecl(AST):
    def __init__(self, func_name, params, return_type, block_node):
    #def __init__(self, func_name, params, block_node):        
        self.func_name = func_name
        self.params = params  # a list of Param nodes
        self.return_type = return_type
        self.block_node = block_node
        
class NoOp(AST):
    pass        
    
class Num(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value

class Param(AST):
    def __init__(self, var_node, type_node):
        self.var_node = var_node
        self.type_node = type_node

class ProcedureDecl(AST):
    def __init__(self, proc_name, params, block_node):
        self.proc_name = proc_name
        self.params = params  # a list of Param nodes
        self.block_node = block_node

class Program(AST):
    def __init__(self, name, block):
        self.name = name
        self.block = block
        
class Type(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value

class UnaryOp(AST):
    def __init__(self, op, expr):
        self.token = self.op = op
        self.expr = expr

class Var(AST):
    """The Var node is constructed out of ID token."""
    def __init__(self, token):
        self.token = token
        self.value = token.value

class VarDecl(AST):
    def __init__(self, var_node, type_node):
        self.var_node = var_node
        self.type_node = type_node
