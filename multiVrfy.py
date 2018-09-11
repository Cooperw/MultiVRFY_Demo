#!/usr/bin/python

#Written By: Cooper Wiegand

#*** WARNING ***
#Use on a host without prior authorization may be illegal
#use responsibly and with caution.

import multiprocessing as mp
import string
import itertools
import sys
import subprocess
import os
import time

#Define function
def attempt_vrfy(jobs, output):
	DEVNULL = open(os.devnull,'w')
	while True:
		job = jobs.get()
		if job is None: break

		try:
			subprocess.check_call(['python','./vrfy.py'
				,job[1],job[0]], stdout=DEVNULL)
			output.put(job[0]+'@'+job[1])
		except:
			pass

if __name__ == '__main__':

	startTime = time.time()

	if len(sys.argv) != 3:
		print "Usage: {0} <users_list> <hosts_list>".format(sys.argv[0])
		sys.exit(1)

	#Define an output queue
	output = mp.Queue()

	#Define an input queue
	jobs = mp.Queue()

	#Populate ips and users
	users = []
	ips = []
	with open(sys.argv[1]) as f:
		users = f.read().splitlines()
	with open(sys.argv[2]) as f:
		ips = f.read().splitlines()
	myList = list(itertools.product(users,ips))

	print("[*] Running {0} Jobs.".format(len(myList)))

	pool = [ mp.Process(target=attempt_vrfy, args=(jobs,output))
		for x in range(len(myList)) ]

	#Run processes
	for p in pool:
		p.start()

	#Add list to jobs
	for i in myList:
		jobs.put(i)

	#Add loop break
	for p in pool:
		jobs.put(None)

	#Exit completed processes
	for p in pool:
		p.join()

	print("[*] The results are in!")

	#Get Results
	while not output.empty():
		print(output.get())

	print("[*] Execution took %s seconds." % (time.time() - startTime))
