''' Token Class '''
class Token(object):
    ''' 
    Token 
    '''

       
    ID, INTEGER, PLUS, MINUS, MULTIPLY, DIVIDE, LPAREN, RPAREN, EOF = 'ID', 'INTEGER', 'PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE', 'LPAREN', 'RPAREN', 'EOF'

    def __init__(self, token_type, token_value):
        
        # token type: INTEGER, PLUS, or EOF
        self.token_type = token_type

        # token value: 0, 1, 2. 3, 4, 5, 6, 7, 8, 9, '+', '-', '*', '/',or None
        self.token_value = token_value

    def __str__(self):
        """String representation of the class instance.

        Examples:
            Token(INTEGER, 3)
            Token(PLUS '+')
            Token(MULTIPLY '*')
            Token(DIVIDE '/')
        """
        return 'Token({type}, {value})'.format(
            type=self.token_type,
            value=repr(self.token_value)
        )

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    t = Token(Token.INTEGER, 12)
    print(t)
