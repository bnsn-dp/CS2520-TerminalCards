# How to implement terminal-like commands in python
# 1. Take the command as string input
# 2. Split the string into a tuple
# 3. Read the first item as the core command
# 4. Feed the remaining elements of the tuple into an appropriate parameter

master_pile = {} #dictionary of all the cards in the deck
master_file = None #file to keep track of current deck
def process(raw_command: str):
  segments = raw_command.split(" ", 1)
  command = segments[0]
  flags = segments[1] if len(segments )> 1 else ""
  match command:
    case "help":
      help()
    case "decks":
      decks(flags)
    case "current":
      current(flags)
    case "cards":
      cards(flags)
    case "select":
      select(flags)
    case "shuffle":
      shuffle(flags)
    case "draw":
      draw(flags)
    case "flip":
      flip(flags)
    case "add":
      add(flags)
    case "quit":
      exit()
    case _:
      print()
      print("unrecognized command")
      print()

def help():
  print()
  print("\t{:<12} {}".format("help", "Prints list of all commands"))
  print("\t{:<12} {}".format("decks[!]", "Prints list of all decks"))
  print("\t{:<12} {}".format("current[!]", "Prints current working deck"))
  print("\t{:<12} {}".format("cards[!]", "Prints list of all cards in current working deck"))
  print("\t{:<12} {}".format("select[!]", "Changes current working deck"))
  print("\t{:<12} {}".format("shuffle[!]", "Randomizes order of cards in current working deck"))
  print("\t{:<12} {}".format("draw[!]", "Prints the question of the card at the top of the current working deck"))
  print("\t{:<12} {}".format("flip[!]", "Prints the answer of the most recently drawn card"))
  print("\t{:<12} {}".format("add[!]", "Adds a card to a deck"))
  print("\t{:<12} {}".format("quit", "Exits the program"))
  print()

def decks(flags):
  try:
    file = open("decks.txt", "r") #opening file that contains list of decks
    for line in file: #printing the list of decks
      line = line.rstrip("\n")
      print(line + "\n")
  except FileNotFoundError:
    print(f"No decks found. Create a deck with the 'select' command")

def current(flags):
  return 0

def cards(flags):
  return 0

def select(flags):
  global master_file #specifying that we are using the global variable
  try: #making sure file exists and opening it
    file = open(flags, "r")
    master_file = flags #changing the current working deck
    file.close()
    print(f"Deck {flags} selected")
  except FileNotFoundError: #no file so we ask to create it
    print()
    answer = input("Deck not found. Do you want to create it? (yes/no): ")
    if answer == "yes":
      master_file = flags #changing the current working deck
      file = open(flags, "a") #creating file
      file.close()
      print(f"Deck {flags} selected")
      #saving the name of the newly added deck into a file
      file = open("decks.txt","a")
      file.write(master_file) #adding to list of decks
      file.close()

def shuffle(flags):
  return 0

def draw(flags):
  return 0

def flip(flags):
  return 0

def add(flags):
  if master_file is None: #making sure we are using a deck 
    print(" No deck selected")
    print(" Use command 'select' to select/add a deck. Use command 'help' for list of commands")
  else:
    answer = input("Enter answer for %s: " % flags) #getting answer for the key/question
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
    print(f"No deck selected. Use command 'select' to select/add a deck. Use command 'help' for list of commands")

def print_banner():
  print("TerminalCards (TC) by B.Diep, M. Nasla, J. Rodas, M. Yaskowitz")
  print()

def main():
  print_banner()
  print("Welcome to TerminalCards! Type \"help\" to get started\n")
  root = "User@CS2520"
  working_deck = ""
  prompt_marker = ":~$ "
  while True:
    command = input(root + working_deck + prompt_marker)
    process(command)

main()
