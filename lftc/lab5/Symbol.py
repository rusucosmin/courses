"""
January 27, 2015
"""
class Symbol(object):
  """Symbol"""
  def __init__(self, symbol, grammar):
    self.symbol = symbol.strip()
    self.grammar = grammar

    # Terminal is set to True if it is terminal. This variable is used for
    # quick access instead of searching the grammar again and again.
    self.terminal = None

  def is_terminal(self):
    # Checks if the symbol is terminal. For first time request, it checks the
    # gramar. Later, terminal variable is directly used.
    if self.terminal == None:
      self.terminal = self.symbol not in self.grammar.non_terminals
    return self.terminal

  def __str__(self):
    return self.symbol

  def __eq__(self, other):
    if isinstance(other, Symbol) and other.symbol == self.symbol:
      return True
    elif isinstance(other, int) and other == self.symbol:
      return True
    elif isinstance(other, str) and other == self.symbol:
      return True
    return False


def main():
  a = Symbol("a", None)
  b = Symbol("b", None)
  aa = Symbol("a", None)

  print [Symbol("c", None), Symbol("a", None)].index(aa)

if __name__ == '__main__':
  main()
