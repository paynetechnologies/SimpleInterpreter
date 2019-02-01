'''Token.py'''
''' Token Class '''
class Token():
    ''' 
    Token 
    '''
    # Token types
    (
        ASSIGN, BEGIN, COLON, COMMA, DIV, DOT, END, FLOAT_DIV, 
        EOF, ID, INTEGER, INTEGER_CONST, INTEGER_DIV, LPAREN, 
        MINUS, MUL, PLUS, PROCEDURE, PROGRAM,  REAL, REAL_CONST, RPAREN, SEMI, VAR
    ) = ( 
        'ASSIGN', 'BEGIN', 'COLON', 'COMMA', 'DIV', 'DOT', 'END', 'FLOATS_DIV', \
        'EOF', 'ID', 'INTEGER', 'INTEGER_CONST', 'INTEGER_DIV', 'LPAREN', \
        'MINUS', 'MUL', 'PLUS', 'PROCEDURE', 'PROGRAM', 'REAL', 'REAL_CONST', 'RPAREN', 'SEMI', 'VAR'
    ) 


    def __init__(self, type, value):
        self.type = type
        self.value = value         # token value: 0, 1, 2. 3...'+', '-', '*', '/', ID, None

    def __str__(self):
        """String representation of the class instance.

        Examples:
            Token(INTEGER, 3)
            Token(PLUS '+')
            Token(MULTIPLY '*')
        """
        return 'Token({type}, {value})'.format(
            type=self.type,
            value=repr(self.value)
        )

    def __repr__(self):
        return self.__str__()


# RESERVED_KEYWORDS = {
#     'BEGIN': Token(Token.BEGIN, Token.BEGIN),
#     'END': Token(Token.END, Token.END),
#     }

RESERVED_KEYWORDS = {
    'PROGRAM': Token('PROGRAM', 'PROGRAM'),
    'VAR': Token('VAR', 'VAR'),
    'DIV': Token('INTEGER_DIV', 'DIV'),
    'INTEGER': Token('INTEGER', 'INTEGER'),
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
