from src.Token import Token

class AST:
    #Token token # node is derived from which token?
    
    #List<AST> children # operands
    
    def __init__(self, token):
        self.token = token
        self.children = []

    def add_child(self, ast):
        if self.children is None:
            self.children = []
        self.children.append(ast)
