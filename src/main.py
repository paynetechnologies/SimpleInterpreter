'''
Main
'''
import sys
import string

class Craddle:
    '''lex parser '''
    
    TAB = '\t'
    look = ''
    EOF = '$'
    WHITESPACE = ' \t\r\n'
    NEWLINE = '\n'


    #-----------------------------        
    #         Lex
    #-----------------------------

    def isAlpha(self, c):
        return c.isalpha()

    def isDigit(self, d):
        return d.isdigit()

    def isWhitespace(self, s):
        return s in [' \t\r\n']

    def skipWhiteSpace(self):
        while self.isWhitespace(self.look):
            self.look = self.getChar()

    def match(self, c):
        if self.look == c:
            self.look = self.getChar()
        else:
            self.expected(c)
        self.skipWhiteSpace()

    def getName(self):
        if not self.isAlpha(self.look):
            self.expected('Name')

        token = ''
        while self.isAlpha(self.look):
            token += self.look.upper()
            self.look = self.getChar()
        self.skipWhiteSpace()
        return token

    def getNum(self):
        if not self.isDigit(self.look):
            self.expected('Integer')

        token = ''
        while self.isDigit(self.look):
            token += self.look.upper()
            self.look = self.getChar()
        self.skipWhiteSpace()
        return token

    #-----------------------------        
    #         Parser
    #-----------------------------
    def assignment(self):
        name = self.getName()
        self.match('=')
        self.expression
        self.emitLine('LEA {name} (PC),A0')
        self.emitLine('MOVE D0,(A0)')



    def ident(self):
        name = self.getName()
        if self.look == '(':
            self.match('(')
            self.match(')')
            self.emitLine(f'BSR {name}')
        else:
            self.emitLine(f'MOVE {name} (PC),D0')
    
    
    '''
    <signed factor> ::= [<addop>] <factor>
    <factor> ::= <integer> | <variable> | (<expression>)
    '''
    def factor(self):
        if self.look == '(':
            self.match('(')
            self.expression()
            self.match(')')
        elif self.isAlpha(self.look):
            #self.emitLine('MOVE {self.getName()} (PC), D0')
            self.ident()
        else:
            self.emitLine(f'MOVE #{self.getNum()}, D0')

    '''
    term ::= <term> < + | - > <term>
    term ::= <factor> [ <mulop> <factor ]*
    <term> ::= <signed factor> [<mulop> factor]*
    '''
    def term(self):
        self.factor()
        while self.look in ['*', '/']:
            self.emitLine(f'MOVE D0,-(SP)')
            if self.look == '*':
                self.multiply()
            elif self.look == '/':
                self.divide()
            else:
                self.expected('MulOp')

    def add(self):
        self.match('+')
        self.term()
        self.emitLine('ADD (SP)+,D0')

    def subtract(self):
        self.match('-')
        self.term()
        self.emitLine('SUB (SP)+,D0')
        self.emitLine('NEG D0')
        
    def multiply(self):
        self.match('*')
        self.factor()
        self.emitLine('MULS (SP)+,D0')

    def divide(self):
        self.match('/')
        self.factor()
        self.emitLine('MOVE (SP)+,D1')
        self.emitLine('DIVS D1, D0')

    def isAddOp(self, c):
        return c in ['+', '-']

    '''
    <expression> ::= <unary op> <term> [<addop> <term>]*
    '''
    def expression(self):
        if self.isAddOp(self.look):
            self.emitLine('CLR D0')
        else:
            self.term()

        while self.isAddOp(self.look):
            self.emitLine(f'MOVE D0,-(SP)')

            if self.look == '+':
                self.add()
            elif self.look == '-':
                self.subtract()
            else:
                self.expected('AddOp')


    def getChar(self):
        self.bfrPtr += 1

        if self.bfrPtr >= len(self.code):
            return craddle.EOF

        return self.code[self.bfrPtr]            

    def __init__(self, code):
        super().__init__()
        self.code = code
        self.bfrPtr = -1
        self.lines = code.split('\n')

   
    def tokenize(self):
        self.look = self.getChar()
        while self.look != Craddle.EOF:        
            self.expression()

    #-----------------------------        
    #         Output
    #-----------------------------
    def emit(self, s):
        print(f'\t {s}')

    def emitLine(self, s):
        self.emit(s)


    #-----------------------------        
    #         Error
    #-----------------------------

    def error(self, s):
        print('')
        print(f'Error {s}')

    def abort(self, s):
        self.error(s)
        sys.exit()

    def expected(self, s):
        self.abort(s + ' Expected')

if __name__ == '__main__':
    craddle = Craddle('a+b-d')
    craddle.tokenize()
