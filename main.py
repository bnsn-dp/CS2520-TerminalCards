# How to implement terminal-like commands in python
# 1. Take the command as string input
# 2. Split the string into a tuple
# 3. Read the first item as the core command
# 4. Feed the remaining elements of the tuple into an appropriate parameter


def process(string):
	match string:
		case "help":
			help()
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