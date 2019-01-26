'''
Main
'''
import sys

def isAlpha(c):
    return c.isalpha()

def isDigit(d):
    return d.isdigit()

def isWhitespace(s):
    return s in [' \t\r\n']

class Compiler:
    '''lex parser '''

    TAB = '\t'
    look = ''
    EOF = '$'
    WHITESPACE = ' \t\r\n'
    NEWLINE = '\n'

    def __init__(self):
        super().__init__()
        self.bfrPtr = -1
        self.lines = None
        self.code = None

    def load(self, code):
        self.code = code
        self.lines = code.split('\n')


    #-----------------------------
    #         Lex
    #-----------------------------



    def skipWhiteSpace(self):
        while isWhitespace(self.look):
            self.look = self.getChar()

    def match(self, c):
        if self.look == c:
            self.look = self.getChar()
        else:
            self.expected(c)
        self.skipWhiteSpace()

    def getName(self):
        if not isAlpha(self.look):
            self.expected('Name')

        token = ''
        while isAlpha(self.look):
            token += self.look.upper()
            self.look = self.getChar()
        self.skipWhiteSpace()
        return token

    def getNum(self):
        if not isDigit(self.look):
            self.expected('Integer')

        token = ''
        while isDigit(self.look):
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
        self.expression()
        self.emitLine(f'LEA {name} (PC),A0')
        self.emitLine(f'MOVE D0,(A0)')



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
        elif isAlpha(self.look):
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
            return Compiler.EOF

        return self.code[self.bfrPtr]            

    def tokenize(self):
        self.look = self.getChar()
        while self.look != Compiler.EOF:
            self.assignment()

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
    c = Compiler()
    c.load('a=b-d')
    c.tokenize()

    
