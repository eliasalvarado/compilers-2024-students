import sys
from antlr4 import *
from MiniLangLexer import MiniLangLexer
from MiniLangParser import MiniLangParser
from antlr4.error.ErrorListener import ErrorListener

class MyErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"Error: En línea {line}, columna {column}: {msg}. Token no reconocido.")

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = MiniLangLexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(MyErrorListener())
    stream = CommonTokenStream(lexer)
    parser = MiniLangParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(MyErrorListener())
    tree = parser.prog()  # We are using 'prog' since this is the starting rule based on our MiniLang grammar, yay!

if __name__ == '__main__':
    main(sys.argv)
