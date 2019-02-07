from src.Token import Token, RESERVED_KEYWORDS

'''Lexer.py'''
'''Lexical analyzer (also known as scanner or tokenizer)'''

class Lexer(object):
    '''Lexer'''
    WHITESPACE      = ' \t\r\n'
    TAB             = '\t'
    NEWLINE         = '\n'
    EOF_MARKER      = '$'

    def __init__(self, text):
        self.text = text            # client string input, e.g. "3 + 5", "12 - 5", etc
        self.pos = 0                # self.pos is an index into self.text
        self.current_token = None   # current token instance
        self.current_char = self.text[self.pos] #init with 1st char

        self.line_no = 1
        self.line_pos = 1
        self.tokens = []            # list of tokens

    def error(self, msg):
        raise ValueError(f'Lexer Error parsing input : {msg}')

    def advance(self):
        """Advance the 'pos' pointer and set the 'current_char' variable."""
        self.pos += 1
        self.line_pos += 1

        if self.pos > len(self.text) - 1:
            self.current_char = None  # Indicates end of input
        else:
            self.current_char = self.text[self.pos]

    def peek(self):
        peek_pos = self.pos + 1

        if peek_pos > len(self.text) - 1:
            return None
        else:
            return self.text[peek_pos]

    def skip_whitespace(self):
        ''' [ \t\n]* '''

        # while self.current_char is not None and self.current_char.isspace():
        #     self.advance()
        while self.current_char is not None and self.current_char in Lexer.WHITESPACE:
            if self.current_char in Lexer.NEWLINE:
                self.line_no += 1
                self.line_pos = 1
            elif self.current_char in Lexer.TAB:
                self.line_pos += 3
            self.advance()                

    def skip_comment(self):
        '''Pascal comment '''
        while self.current_char != '}':
            self.advance()
        self.advance()  # the closing curly brace

    # def integer(self):
    #     """Return a (multidigit) integer consumed from the input."""
    #     result = ''
    #     while self.current_char is not None and self.current_char.isdigit():
    #         result += self.current_char
    #         self.advance()
    #     token = Token(Token.INTEGER, result, self.line_no, self.line_pos)
    #     self.tokens.append(token)             
    #     return int(result)

    def _id(self):
        """Handle identifiers and reserved keywords"""
        result = ''
        while self.current_char is not None and self.current_char.isalnum():
            result += self.current_char
            self.advance()
        
        token = RESERVED_KEYWORDS.get(result.upper(), None)
        if token is None:
            token = Token(Token.ID, result, self.line_no, self.line_pos))
        self.tokens.append(token)             
        return token

    def number(self):
        """Return a (multidigit) integer or float consumed from the input."""
        result = int(self.current_char) - 0
        while self.current_char is not None and self.current_char.isdigit():
            result = result * 10 + int(self.current_char) - 0
            #result += self.current_char
            self.advance()

        if self.current_char == '.':
            result += self.current_char
            self.advance()

            while (self.current_char is not None and self.current_char.isdigit()):
                #result += self.current_char
                result = result * 10 + int(self.current_char) - 0
                self.advance()

            token = Token('REAL_CONST', float(result))
            token = Token(Token.REAL_CONST, result, self.line_no, self.line_pos)
        else:
            token = Token('INTEGER_CONST', int(result))
            token = Token(Token.INTEGER_CONST, result, self.line_no, self.line_pos)
        
        self.tokens.append(token)             
        return token

    def get_next_token(self):
        """
        This method is responsible for breaking a sentence
        apart into tokens. One token at a time.
        """
        while self.current_char is not None:
            # space
            if self.current_char in Lexer.WHITESPACE: #.isspace():
                self.skip_whitespace()
                continue

            # Pascal Comment
            if self.current_char == '{':
                self.advance()
                self.skip_comment()
                continue           

            # alpha
            if self.current_char.isalpha():
                return self._id()

            # digit
            if self.current_char.isdigit():
                return self.number()
                
            # Pascal assign op
            if self.current_char == ':' and self.peek() == '=':
                self.advance()
                self.advance()
                token = Token(Token.ASSIGN, ':=', self.line_no, self.line_pos)
                self.tokens.append(token)             
                return Token(Token.ASSIGN, ':=')

            # Semi
            if self.current_char == ';':
                self.advance()
                token = Token(Token.SEMI, ';', self.line_no, self.line_pos)
                self.tokens.append(token)             
                return Token(Token.SEMI, ';')

            # colon
            if self.current_char == ':':
                self.advance()
                return Token(Token.COLON, ':')

            # Comma
            if self.current_char == ',':
                self.advance()
                return Token(Token.COMMA, ',')
         
            # Plus
            if self.current_char == '+':
                self.advance()
                return Token(Token.PLUS, '+')

            # Minus
            if self.current_char == '-':
                self.advance()
                return Token(Token.MINUS, '-')

            if self.current_char == '*':
                self.advance()
                return Token(Token.MUL, '*')

            if self.current_char == '/':
                self.advance()
                return Token(Token.FLOAT_DIV, '/')

            if self.current_char == '(':
                self.advance()
                return Token(Token.LPAREN, '(')

            if self.current_char == ')':
                self.advance()
                return Token(Token.RPAREN, ')')          

            if self.current_char == '.':
                self.advance()
                return Token(Token.DOT, '.')                  

            self.error(f'get_next_token - unknown char : {self.current_char}')

        return Token(Token.EOF, None)


def runmain():
    from src.Interpreter import Interpreter
    while True:
        try:
            text = input('calc> ')
        except EOFError:
            break
        if not text:
            continue
        interpret = Interpreter(text)
        result = interpret.interpret()
        print(result)

if __name__ == '__main__':
    runmain()