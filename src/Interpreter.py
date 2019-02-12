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
