'''Interpreter.py'''
import collections
from src.Token import Token
from src.Lexer import Lexer
from src.Parser import Parser
from src.NodeVisitor import NodeVisitor
from src.Semantic_Analyzer import SemanticAnalyzer


DBUG = True
def dprint(msg):
    if DBUG:
        print(f'Intepreter : {msg}')

# class Interpreter(NodeVisitor):
#     def __init__(self, tree):
#         self.tree = tree
#         self.GLOBAL_MEMORY = collections.OrderedDict()

#     def visit_Assign(self, node):
#         dprint(f'visit_Assign : {node}')
#         var_name = node.left.value
#         var_value = self.visit(node.right)
#         self.GLOBAL_MEMORY[var_name] = var_value

#     def visit_BinOp(self, node):
#         dprint(f'visit_BinOp : {node}')
#         if node.oerand.type == Token.PLUS:
#             return self.visit(node.left) + self.visit(node.right)
#         elif node.oerand.type == Token.MINUS:
#             return self.visit(node.left) - self.visit(node.right)
#         elif node.oerand.type == Token.MUL:
#             return self.visit(node.left) * self.visit(node.right)
#         elif node.oerand.type == Token.INTEGER_DIV:
#             return self.visit(node.left) // self.visit(node.right)
#         elif node.oerand.type == Token.FLOAT_DIV:
#             return float(self.visit(node.left)) / float(self.visit(node.right))

#     def visit_Block(self, node):
#         dprint(f'visit_Block : {node}')
#         for declaration in node.declarations:
#             self.visit(declaration)
#         self.visit(node.compound_statement)

#     def visit_Compound(self, node):
#         dprint(f'visit_Compound : {node}')
#         for child in node.children:
#             self.visit(child)

#     def visit_FunctionDecl(self, node):
#         pass

#     def visit_NoOp(self, node):
#         dprint(f'visit_Nop : {node}')
#         pass

#     def visit_Num(self, node):
#         dprint(f'visit_Num : {node}')
#         return node.value

#     def visit_ProcedureDecl(self, node):
#         pass

#     def visit_Program(self, node):
#         dprint(f'visit_Program : {node}')
#         self.visit(node.block)

#     def visit_Type(self, node):
#         dprint(f'visit_Type : {node}')
#         # Do nothing
#         pass

#     def visit_UnaryOp(self, node):
#         dprint(f'visit_UnaryOp : {node}')
#         op = node.op.type
#         if op == Token.PLUS:
#             return +self.visit(node.expr)
#         elif op == Token.MINUS:
#             return -self.visit(node.expr)

#     def visit_Var(self, node):
#         dprint(f'visit_Var : {node}')
#         var_name = node.value
#         var_val = self.GLOBAL_MEMORY.get(var_name)
#         if var_val is None:
#             raise NameError(repr(var_name))
#         else:
#             return var_val

#     def visit_VarDecl(self, node):
#         dprint(f'visit_VarDecl : {node}')
#         # Do nothing
#         pass

#     def interpret(self):
#         tree = self.tree
#         if tree is None:
#             return ''
#         return self.visit(tree)


def main():
    #text = open('src/test/pascal_13.pas', 'r').read()      # Error: Symbol(identifier) not found 'y'
    #text = open('src/test/pascal_01_13.pas', 'r').read()   # valid program
    #text = open('src/test/pascal_02_13.pas', 'r').read()   # Duplicate id x found
    #text = open('src/test/pascal_03_13.pas', 'r').read()   # Error: Symbol(identifier) not found 'z'
    #text = open('src/test/pascal_04_13.pas', 'r').read()    # Error: Duplicate identifier 'x' found
    #text = open('src/test/factorial.pas', 'r').read() # need to parse IF statements

    #text = open('src/test/pascal_01_14.pas', 'r').read()    
    #text = open('src/test/nested_scope_01_14.pas', 'r').read()    
    #text = open('src/test/nested_scope_02_14.pas', 'r').read()    
    #text = open('src/test/nested_scope_03_14.pas', 'r').read()    
    #text = open('src/test/test_14/nested_scope_04_14.pas', 'r').read()
    text = open('src/test/test_14/nested_function_01_14.pas', 'r').read()
    #text = open('src/test/test_14/barebones.pas', 'r').read()
    
    lexer = Lexer(text)
    parser = Parser(lexer)
    tree = parser.parse()

    semantic_analyzer = SemanticAnalyzer()

    try:
        semantic_analyzer.visit(tree)
    except SystemError as sys_error:
        print(sys_error)

    for token in lexer.tokens:
        print(token) 

if __name__ == '__main__':
    main()
