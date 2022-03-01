# allows for sleeping
from time import sleep
# allows for running external code
import subprocess

# get the current ip address
ip = subprocess.getoutput("ifconfig | grep 'inet 128*'")
ip_prev = ip


subprocess.getoutput("python3 simple_telegram.py")

# conntinually
while True:
	sleep(30)
	# check the IP
	ip = subprocess.getoutput("ifconfig | grep 'inet 128*'")
	#if it hasnt changed then we dont need to do anything
	if ip == ip_prev:
		continue
	else:
		# if it has changed, record the change
		ip_prev = ip
		# run the python script that will text the Telegram bot's owner

		# this script runs the same command and sends it to me
		subprocess.getoutput("python3 simple_telegram.py")
