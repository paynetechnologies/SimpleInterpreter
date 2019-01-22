'''Lexer'''
from src.token import Token
#from src.Interpreter import Interpreter

class Lexer(object):
    '''Lexer'''

    def __init__(self, text):
        self.text = text            # client string input, e.g. "3 + 5", "12 - 5", etc
        self.pos = 0                # self.pos is an index into self.text
        self.current_token = None   # current token instance
        self.current_char = self.text[self.pos]

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
                return Token(Token.MUL, '*')

            if self.current_char == '/':
                self.advance()
                return Token(Token.DIV, '/')

            if self.current_char == '(':
                self.advance()
                return Token(Token.LPAREN, '(')

            if self.current_char == ')':
                self.advance()
                return Token(Token.RPAREN, ')')                

            self.error('get_next_token - unknown char')

        return Token(Token.EOF, None)


def runmain():
    while True:
        try:
            text = input('calc> ')
        except EOFError:
            break
        if not text:
            continue
        interpreter = Interpreter(text)
        result = interpreter.interpret()
        print(result)


if __name__ == '__main__':
    runmain()
