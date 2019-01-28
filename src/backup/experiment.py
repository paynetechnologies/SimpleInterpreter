# Token types
#
# EOF (end-of-file) token is used to indicate that
# there is no more input left for lexical analysis
INTEGER       = 'INTEGER'
REAL          = 'REAL'
INTEGER_CONST = 'INTEGER_CONST'
REAL_CONST    = 'REAL_CONST'
PLUS          = 'PLUS'
MINUS         = 'MINUS'
MUL           = 'MUL'
INTEGER_DIV   = 'INTEGER_DIV'
FLOAT_DIV     = 'FLOAT_DIV'
LPAREN        = 'LPAREN'
RPAREN        = 'RPAREN'
ID            = 'ID'
ASSIGN        = 'ASSIGN'
BEGIN         = 'BEGIN'
END           = 'END'
SEMI          = 'SEMI'
DOT           = 'DOT'
PROGRAM       = 'PROGRAM'
VAR           = 'VAR'
COLON         = 'COLON'
COMMA         = 'COMMA'
EOF           = 'EOF'

class Token():
    ''' 
    Token 
    '''

    def __init__(self, type, value):
        self.type = type
        self.value = value

    # Token types
    (
        ASSIGN, BEGIN, COLON, COMMA, DIV, DOT, END, FLOAT_DIV, 
        EOF, ID, INTEGER, INTEGER_CONST, INTEGER_DIV, LPAREN, 
        MINUS, MUL, PLUS, PROGRAM,  REAL, REAL_CONST, RPAREN, SEMI, VAR
    ) = ( 
        'ASSIGN', 'BEGIN', 'COLON', 'COMMA', 'DIV', 'DOT', 'END', 'FLOAD_DIV', \
        'EOF', 'ID', 'INTEGER', 'INTEGER_CONST', 'INTEGER_DIV', 'LPAREN', \
        'MINUS', 'MUL', 'PLUS', 'PROGRAM', 'REAL', 'REAL_CONST', 'RPAREN', 'SEMI', 'VAR'
    ) 


RK = {
    'BEGIN': Token(Token.BEGIN, Token.BEGIN),
    'END': Token(Token.END, Token.END),
    }

RK2 = {
    'PROGRAM': Token('PROGRAM', 'PROGRAM'),
    'VAR': Token('VAR', 'VAR'),
    'DIV': Token('INTEGER_DIV', 'DIV'),
    'INTEGER': Token('INTEGER', 'INTEGER'),
    'REAL': Token('REAL', 'REAL'),
    'BEGIN': Token('BEGIN', 'BEGIN'),
    'END': Token('END', 'END'),
}

def main():
    print(f'RK : {[t for t in RK]}')
    print(f'RK2 : {[t for t in RK2]}')
    print(f'token.assign : {Token.ASSIGN}')
        

if __name__ == "__main__":
    main()