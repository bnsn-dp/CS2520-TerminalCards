# How to implement terminal-like commands in python
# 1. Take the command as string input
# 2. Split the string into a tuple
# 3. Read the first item as the core command
# 4. Feed the remaining elements of the tuple into an appropriate parameter
import random

master_pile = {} #dictionary of all the cards in the deck. Unordered by default
queue = [] # an empty list that will hold the key-value pairs in a given order. Can be emptied, so we don't want to use the master_pile here
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
  print("\t{:<12} {}".format("decks", "Prints list of all decks"))
  print("\t{:<12} {}".format("current", "Prints current working deck"))
  print("\t{:<12} {}".format("cards[!]", "Prints list of all cards in current working deck"))
  print("\t{:<12} {}".format("select", "Changes current working deck"))
  print("\t{:<12} {}".format("shuffle[!]", "Randomizes order of cards in current working deck"))
  print("\t{:<12} {}".format("draw[!]", "Prints the question of the card at the top of the current working deck"))
  print("\t{:<12} {}".format("flip[!]", "Prints the answer of the most recently drawn card"))
  print("\t{:<12} {}".format("add[!]", "Adds a card to a deck"))
  print("\t{:<12} {}".format("quit", "Exits the program"))
  print()

def decks(flags):
  # Flags:
  #	  [--sort | -s <name | size> <ascend | descend>]: Sorts the decks with the specified rules
  #     For example: "decks --sort name ascend" would return the decks sorted by name in alphabetical order
  try:
    file = open("decks.txt", "r") #opening file that contains list of decks
    for line in file: #printing the list of decks
      line = line.rstrip("\n")
      print(line + "\n")
  except FileNotFoundError:
    print(f"No decks found. Create a deck with the 'select' command")

def current(flags):
  print(master_file)

def cards(flags):
  # Prints out the contents of the master_file
  # Flags:
  #   [--sort | -s <name | size> <ascend | descend>]: Sorts the cards with the specified rules
  #     For example: "cards --sort name ascend" would return the decks sorted by name in alphabetical order
  split = flags.split()
  if len(split) == 0:
    for key, value in master_pile.items():
      print(f"{key}: {value}")
  elif split[0] == "--sort" or split[0] == "-s":
    if split[1] == "name" and split[2] == "ascend":
      sort = sorted(master_pile.keys())
      for name in sort:
        print(name, master_pile[name])
    elif split[1] == "name" and split[2] == "descend":
      sort = sorted(master_pile.keys(), reverse=True)
      for name in sort:
        print(name, master_pile[name])
    elif split[1] == "size" and split[2] == "ascend":
      sort = dict(sorted(master_pile.items(), key=lambda item: len(item[0])))
      for name, age in sort.items():
        print(name, age)
    elif split[1] == "size" and split[2] == "descend":
      sort = dict(sorted(master_pile.items(), key=lambda item: len(item[0]), reverse=True))
      for name, age in sort.items():
        print(name, age)

  #return 0

def select(flags):
  # Flags:
  # 	"name": a string specifying the name of the deck.

  global master_file #specifying that we are using the global variable
  try: #making sure file exists and opening it
    file = open(flags, "r")
    master_file = flags #changing the current working deck
    file.close()
    update_master_pile() # This will populate master_pile with the cards so the other functions can use it
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
  # Randomizes the order of the current master_pile
  keys = list(master_pile.keys())
  random.shuffle(keys)
  for key in keys:
    print(f"{key}: {master_pile[key]}")

def draw(flags):
  # Pops and prints a key off the top of the current master_pile
  if master_pile:
    card_key, card_value = master_pile.popitem(last=False)
    print("Question:", card_key)
  else:
    print("No cards left in the deck.")

def flip(flags):
  # Prints the value of the current key
  global master_pile # Accessing Global variable master_pile
  if master_pile:
    current_card_key = list(master_pile.keys())[-1] # Accessing the current card in the master_pile.
    print("Answer:", master_pile[current_card_key]) # Prints the answer to the current card
  else:
    print("No cards have been drawn yet.")

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
