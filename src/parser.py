from src.ast import AST, BinOp, Num
from src.lexer import Lexer
from src.token import Token

class Parser(object):

    def __init__(self, lexer):
        self.lexer = lexer
        # set current token to the first token taken from the input
        self.current_token = self.lexer.get_next_token()

    def error(self, msg):
        raise Exception(f'Invalid syntax : {msg}')    

    def match(self, token_type):
        ''' 
        compare the current token type with the passed token type and
        if they match then "eat" the current token and assign the next
        token to the self.current_token, otherwise raise an exception.
        '''
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error('Unknown token type : ' + token_type)

    

    def factor(self):
        ''' 
        #7
        FACTOR -> INTEGER | LPAREN EXPR RPAREN 
        '''
        token = self.current_token

        if token.type == Token.INTEGER:
            self.match(Token.INTEGER)
            return Num(token)
        elif token.type == Token.LPAREN:
            self.match(Token.LPAREN)
            node = self.expr()
            self.match(Token.RPAREN)
            return node
    
    def term(self ):
        ''' 
        #7
        TERM -> FACTOR ((MULOP) FACTOR)*
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


    def expr(self):
        """
        # 7
        EXPR -> TERM (ADDOP TERM)*
        TERM -> FACTOR ((MULOP) FACTOR)*
        FACTOR -> [INTEGER] | LPAREN EXPR RPAREN
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

    def parse(self):
        return self.expr()