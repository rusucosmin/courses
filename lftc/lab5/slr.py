'''

SLR PARSING

'''
import sys

from Grammar import Grammar
from Goto import GotoGenerator
from ParsingTable import Table
from LR_Parser import LR_Parser

# default grammar and input string if no argument is given by user

grammar = """
X' := S
S := T S'
S' := + T S' | E
T := F T'
T' := * F T' | E
F := ( S ) | id | const
"""
input = "id + ( id * id )"


def main(*argv):
  global input, grammar
  if len(argv[0]) == 2:
    grammar = """"""
    with open(argv[0][0], 'r') as content_file:
        grammar = content_file.read()

    input = argv[0][1]

  g = Grammar(grammar)
  g.parse()
  gotos = GotoGenerator(g)
  gotos.generate()
  gotos.display()

  g.first_follow.display()

  parsing_table = Table(g, gotos)
  parsing_table.generate()

  lr_parser = LR_Parser(g, parsing_table, input)
  lr_parser.parse()

  # print parsingTable.get("5", "$")

if __name__ == '__main__':
  main(sys.argv[1:])
