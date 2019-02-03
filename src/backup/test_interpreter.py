import unittest


class LexerTestCase(unittest.TestCase):
    def makeLexer(self, text):
        from src.Lexer import Lexer
        lexer = Lexer(text)
        return lexer

    def test_01_lexer_integer(self):
        from src.Token import Token
        lexer = self.makeLexer('234')
        token = lexer.get_next_token()
        self.assertEqual(token.type, Token.INTEGER_CONST)
        self.assertEqual(token.value, 234)

    def test_02_lexer_mul(self):
        from src.Token import Token
        lexer = self.makeLexer('*')
        token = lexer.get_next_token()
        self.assertEqual(token.type, Token.MUL)
        self.assertEqual(token.value, '*')

    def test_03_lexer_div(self):
        from src.Token import Token
        lexer = self.makeLexer(' / ')
        token = lexer.get_next_token()
        self.assertEqual(token.type, Token.FLOAT_DIV)
        self.assertEqual(token.value, '/')

    def test_04_lexer_plus(self):
        from src.Token import Token
        lexer = self.makeLexer('+')
        token = lexer.get_next_token()
        self.assertEqual(token.type, Token.PLUS)
        self.assertEqual(token.value, '+')

    def test_05_lexer_minus(self):
        from src.Token import Token
        lexer = self.makeLexer('-')
        token = lexer.get_next_token()
        self.assertEqual(token.type, Token.MINUS)
        self.assertEqual(token.value, '-')

    def test_06_lexer_lparen(self):
        from src.Token import Token
        lexer = self.makeLexer('(')
        token = lexer.get_next_token()
        self.assertEqual(token.type, Token.LPAREN)
        self.assertEqual(token.value, '(')

    def test_07_lexer_rparen(self):
        from src.Token import Token
        lexer = self.makeLexer(')')
        token = lexer.get_next_token()
        self.assertEqual(token.type, Token.RPAREN)
        self.assertEqual(token.value, ')')

    def test_08_lexer_new_tokens(self):
        from src.Token import Token
        #ASSIGN,  DOT, ID, SEMI, BEGIN, END

        records = (
            (':=', Token.ASSIGN, ':='),
            ('.', Token.DOT, '.'),
            ('number', Token.ID, 'number'),
            (';', Token.SEMI, ';'),
            ('BEGIN', Token.BEGIN, 'BEGIN'),
            ('END', Token.END, 'END'),
        )
        for text, tok_type, tok_val in records:
            lexer = self.makeLexer(text)
            token = lexer.get_next_token()
            self.assertEqual(token.type, tok_type)
            self.assertEqual(token.value, tok_val)

class InterpreterTestCase(unittest.TestCase):
    def makeInterpreter(self, text):
        from src.Lexer import Lexer
        from src.Parser import Parser
        from src.Interpreter import Interpreter
        lexer = Lexer(text)
        parser = Parser(lexer)
        interpreter = Interpreter(parser)
        return interpreter

    def test_09_arithmetic_expressions(self):
        for expr, result in (
            ('3', 3),
            ('2 + 7 * 4', 30),
            ('7 - 8 / 4', 5),
            ('14 + 2 * 3 - 6 / 2', 17),
            ('7 + 3 * (10 / (12 / (3 + 1) - 1))', 22),
            ('7 + 3 * (10 / (12 / (3 + 1) - 1)) / (2 + 3) - 5 - 3 + (8)', 10),
            ('7 + (((3 + 2)))', 12),
            ('- 3', -3),
            ('+ 3', 3),
            ('5 - - - + - 3', 8),
            ('5 - - - + - (3 + 4) - +2', 10),
        ):
            interpreter = self.makeInterpreter('BEGIN a := %s END.' % expr)
            interpreter.interpret()
            globals = interpreter.GLOBAL_MEMORY
            self.assertEqual(globals['a'], result)

    def test_10_expression_invalid_syntax1(self):
        interpreter = self.makeInterpreter('10 *')
        with self.assertRaises(Exception):
            interpreter.interpret()

    def test_11_expression_invalid_syntax2(self):
        interpreter = self.makeInterpreter('1 (1 + 2)')
        with self.assertRaises(Exception):
            interpreter.interpret()

    def test_12_expression_invalid_syntax3(self):
        interpreter = self.makeInterpreter('BEGIN a := 10 * ; END.')
        with self.assertRaises(Exception):
            interpreter.interpret()

    def test_13_expression_invalid_syntax4(self):
        interpreter = self.makeInterpreter('BEGIN a := 1 (1 + 2); END.')
        with self.assertRaises(Exception):
            interpreter.interpret()

    def test_14_statements(self):
        text = """\
BEGIN

    BEGIN
        number := 2;
        a := number;
        b := 10 * a + 10 * number / 4;
        c := a - - b
    END;

    x := 11;
END.
"""
        interpreter = self.makeInterpreter(text)
        interpreter.interpret()

        globals = interpreter.GLOBAL_MEMORY
        self.assertEqual(len(globals.keys()), 5)
        self.assertEqual(globals['number'], 2)
        self.assertEqual(globals['a'], 2)
        self.assertEqual(globals['b'], 25)
        self.assertEqual(globals['c'], 27)
        self.assertEqual(globals['x'], 11)


if __name__ == '__main__':
    unittest.main()


'''
try:
    linux_interaction()
except AssertionError as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally:
    print('Cleaning up, irrespective of any exceptions.')
'''    