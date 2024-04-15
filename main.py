# How to implement terminal-like commands in python
# 1. Take the command as string input
# 2. Split the string into a tuple
# 3. Read the first item as the core command
# 4. Feed the remaining elements of the tuple into an appropriate parameter


def process(raw_command: str):
	segments = raw_command.split(" ", 1)
	command = segments[0]
	flags = segments[0] if len(segments > 1) else ""
	match command:
		case "help":
			help(flags)
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
	return 0

def current(flags):
	return 0

def cards(flags):
	return 0

def select(flags):
	return 0

def shuffle(flags):
	return 0

def draw(flags):
	return 0

def flip(flags):
	return 0

def add(flags):
	return 0

def print_banner():
	print("TerminalCards (TC) by B.Diep, M. Nasla, J. Rodas, M. Yaskowitz")
	print()

def main():
	master_pile = {}
	print_banner()
	print("Welcome to TerminalCards! Type \"help\" to get started\n")
	root = "User@CS2520"
	working_deck = ""
	prompt_marker = ":~$ "
	while True:
		command = input(root + working_deck + prompt_marker)
		process(command)

main()