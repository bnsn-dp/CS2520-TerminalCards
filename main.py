import random

COMMANDS = {
  "help"    : "Prints list of all commands AND Prints usage for given command",
  "decks"   : "Prints list of all decks",
  "current" : "Prints name of selected deck",
  "cards"   : "Prints list of all cards in selected deck",
  "select"  : "Selects a deck",
  "shuffle" : "Randomizes order of cards in selected deck",
  "draw"    : "Prints the question face of the card at the top of the deck",
  "flip"    : "Prints the answer face of the most recently drawn card",
  "add"     : "Adds a card to a deck",
  "quit"    : "Exits the program"
}

master_pile = {} #dictionary of all the cards in the deck. Unordered by default
queue = [] # an empty list that will hold the key-value pairs in a given order. Can be emptied, so we don't want to use the master_pile here
master_file = "" #file to keep track of current deck

def process(raw_command: str):
  segments = raw_command.split(" ", 1)
  command = segments[0]
  flags = segments[1] if len(segments) > 1 else ""
  match command:
    case "help":
      help(flags)
    case "decks":
      decks()
    case "current":
      current()
    case "cards":
      cards(flags)
    case "select":
      select(flags)
    case "shuffle":
      shuffle()
    case "draw":
      draw()
    case "flip":
      flip()
    case "add":
      add(flags)
    case "quit":
      exit()
    case _:
      print()
      print("unrecognized command")
      print()

def help(flags):
  print()
  if len(flags.split(" ")) > 1:
    print("\n\tToo many flags. \"help\" command takes only one flag [command]")
    return
  match flags:
    case "decks":
      print("\tUSAGE: \"decks\"")
    case "current":
      print("\tUSAGE: \"current\"")
    case "cards":
      print("\tUSAGE: \"cards\" [--ascend | -a] [--descend | -d] [--obscure | -o]")
      print("\tFLAG: [--ascend | -a] Prints cards sorted in ascending order")
      print("\t      [--descend | -d] Prints cards sorted in descending order")
      print("\t      [--obscure | -o] Prints cards without answers")
      print("\tNOTE: Needs a selected deck")
    case "select":
      print("\tUSAGE: \"select\" [deck]")
      print("\tFLAG: [deck] specifies which deck to choose")
    case "shuffle":
      print("\tUSAGE: \"shuffle\"")
      print("\tNOTE: Needs a selected deck")
    case "draw":
      print("\tUSAGE: \"draw\"")
      print("\tNOTE: Needs a selected deck")
    case "flip":
      print("\tUSAGE: \"flip\"")
      print("\tNOTE: Needs a recently drawn card")
    case "add":
      print("\tUSAGE: \"add\" [question]")
      print("\tNOTE: Needs a selected deck")
    case "quit":
      print("\tUSAGE: \"quit\"")
    case "":
      print("\tUSAGE: \"help\" [command]")
      print("\tFLAGS: [command] Prints usage and flags of [command]\n")
      for command, definition in COMMANDS.items():
        print("\t{:<12} {}".format(command, definition))
    case _:
      print("Unrecognized Command")
  print()

def decks():
  try:
    file = open("decks.txt", "r") #opening file that contains list of decks
    for line in file: #printing the list of decks
      line = line.rstrip("\n")
      print("\n\t" + line)
    print()
  except FileNotFoundError:
    print(f"\n\tNo decks found. Create a deck with the 'select' command\n")

def current():
  print(master_file)

def cards(flags):
  OBSCURE_FLAGS = [
    "--obscure",
    "-o"
  ]
  ASCEND_FLAG = [
    "--ascend",
    "-a"
  ]
  DESCEND_FLAG = [
    "--descend",
    "-d"
  ]
  obscured = False
  reverse = False
  split_flags = flags.split()
  if len(split_flags) > 3:
    print("\n\tToo many flags! \"cards\" takes at most three flags")
    help("cards")
    return -1
  for flag in split_flags:
    if flag in ASCEND_FLAG:
      reverse = False
    elif flag in DESCEND_FLAG:
      reverse = True
    elif flag in OBSCURE_FLAGS:
      obscured = True
    else:
      print("\n\tFlag " + flag + " not recognized. Try again")
      help("cards")
      return -1
  print()
  for q, a in sorted(master_pile.items(), reverse=reverse):
    if obscured:
      print("\t%s" % q)
    else:
      print("\t%s : %s" % (q, a))
  print()

