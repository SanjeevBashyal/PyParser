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