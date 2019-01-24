from src.token import Token, RESERVED_KEYWORDS
from src.lexer import Lexer
from src.parser import Parser

class NodeVisitor(object):
    
    def visit(self, node):
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception('No visit_{} method'.format(type(node).__name__))

class Interpreter(NodeVisitor):

    GLOBAL_SCOPE = {}

    def __init__(self, parser):
        self.parser = parser

    def visit_BinOp(self, node):
        if node.op.type == Token.PLUS:
            return self.visit(node.left) + self.visit(node.right)
        elif node.op.type == Token.MINUS:
            return self.visit(node.left) - self.visit(node.right)
        elif node.op.type == Token.MUL:
            return self.visit(node.left) * self.visit(node.right)
        elif node.op.type == Token.DIV:
            return self.visit(node.left) / self.visit(node.right)


    def visit_Num(self, node):
        return node.value


    def visit_UnaryOp(self, node):
        op = node.op.type
        if op == Token.PLUS:
            return +self.visit(node.expr)
        elif op == Token.MINUS:
            return -self.visit(node.expr)


    def visit_Compound(self, node):
        for child in node.children:
            self.visit(child)

    def visit_Assign(self, node):
        var_name = node.left.value
        self.GLOBAL_SCOPE[var_name] = self.visit(node.right)

    def visit_Var(self, node):
        var_name = node.value
        val = self.GLOBAL_SCOPE.get(var_name)
        if val is None:
            raise NameError(repr(var_name))
        else:
            return val

    def visit_NoOp(self, node):
        pass


    def interpret(self):
        tree = self.parser.parse()
        if tree is None:
            return ''
        return self.visit(tree)


def main():
    text = open('src/test/pascal.txt', 'r').read()

    #import sys
    #while True:
    #try:
        #text = input('spi> ')
        #text = open(sys.argv[1], 'r').read()
    # except EOFError:
    #     break
    # if not text:
    #     continue    

    lexer = Lexer(text)
    parser = Parser(lexer)
    interpreter = Interpreter(parser)
    result = interpreter.interpret()
    print(interpreter.GLOBAL_SCOPE)          

if __name__ == '__main__':
    main()


'''
$ python spi.py
spi> - 3
-3
spi> + 3
3
spi> 5 - - - + - 3
8
spi> 5 - - - + - (3 + 4) - +2
10
'''    