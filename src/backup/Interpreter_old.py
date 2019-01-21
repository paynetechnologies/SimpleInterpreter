'''parser'''
from src.token import Token

class Interpreter(object):
    '''Parser'''

    def __init__(self, text):
        self.text = text            # client string input, e.g. "3 + 5", "12 - 5", etc
        self.pos = 0                # self.pos is an index into self.text
        self.current_token = None   # current token instance
        self.current_char = self.text[self.pos]


    # LEX ***********************

    def error(self, msg):
        raise Exception('Error parsing input : ' + msg)


    def advance(self):
        """Advance the 'pos' pointer and set the 'current_char' variable."""
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None  # Indicates end of input
        else:
            self.current_char = self.text[self.pos]


    def skip_whitespace(self):
        ''' [ \t\n]* '''
        while self.current_char is not None and self.current_char.isspace():
            self.advance()


    def integer(self):
        """Return a (multidigit) integer consumed from the input."""
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)


    def get_next_token(self):
        """
        Lexical analyzer (also known as scanner or tokenizer)
        This method is responsible for breaking a sentence
        apart into tokens.
        """
        while self.current_char is not None:

            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                return Token(Token.INTEGER, self.integer())

            if self.current_char == '+':
                self.advance()
                return Token(Token.PLUS, '+')

            if self.current_char == '-':
                self.advance()
                return Token(Token.MINUS, '-')

            if self.current_char == '*':
                self.advance()
                return Token(Token.MULTIPLY, '*')

            if self.current_char == '/':
                self.advance()
                return Token(Token.DIVIDE, '/')

            self.error('get_next_token - unknown char')

        return Token(Token.EOF, None)


    def match(self, token_type):
        ''' 
        compare the current token type with the passed token type and
        if they match then "eat" the current token and assign the next
        token to the self.current_token, otherwise raise an exception.
        '''
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error('Unknown toke type : ' + token_type)

    
    def expr(self):
        """
        Parser / Interpreter
        EXPR -> [TERM OP TERM]*
        TERM -> [INTEGER]+
        INTEGER -> [0..9] 
        OP -> PLUS | MINUS | MULTIPLY | DIVIDE

        # 5
        expr -> factor ( (MUL | DIV) factor)*
        (MUL | DIV) -> * | /

        # 6
        EXPR -> TERM (ADDOP TERM)*
        TERM -> FACTOR ((MULOP) FACTOR)*
        FACTOR -> [INTEGER]+
        INTEGER -> [0..9]
        MULOP -> * | /
        ADDOP -> + | -  

        """
        # set current token to the first token taken from the input
        # not in #6 - self.current_token = self.get_next_token() 

        result = self.term()

        while self.current_token.type in (Token.PLUS, Token.MINUS):
            token = self.current_token
            if (token.type == Token.PLUS):
                self.match(Token.PLUS)
                result = result + self.term()
            elif (token.type == Token.MINUS):
                self.match(Token.MINUS)
                result = result - self.term()
        
        return result

    # def term(self):
    #     ''' A TERM is + | - '''
    #     token = self.current_token
    #     self.match(Token.INTEGER)
    #     return token.value

    
    def term(self ):
        ''' 
        #6
        TERM -> FACTOR ((MULOP) FACTOR)*
        
        TERM -> + | - 
        '''

        token = self.current_token

        self.factor()
        while (True):

            if (self.current_token.type in ['*','/','DIV','MOD']):
                t = self.get_next_token()
                self.match(t)
                self.factor()

            return token.value


    def factor(self):
        ''' 
        #6
        FACTOR -> INTEGER

        Factor -> ( expr ) | NUM | ID 

        '''

        if (self.current_token.type == Token.LPAREN == "("):
            self.match("(") 
            self.expr()
            self.match(")")
            #return token.value

        elif (self.current_token.type == Token.NUM):
            #emit(Token.NUM, Token.token_value) ; 
            self.match(Token.NUM)
            #return token.value

        elif (self.current_token.type == Token.ID):
            #emit(Token.ID, Token.token_value); 
            self.match(Token.ID)
            #return token.value
        else:
            self.error("factor syntax error")



    # def expr(self):
    
    #     self.term()
        
    #     while(True):

    #         if (parser.lookahead == '+' or parser.lookahead == '-'):
    #             t = parser.lookahead
    #             self.match(t); 
    #             self.term(); 
    #             emit(t, Token.NONE)

    #         else:
    #             return
    
        '''
        # we expect the current token to be an integer
        left = self.current_token
        self.match(Token.INTEGER)
        
        # we expect the current token to be either a '+' or '-'
        op = self.current_token

        if op.type == Token.PLUS:
            self.match(Token.PLUS)
        elif op.type == Token.MINUS:
            self.match(Token.MINUS)
        elif op.type == Token.MULTIPLY:
            self.match(Token.MULTIPLY)
        elif op.type == Token.DIVIDE:
            self.match(Token.DIVIDE)

        # we expect the current token to be an integer
        right = self.current_token
        self.match(Token.INTEGER)
        # after the above call the self.current_token is set to EOF token

        # at this point either the INTEGER PLUS INTEGER or the INTEGER MINUS 
        # INTEGER sequence of tokens has been successfully found and the method 
        # can just return the result of adding or subtracting two integers, thus 
        # effectively interpreting client input
        if op.type == Token.PLUS:
            result = left.value + right.value
        elif op.type == Token.MINUS:   
            result = left.value - right.value
        elif op.type == Token.MULTIPLY:   
            result = left.value * right.value
        elif op.type == Token.DIVIDE:   
            result = left.value / right.value
        return result
        '''


def runmain():
    while True:
        try:
            text = input('calc> ')
        except EOFError:
            break
        if not text:
            continue
        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)


if __name__ == '__main__':
    runmain()