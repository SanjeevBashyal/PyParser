import sys
import os
from antlr4 import *
from SqlLexer import SqlLexer
from SqlParser import SqlParser
from SqlVisitor import SqlVisitor
from MySqlVisitor import MySqlVisitor

path=os.getcwd()

def readInputFile(filename):
    with open(filename) as fn:
        data = fn.read()
    return data

def main(argv):
    # Takes input from a file
    input = InputStream(readInputFile(os.path.join(path,'code.txt')))
    lexer = SqlLexer(input)
    stream = CommonTokenStream(lexer)
    parser = SqlParser(stream)
    tree = parser.prog()
    # MySqlVisitor extends the generated visitor file
    MySqlVisitor().visitProg(tree) # Evaluate the expression

if __name__ == '__main__':
    main(sys.argv)