import os

def read_file(filename, friend1, friend2):
	chat_history = []
	current_turn = ''
	if os.path.isfile(filename):
		with open(filename,'r') as rf:
				for line in rf:
					if friend1 not in line and friend2 not in line:
						chat_history.append([current_turn,line.strip()])
					elif friend1 in line:
						current_turn = friend1
					elif friend2 in line:
						current_turn = friend2

	else:
		print("File not found")
	
	return chat_history


def write_file(chat_history):
	with open("output.txt","w") as wf:
		for item in chat_history:
			wf.write(item[0]+": " + item[1] + "\n")


def main():
	filename = input("Please enter a file name to open: ")
	write_file(read_file(filename,'Isaac','Ken'))


main()
  