def select(flags):
  global master_file #specifying that we are using the global variable
  global queue
  try: #making sure file exists and opening it
    file = open(flags, "r")
    master_file = flags #changing the current working deck
    file.close()
    update_master_pile() # This will populate master_pile with the cards so the other functions can use it
    queue = list(master_pile.items())
    print(f"\n\tDeck {flags} selected\n")
  except FileNotFoundError: #no file so we ask to create it
    print()
    answer = input("\tDeck not found. Do you want to create it? (yes/no): ")
    print()
    if answer == "yes":
      master_file = flags #changing the current working deck
      file = open(flags, "a") #creating file
      file.close()
      print(f"\n\tDeck {flags} selected\n")
      #saving the name of the newly added deck into a file
      file = open("decks.txt","a")
      file.write(master_file) #adding to list of decks
      file.close()

def shuffle():
  # Randomizes the order of the current master_pile
  global queue
  random.shuffle(queue)
  print("\n\tShuffled deck\n")

def draw():
  # Pops and prints a key off the top of the current master_pile
  global queue
  if queue:
    card_key, card_value = queue.pop() # removed parameter: last=False
    print("\n\tQuestion:", card_key, "\n")
  else:
    print("\n\tNo cards left in the deck.\n")

def flip():
  # Prints the value of the current key
  global master_pile # Accessing Global variable master_pile
  if master_pile:
    current_card_key = list(master_pile.keys())[-1] # Accessing the current card in the master_pile.
    print("\tAnswer:", master_pile[current_card_key]) # Prints the answer to the current card
  else:
    print("\tNo cards have been drawn yet.")

def add(flags):
  if master_file is None: #making sure we are using a deck
    print("\tNo deck selected")
    print("\tUse command 'select' to select/add a deck. Use command 'help' for list of commands")
  else:
    answer = input("\tEnter answer for %s: " % flags) #getting answer for the key/question
    #writing to file
    file = open(master_file, "a")
    file.write("%s : %s\n" % (flags, answer))
    file.close()
    update_master_pile() #updating the master pile

#updating the master pile
def update_master_pile():
  global master_file #specifying that we are using the global variable
  if master_file is not None:
    file = open(master_file, "r")
    for line in file:
      line = line.rstrip("\n")
      key, value = line.split(" : ")
      master_pile[key] = value
    file.close()
  else:
    print(f"\tNo deck selected. Use command 'select' to select/add a deck. Use command 'help' for list of commands")

def print_banner():
  print("""  _______                  _             _  _____              _     
 |__   __|                (_)           | |/ ____|            | |    
    | | ___ _ __ _ __ ___  _ _ __   __ _| | |     __ _ _ __ __| |___ 
    | |/ _ \\ '__| '_ ` _ \\| | '_ \\ / _` | | |    / _` | '__/ _` / __|
    | |  __/ |  | | | | | | | | | | (_| | | |___| (_| | | | (_| \\__ \\
    |_|\\___|_|  |_| |_| |_|_|_| |_|\\__,_|_|\\_____\\__,_|_|  \\__,_|___/""")
  print("\n\t(TC) by B.Diep, M. Nasla, J. Rodas, M. Yaskowitz")
  print()

def main():
  print_banner()
  print("Welcome to TerminalCards! Type \"help\" to get started\n")
  root = "User@CS2520\\"
  prompt_marker = "\\:~$ "
  while True:
    command = input(root + master_file + prompt_marker)
    process(command)

main()
