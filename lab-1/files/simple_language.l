%{
#include <cstdlib>
#include <string>
#include "y.tab.h"
extern void yyerror(const char *s);
%}

%%

[a-zA-Z][a-zA-Z0-9]*    { yylval.str = new std::string(yytext);  return ID; }
[0-9]+                  { yylval.num = strtol(yytext, NULL, 10); return NUMBER; }
"+"                     { return '+'; }
"-"                     { return '-'; }
"*"                     { return '*'; }
"/"                     { return '/'; }
"="                     { return '='; }
":"                     { return ':'; }
[ \t]                  ;  // skip whitespace
\n                      ;  // skip newlines
.                       yyerror("Invalid character");

%%

int yywrap() {
    return 1;
}