'''
program : <compound_statement> PERIOD

compound_statement : BEGIN <statement_list> END

statement_list  : <statement> 
                | <statement> SEMI <statement_list>

statement   : <compound_statement>    
            | <assignment_statement>  
            | <empty>

assignment_statement : <var> ASSIGN_OP <expr>                        

empty :

expr : <term> ((PLUS | MINUS) <term>)*

term : <factor> ((MUL | DIV) <factor>)*

factor  : PLUS <factor>  
        | MINUS <factor>  
        | INTEGER     
        | LPAREN <expr> RPAREN  
        | <var>

var : ID

ID : [a..zA..Z]<alphanum>*

alpahnum : [a..zA..Z0..9_]

ASSIGN_OP : :=
PERIOD : .
PLUS : +
MINUS : -
MUL : *
DIV : /
SEMI : ;

“BEGIN END”
“BEGIN a := 5; x := 11 END”
“BEGIN a := 5; x := 11; END”
“BEGIN BEGIN a := 5 END; x := 11 END”
“a := 11”
“b := a + 9 - 5 * 2”
'''

"""
Part 14

program : PROGRAM variable SEMI block DOT

block : declarations compound_statement

declarations : (VAR (variable_declaration SEMI)+)*
    | (PROCEDURE ID (LPAREN formal_parameter_list RPAREN)? SEMI block SEMI)*
    | empty

variable_declaration : ID (COMMA ID)* COLON type_spec

formal_params_list : formal_parameters
                    | formal_parameters SEMI formal_parameter_list

formal_parameters : ID (COMMA ID)* COLON type_spec

type_spec : INTEGER

compound_statement : BEGIN statement_list END

statement_list : statement
                | statement SEMI statement_list

statement : compound_statement
            | assignment_statement
            | empty

assignment_statement : variable ASSIGN expr

empty :

expr : term ((PLUS | MINUS) term)*

term : factor ((MUL | INTEGER_DIV | FLOAT_DIV) factor)*

factor : PLUS factor
        | MINUS factor
        | INTEGER_CONST
        | REAL_CONST
        | LPAREN expr RPAREN
        | variable

variable: ID
"""