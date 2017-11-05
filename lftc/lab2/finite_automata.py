# TODO: Create a file containing the description of a deterministic FA describing the integer
# constants (literals) from C / C++ . Use it as test data for your program.


import json

class FiniteAutomata:
  def __init__(self, jsonObj = {}):
    self.json = jsonObj
    self.deterministic = True
    self.validate()
    self.graph = {}
    self.load_graph()

  def load_graph(self):
    for t in self.get_transitions():
      if t["from"] not in self.graph:
        self.graph[t["from"]] = {}
      if t["letter"] in self.graph[t["from"]]:
        print ("> Warning, autmoata is not a deterministic one!")
        self.deterministic = False
      self.graph[t["from"]][t["letter"]] = t["to"]

  def validate(self):
    if "states" not in self.json:
      raise ValueError("Json has no 'states' field.")
    if "alphabet" not in self.json:
      raise ValueError("Json has no 'alphabet' field.")
    if "transitions" not in self.json:
      raise ValueError("Json has no 'transitions' field.")
    if "initial_state" not in self.json:
      raise ValueError("Json has no 'initial_state' field.")
    if "accepted_states" not in self.json:
      raise ValueError("Json has no 'accepted_states' field.")
    if self.get_initial_state() not in self.get_states():
      raise ValueError("Initial state not a known state.")
    if True in [x not in self.get_states() \
        for x in self.get_accepted_states()]:
      raise ValueError("Initial state not a known state.")
    for t in self.get_transitions():
      if t["from"] not in self.get_states():
        raise ValueError("Transition contains unknown state.")
      if t["to"] not in self.get_states():
        raise ValueError("Transition contains unknown state.")
      if t["letter"] not in self.get_alphabet():
        raise ValueError("Transition letter not in the alphabet.")

  def get_states(self):
    return self.json["states"]

  def get_initial_state(self):
    return self.json["initial_state"]

  def get_accepted_states(self):
    return self.json["accepted_states"]

  def get_transitions(self):
    return self.json["transitions"]

  def get_alphabet(self):
    return self.json["alphabet"]

  def accept(self, seq):
    state = self.get_initial_state()
    for ch in seq:
      if state in self.graph and ch in self.graph[state]:
        state = self.graph[state][ch]
      else:
        return False
    return state in self.get_accepted_states()

  def longest_accepted_prefix(self, seq):
    state = self.get_initial_state()
    current = ""
    last_accepted = None
    if state in self.get_accepted_states():
      last_accepted = ""
    for ch in seq:
      if state in self.graph and ch in self.graph[state]:
        current += ch
        state = self.graph[state][ch]
        if state in self.get_accepted_states():
          last_accepted = current
      else:
        return last_accepted
    return last_accepted

class UI:
  def __init__(self, fa):
    self.fa = fa

  def print_menu(self):
    print("")
    print("> Menu")
    print("> 1. print set of states")
    print("> 2. print the alphabet")
    print("> 3. print all the trasitions")
    print("> 4. print accepted states")
    print("> 5. check if accepted")
    print("> 6. get the longest accepted prefix ")
    print("")
    print("> x. exit")
    print("")

  def run(self):
    while True:
      self.print_menu()
      op = raw_input("> ")
      if op == "1":
        print("> states: ["),
        print(", ".join([str(x) for x in self.fa.get_states()])),
        print("]")
      elif op == "2":
        print("> alphabet: "),
        print(self.fa.get_alphabet())
      elif op == "3":
        print("> transitions: [")
        print(",\n".join([">   %s ---%s---> %s" % (x["from"], x["letter"], x["to"]) \
            for x in self.fa.get_transitions()]))
        print("> ]")
      elif op == "4":
        print("> accepted states: ["),
        print(", ".join([str(x) for x in self.fa.get_accepted_states()])),
        print("]")
      elif op == "5":
        if not self.fa.deterministic:
          print("> Only for deterministic finite automata")
          continue
        seq = raw_input("> sequence: ")
        if self.fa.accept(seq):
          print("> Accepted")
        else:
          print("> Not accepted")
      elif op == "6":
        if not self.fa.deterministic:
          print("> Only for deterministic finite automata")
          continue
        seq = raw_input("> sequence: ")
        pref = self.fa.longest_accepted_prefix(seq)
        if pref == None:
          print("> No prefix is accepted")
        else:
          print("> The longest accepted prefix is: '%s'" % pref)
      elif op == "x":
        print("> bye bye")
        return
      else:
        print("> Error: Unknown operation")


def main():
  with open("fa.json") as f:
    fa = FiniteAutomata(json.load(f))
    ui = UI(fa)
    ui.run()

if __name__ == "__main__":
  main()
