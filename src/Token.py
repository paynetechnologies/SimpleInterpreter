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

    def __repr__(self):
        return self.__str__()

    def __init__(self, _type, value, line_no=0, line_pos=0):        
        self.type = _type
        self.value = value
        self.line_no = line_no
        self.line_pos = line_pos #- len(value)
        
    def __str__(self):
        return '{0}:{1}'.format(self.line_no, self.line_pos).ljust(10) + self.type.ljust(15) + str(self.value)


RESERVED_KEYWORDS = {
    'BEGIN': Token('BEGIN', 'BEGIN'),
    'DIV': Token('INTEGER_DIV', 'DIV'),
    'END': Token('END', 'END'),
    'FUNCTION': Token('FUNCTION', 'FUNCTION'),
    'INTEGER': Token('INTEGER', 'INTEGER'),
    'LONGINT': Token('LONGINT', 'LONGINT'),
    'PROCEDURE' : Token('PROCEDURE', 'PROCEDURE'),
    'PROGRAM': Token('PROGRAM', 'PROGRAM'),
    'REAL': Token('REAL', 'REAL'),
    'VAR': Token('VAR', 'VAR'),    
}

if __name__ == '__main__':
    print(Token(Token.INTEGER, Token.INTEGER))
