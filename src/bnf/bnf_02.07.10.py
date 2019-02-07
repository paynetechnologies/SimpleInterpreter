"""
program : PROGRAM variable SEMI block DOT

    PROGRAM factorial; 
    BEGIN
        function factoria(a: integer): longint;
        begin
        end;
    END.

block : declarations compound_statement

declarations : (VAR (variable_declaration SEMI)+)*
    | (PROCEDURE ID (LPAREN formal_parameter_list RPAREN)? SEMI block SEMI)*
    | (FUNCTION  ID (LPAREN formal_parameter_list RPAREN : type_spec)? SEMI block SEMI)*
    | empty

variable_declaration : ID (COMMA ID)* COLON type_spec

formal_params_list : formal_parameters
                    | formal_parameters SEMI formal_parameter_list

formal_parameters : ID (COMMA ID)* COLON type_spec

type_spec : INTEGER | REAL | LONGINT
return_type_spec : STRING | INTEGER | LONGINT | REAL

compound_statement : BEGIN statement_list END

statement_list : statement
                | statement SEMI statement_list

statement : compound_statement
            | assignment_statement
            | if_statement
            | empty

assignment_statement : variable ASSIGN expr

if_statment : IF bool_expr THEN stat ELSE IF bool_expr THEN stat ELSE stat SEMI

bool_expr : True | False

cs : compound_statement

stat : statement

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
"""
