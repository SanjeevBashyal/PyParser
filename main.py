import sys
import os
from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
# from MySqlVisitor import MySqlVisitor

path=os.getcwd()

def readInputFile(filename):
    with open(filename) as fn:
        data = fn.read()
    return data

def main(argv):
    # Takes input from a file
    input = InputStream(readInputFile(os.path.join(path,'code.txt')))
    lexer = ExprLexer(input)
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)
    tree = parser.prog()
    # MySqlVisitor extends the generated visitor file
    # MySqlVisitor().visitProg(tree) # Evaluate the expression
    print(tree.toStringTree())

if __name__ == '__main__':
    main(sys.argv)