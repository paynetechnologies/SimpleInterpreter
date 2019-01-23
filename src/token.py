''' Token Class '''
class Token():
    ''' 
    Token 
    '''
    # Token types
    # EOF (end-of-file) token is used to indicate that
    # there is no more input left for lexical analysis       
    (ASSIGN, BEGIN, DIV, DOT, END, EOF, ID, INTEGER, LPAREN, MINUS, MUL, PLUS, RPAREN, SEMI) = ( \
        'ASSIGN', 'BEGIN', 'DIV', 'DOT', 'END', 'EOF', 'ID', 'INTEGER', 'LPAREN', \
        'MINUS', 'MUL', 'PLUS', 'RPAREN', 'SEMI') 


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


RESERVED_KEYWORDS = {
    'BEGIN': Token(Token.BEGIN, Token.BEGIN),
    'END': Token(Token.END, Token.END),
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
