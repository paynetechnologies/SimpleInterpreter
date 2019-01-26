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
