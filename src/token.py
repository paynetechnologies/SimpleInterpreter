'''Token.py'''
''' Token Class '''
class Token():
    ''' 
    Token 
    '''
    # Token types
    (
        ASSIGN, BEGIN, COLON, COMMA, DIV, DOT, END, EOF, FLOAT_DIV, 
        FUNCTION, ID, INTEGER, INTEGER_CONST, INTEGER_DIV, LONGINT, LPAREN, 
        MINUS, MUL, PLUS, PROCEDURE, PROGRAM,  REAL, REAL_CONST, RPAREN, SEMI, VAR
    ) = ( 
        'ASSIGN', 'BEGIN', 'COLON', 'COMMA', 'DIV', 'DOT', 'END', 'EOF', 'FLOATS_DIV', \
        'FUNCTION', 'ID', 'INTEGER', 'INTEGER_CONST', 'INTEGER_DIV', 'LONGINT', 'LPAREN', \
        'MINUS', 'MUL', 'PLUS', 'PROCEDURE', 'PROGRAM', 'REAL', 'REAL_CONST', 'RPAREN', 'SEMI', 'VAR'
    ) 


    # def __init__(self, type, value):
    #     self.type = type
    #     self.value = value         # token value: 0, 1, 2. 3...'+', '-', '*', '/', ID, None

    # def __str__(self):
    #     """String representation of the class instance.

    #     Examples:
    #         Token(INTEGER, 3)
    #         Token(PLUS '+')
    #         Token(MULTIPLY '*')
    #     """
    #     return 'Token({type}, {value})'.format(
    #         type=self.type,
    #         value=repr(self.value)
    #     )

    def __repr__(self):
        return self.__str__()

    def __init__(self, type, value, line_no=0, line_pos=0):        
        self.type = type
        self.value = value
        #self.line = line
        self.line_no = line_no
        self.line_pos = line_pos # - len(value)
        
    def __str__(self):
        return '{0}:{1}'.format(self.line_no, self.line_pos).ljust(10) + self.type.ljust(15) + self.value        



# RESERVED_KEYWORDS = {
#     'BEGIN': Token(Token.BEGIN, Token.BEGIN),
#     'END': Token(Token.END, Token.END),
#     }

RESERVED_KEYWORDS = {
    'PROGRAM': Token('PROGRAM', 'PROGRAM'),
    'VAR': Token('VAR', 'VAR'),
    'DIV': Token('INTEGER_DIV', 'DIV'),
    'FUNCTION': Token('FUNCTION', 'FUNCTION'),
    'INTEGER': Token('INTEGER', 'INTEGER'),
    'LONGINT': Token('LONGINT', 'LONGINT'),
    'REAL': Token('REAL', 'REAL'),
    'BEGIN': Token('BEGIN', 'BEGIN'),
    'END': Token('END', 'END'),
    'PROCEDURE' : Token('PROCEDURE', 'PROCEDURE')
}

if __name__ == '__main__':
    #t = Token(Token.INTEGER, Token.INTEGER)
    print(Token(Token.INTEGER, Token.INTEGER))


    # keywords ::= while | return | if | elif | 
    # operators ::= +, -, *, /, **
    # relations ::= >, >=, <, <=, =, <>     
    # identifiers ::= [A..Za..z]+[0..9_]*
    # constants ::= pi | 
    # numbers ::= [0..9]+
    # punctuation ::= ; 
    # EOF (end-of-file) token is used to indicate that there is no more input left for lexical analysis
    
    # Symbol Table ::= Tokens 
    # Tokens ::= Token_Types Attributes
    # Token_Types ::= Keywords, operaors, relations, identifiers, constants, numbers, punctuation
    # Attributes ::= [Lexeme | Number] Line_Number [ptr to symbol table]
    # Line_Number ::= size of input / \n
    # Lexeme ::= ID | NUM
    # ID ::= [A..Za..z]+[0..9_]*
    # NUM ::= [0..9]+    
