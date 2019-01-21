''' Token Class '''
class Token(object):
    ''' 
    Token 
    '''

    # Token types
    #
    # EOF (end-of-file) token is used to indicate that
    # there is no more input left for lexical analysis       
    INTEGER, NUM, ID, PLUS, MINUS, MUL, DIV, LPAREN, RPAREN, EOF = (
        'INTEGER', 'NUM', 'ID', 'PLUS', 'MINUS', 'MUL', 'DIV', 'LPAREN', 'RPAREN', 'EOF'
    )

    def __init__(self, type, value):
        
        # token type: INTEGER, PLUS, or EOF
        self.type = type
        # token value: 0, 1, 2. 3, 4, 5, 6, 7, 8, 9, '+', '-', '*', '/',or None
        self.value = value

    def __str__(self):
        """String representation of the class instance.

        Examples:
            Token(INTEGER, 3)
            Token(PLUS '+')
            Token(MULTIPLY '*')
            Token(DIVIDE '/')
        """
        return 'Token({type}, {value})'.format(
            type=self.type,
            value=repr(self.value)
        )

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    t = Token(Token.INTEGER, 12)
    print(t)


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