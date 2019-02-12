'''Lexical analyzer (also known as scanner or tokenizer)'''
from src.Token import Token, RESERVED_KEYWORDS



class Lexer(object):
    '''Lexer'''
    WHITESPACE      = ' \t\r\n'
    TAB             = '\t'
    NEWLINE         = '\n'
    EOF_MARKER      = '$'

    def __init__(self, text):
        self.text = text            # client string input, e.g. "3 + 5", "12 - 5", etc
        self.current_token = None   # current token instance

        self.line_no = 1
        self.line_pos = 1
        self.pos = 0                # self.pos is an index into self.text        
        self.current_char = self.text[self.pos] #init with 1st char

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

    def number(self):
        """Return a (multidigit) integer or float consumed from the input."""
        result = 0# int(self.current_char) - 0
        while self.current_char is not None and self.current_char.isdigit():
            result = result * 10 + int(self.current_char) - 0
            self.advance()

        if self.current_char == '.':
            result += self.current_char
            self.advance()

            while (self.current_char is not None and self.current_char.isdigit()):
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
        apart into tokens. One character at a time.
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
                #return Token(Token.ASSIGN, ':=')
                return token

            # Semi
            if self.current_char == ';':
                self.advance()
                token = Token(Token.SEMI, ';', self.line_no, self.line_pos)
                self.tokens.append(token)             
                return token

            # colon
            if self.current_char == ':':
                self.advance()
                token = Token(Token.COLON, ':', self.line_no, self.line_pos)
                self.tokens.append(token)          
                #return Token(Token.COLON, ':')
                return token

            # Comma
            if self.current_char == ',':
                self.advance()
                token = Token(Token.COMMA, ',', self.line_no, self.line_pos)
                self.tokens.append(token)
                return token
         
            # Plus
            if self.current_char == '+':
                self.advance()
                token = Token(Token.PLUS, '+', self.line_no, self.line_pos)
                self.tokens.append(token)
                return token

            # Minus
            if self.current_char == '-':
                self.advance()
                token = Token(Token.MINUS, '-', self.line_no, self.line_pos)
                self.tokens.append(token)
                return token

            if self.current_char == '*':
                self.advance()
                token = Token(Token.MUL, '*', self.line_no, self.line_pos)
                self.tokens.append(token)
                return token

            if self.current_char == '/':
                self.advance()
                token = Token(Token.FLOAT_DIV, '/', self.line_no, self.line_pos)
                self.tokens.append(token)
                return token

            if self.current_char == '(':
                self.advance()
                token = Token(Token.LPAREN, '(', self.line_no, self.line_pos)
                self.tokens.append(token)
                return token

            if self.current_char == ')':
                self.advance()
                token = Token(Token.RPAREN, ')', self.line_no, self.line_pos)
                self.tokens.append(token)                
                return token      

            if self.current_char == '.':
                self.advance()
                token = Token(Token.DOT, '.', self.line_no, self.line_pos)
                self.tokens.append(token)
                return token

            self.error(f'get_next_token - unknown char : {self.current_char}')

        token = Token(Token.EOF, 'EOF', self.line_no, self.line_pos)
        return token

    def skip_whitespace(self):
        ''' [ \t\n]* '''
        while self.current_char is not None and self.current_char in Lexer.WHITESPACE:
            if self.current_char in Lexer.NEWLINE:
                self.line_no += 1
                self.line_pos = 0
            elif self.current_char in Lexer.TAB:
                self.line_pos += 3
            self.advance()                


    def skip_comment(self):
        '''Pascal comment '''
        while self.current_char != '}':
            self.advance()
        self.advance()  # the closing curly brace


    def _id(self):
        """Handle identifiers and reserved keywords"""
        result = ''
        while self.current_char is not None and self.current_char.isalnum():
            result += self.current_char
            self.advance()
        
        reserved_token = RESERVED_KEYWORDS.get(result.upper(), None)
        if reserved_token:
            token = Token(reserved_token.type, result, self.line_no, self.line_pos)
        else:
            token = Token(Token.ID, result, self.line_no, self.line_pos)
        self.tokens.append(token)             
        return token


def runmain():
    from src.Semantic_Analyzer import SemanticAnalyzer
    from src.Parser import Parser

    while True:
        try:
            text = \
                """PROGRAM Test;
                   VAR
                       a : INTEGER;
                   BEGIN
                       a := 1
                   END.
                """            
            #input('calc> ')
        except EOFError:
            break
        if not text:
            continue

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

        break
if __name__ == '__main__':
    runmain()
