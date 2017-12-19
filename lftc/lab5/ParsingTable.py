"""
table = {
  "0c" : "r5"
  "0S" : "1"
}
"""

class Table(object):
  """Table"""
  def __init__(self, grammar, gotos):
    super(Table, self).__init__()
    self.grammar = grammar
    self.gotos = gotos
    # self.terminals = terminals
    # self.non_terminals = non_terminals

    # Total number of states (total gotos)
    self.states = gotos.expected_id
    self.table = {}
    # self.action = [[None] * (terminals)] * states
    # self.goto = [[None] * (non_terminals)] * states

  def fillTable(self):
    pass

  def key(self, state, action):
    return str(state) + str(action)

  def insert(self, state, action, value):
    k = self.key(state, action)
    if k not in self.table:
      self.table[k] = {
        "state": state,
        "action": action,
        "value": set([value])
      }
    else:
      self.table[k]["value"].add(value)

    # self.table[k] = {
    #   "state": state,
    #   "action": action,
    #   "value": set([value]) if k not in self.table else self.table[k]["value"] + ", " + value
    # }

  def get(self, state, action):
    return self.table[self.key(state, action)]

  def generate(self):
    print "## Generate parsing table"
    self.generate_shift()
    self.generate_reduction()
    self.generate_goto()
    self.display()

  def generate_shift(self):
    productions = self.grammar.get_dot_terminal_productions()
    for production in productions:
      # print production, "===", production.next_symbol()
      goto_list = self.gotos.find_production(production)
      for goto in goto_list:
        print goto
        goto_to_shift = self.gotos.goto_dict[str(goto.id) + production.next_symbol().symbol]
        # print goto_to_shift.parent_goto, goto_to_shift.closure, goto_to_shift.id

        self.insert(goto_to_shift.parent_goto, goto_to_shift.closure, "S" + str(goto_to_shift.id))
    # for production in self.grammar.grammar:
    #   print production

  def generate_reduction(self):
    productions = self.grammar.get_alpha_dot_productions()

    for production in productions:
      follows = self.grammar.first_follow.follow[production.non_terminal]
      gotos = self.gotos.find_production(production)
      for follow in follows:
        for g_production in self.grammar.grammar:
          if g_production.non_terminal == production.non_terminal and \
            g_production.production == production.production:
            for goto in gotos:
              self.insert(goto.id, follow, "R" + str(production.index))

  def generate_goto(self):
    non_terminals = self.grammar.non_terminals[1:]
    for goto in self.gotos.gotos:
      if goto.closure in non_terminals:
        self.insert(int(goto.parent_goto), goto.closure, str(goto.id))
        # print goto

  def display(self):
    # table = [[""] * (len(self.grammar.terminals) + len(self.grammar.non_terminals))] * (self.states + 1)
    print "\nSLR Parsing Table\n"

    table = [["" for i in range(len(self.grammar.terminals) + len(self.grammar.non_terminals))] for j in range(self.states + 1)]

    display_terminals = self.grammar.terminals + ["$"]
    display_non_terminals = self.grammar.non_terminals
    display_non_terminals.pop(0)
    display_keys = display_terminals + display_non_terminals

    for key in self.table:
      o = self.table[key]
      # table[o["state"]][display_keys.index(o["action"].symbol)] = o["value"]
      table[o["state"]][display_keys.index(o["action"])] = list(o["value"])


    def list_to_str(l):
      r = ""
      for x in l:
        r += str(x) + " "
      return r

    print "   |",
    for cnt, key in enumerate(display_keys):
      print "%5s" %key, "|",
    print "\n","-" * (8 * (cnt + 1) + 4)

    for i, line in enumerate(table):
      print "%2d |" %i,
      for value in line:
        print "%5s" % list_to_str(value), "|",
      print 
