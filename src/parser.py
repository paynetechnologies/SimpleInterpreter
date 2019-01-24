from src.ast import AST, Assign, BinOp, Compound, NoOp, Num, UnaryOp, Var
from src.lexer import Lexer
from src.token import Token


class Parser(object):
    
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token() # set current token to first token from the input

    def error(self, msg):
        raise ValueError(f'Invalid syntax : {msg}')    

    def match(self, token_type):
        ''' 
        compare the current token type with the passed token type and
        if they match then "eat" the current token and assign the next
        token to the self.current_token, otherwise raise an exception.
        '''
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error(f'Unknown token type : {token_type}')

    def program(self):
        """program : compound_statement DOT"""
        node = self.compound_statement()
        self.match(Token.DOT)
        return node


    def compound_statement(self):
        """
        compound_statement: BEGIN statement_list END
        """
        self.match(Token.BEGIN)
        nodes = self.statement_list()
        self.match(Token.END)

        root = Compound()
        for node in nodes:
            root.children.append(node)

        return root        

    def statement_list(self):
        """
        statement_list : statement
                       | statement SEMI statement_list
        """
        node = self.statement()

        results = [node]

        while self.current_token.type == Token.SEMI:
            self.match(Token.SEMI)
            results.append(self.statement())

        if self.current_token.type == Token.ID:
            self.error('statement SEMI statement_list')

        return results

    def statement(self):
        """
        statement : compound_statement
                  | assignment_statement
                  | empty
        """
        if self.current_token.type == Token.BEGIN:
            node = self.compound_statement()
        elif self.current_token.type == Token.ID:
            node = self.assignment_statement()
        else:
            node = self.empty()
        return node

    def assignment_statement(self):
        """
        assignment_statement : variable ASSIGN expr
        """
        left = self.variable()
        token = self.current_token
        self.match(Token.ASSIGN)
        right = self.expr()
        node = Assign(left, token, right)
        return node

    def variable(self):
        """
        variable : ID
        """
        node = Var(self.current_token)
        self.match(Token.ID)
        return node

    def empty(self):
        """An empty production"""
        return NoOp()


    def expr(self):
        """
        #9
        expr : term ((PLUS | MINUS) term)*
        """
        # set current token to the first token taken from the input
        # not in #6 - self.current_token = self.get_next_token() 

        node = self.term()

        while self.current_token.type in (Token.PLUS, Token.MINUS):
            token = self.current_token
            if (token.type == Token.PLUS):
                self.match(Token.PLUS)
            elif (token.type == Token.MINUS):
                self.match(Token.MINUS)
       
            node = BinOp(left=node, op=token, right=self.term())

        return node

    
    def term(self ):
        ''' 
        #9
        term : factor ((MUL | DIV) factor)*
        '''

        node = self.factor()

        while self.current_token.type in (Token.MUL, Token.DIV):
            token = self.current_token
            if token.type == Token.MUL:
                self.match(Token.MUL)
            elif token.type == Token.DIV:
                self.match(Token.DIV)

            node = BinOp(left=node, op=token, right=self.factor())

        return node


    def factor(self):
        """factor : PLUS factor
                  | MINUS factor
                  | INTEGER
                  | LPAREN expr RPAREN
                  | variable
        """
        
        token = self.current_token

        if token.type == Token.PLUS:
            self.match(Token.PLUS)
            node = UnaryOp(token, self.factor())
            return node

        elif token.type == Token.MINUS:
            self.match(Token.MINUS)
            node = UnaryOp(token, self.factor())
            return node

        elif token.type == Token.INTEGER:
            self.match(Token.INTEGER)
            return Num(token)

        elif token.type == Token.LPAREN:
            self.match(Token.LPAREN)
            node = self.expr()
            self.match(Token.RPAREN)
            return node
        else:
            node = self.variable()
            return node


    def parse(self):
        """
        program : compound_statement DOT
        compound_statement : BEGIN statement_list END
        statement_list : statement
                       | statement SEMI statement_list
        statement : compound_statement
                  | assignment_statement
                  | empty
        assignment_statement : variable ASSIGN expr
        empty :
        expr: term ((PLUS | MINUS) term)*
        term: factor ((MUL | DIV) factor)*
        factor : PLUS factor
               | MINUS factor
               | INTEGER
               | LPAREN expr RPAREN
               | variable
        variable: ID
        """
        node = self.program()
        if self.current_token.type != Token.EOF:
            self.error('Missing EOF')

        return node
