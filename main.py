import tkinter
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
	print("\t{:<8} {}".format("help", "Prints list of all commands"))
	print("\t{:<8} {}".format("quit", "Exits the program"))
	print()

def print_banner():
	print("TerminalCards (TC) by B.Diep, M. Nasla, J. Rodas, M. Yaskowitz")
	print()

def main():
	master_pile = {}
	print_banner()
	while True:
		command = input("User@CS2520:~$ ")
		process(command)
	return 0

main()