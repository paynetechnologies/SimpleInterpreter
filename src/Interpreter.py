import collections
from src.Token import Token
from src.Lexer import Lexer
from src.Parser import Parser
from src.NodeVisitor import NodeVisitor
from src.SymbolTable import Symbol, SymbolTable, SymbolTableBuilder, BuiltinTypeSymbol, VarSymbol


d = False        
def dprint(msg):
    if d:
        print(msg)

class Interpreter(NodeVisitor):
    def __init__(self, tree):
        self.tree = tree
        self.GLOBAL_MEMORY = collections.OrderedDict()

    def visit_Program(self, node):
        dprint(f'visit_Program : {node}')
        self.visit(node.block)

    def visit_ProcedureDecl(self, node):
        pass #self.visit(node.block_node)

    def visit_Block(self, node):
        dprint(f'visit_Block : {node}')
        for declaration in node.declarations:
            self.visit(declaration)
        self.visit(node.compound_statement)

    def visit_VarDecl(self, node):
        dprint(f'visit_VarDecl : {node}')
        # Do nothing
        pass

    def visit_Type(self, node):
        dprint(f'visit_Type : {node}')
        # Do nothing
        pass

    def visit_BinOp(self, node):
        dprint(f'visit_BinOp : {node}')
        if node.op.type == Token.PLUS:
            return self.visit(node.left) + self.visit(node.right)
        elif node.op.type == Token.MINUS:
            return self.visit(node.left) - self.visit(node.right)
        elif node.op.type == Token.MUL:
            return self.visit(node.left) * self.visit(node.right)
        elif node.op.type == Token.INTEGER_DIV:
            return self.visit(node.left) // self.visit(node.right)
        elif node.op.type == Token.FLOAT_DIV:
            return float(self.visit(node.left)) / float(self.visit(node.right))

    def visit_Num(self, node):
        dprint(f'visit_Num : {node}')
        return node.value

    def visit_UnaryOp(self, node):
        dprint(f'visit_UnaryOp : {node}')
        op = node.op.type
        if op == Token.PLUS:
            return +self.visit(node.expr)
        elif op == Token.MINUS:
            return -self.visit(node.expr)

    def visit_Compound(self, node):
        dprint(f'visit_Compound : {node}')
        for child in node.children:
            self.visit(child)

    def visit_Assign(self, node):
        dprint(f'visit_Assign : {node}')
        var_name = node.left.value
        self.GLOBAL_MEMORY[var_name] = self.visit(node.right)

    def visit_Var(self, node):
        dprint(f'visit_Var : {node}')
        var_name = node.value
        var_val = self.GLOBAL_MEMORY.get(var_name)
        if var_val is None:
            raise NameError(repr(var_name))
        else:
            return var_val

    def visit_NoOp(self, node):
        dprint(f'visit_Nop : {node}')
        pass

    def interpret(self):
        tree = self.tree
        if tree is None:
            return ''
        return self.visit(tree)


def main():
    text = open('src/test/pascal_13.pas', 'r').read()

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
    tree = parser.parse()

    symtab_builder = SymbolTableBuilder()
    symtab_builder.visit(tree)
    print('')
    print('Symbol Table contents:')
    print(symtab_builder.symtab)

    interpreter = Interpreter(tree)
    result = interpreter.interpret()

    print('')
    print('Run-time GLOBAL_MEMORY contents:')
    for k, v in sorted(interpreter.GLOBAL_MEMORY.items()):
        print(f'{k} = {v}')
        #print('%s = %s' % (k, v))       

if __name__ == '__main__':
    main()
