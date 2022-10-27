import sys
from antlr4 import *
<<<<<<< HEAD

=======
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from MySqlVisitor import MySqlVisitor

def readInputFile():
    pass
>>>>>>> 6626bcdef85f05274215467d82e1e8af213a172d

def main(argv):
    # Takes input from a file
    input = InputStream(readInputFile("test.txt"))
    lexer = ExprLexer(input)
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)
    tree = parser.prog()
    # MySqlVisitor extends the generated visitor file
    MySqlVisitor().visitProg(tree) # Evaluate the expression

if __name__ == '__main__':
    main(sys.argv)