# MultiVRFY_Demo
A script I whipped up to quickly scan vulnerable mail servers for data using pythons's multiprocessing.

***WARNING***

***Use on a host without prior authorization MAY be illegal.
Please use responsibly and with caution. These scripts where developed in a private lab enviroment. For more information on finding hosts check https://nmap.org/book/legal-issues.html***

The list of users is a collection of usernames that we are checking against the vulnerable server.
The list of hosts is simply a collection of ips with port 25 open.
```
cwiegand@kali:~$ nmap -p 25 10.100.0.0/24 -oG smtp_open
cwiegand@kali:~$ cat smtp_open | grep "/open/" | cut -d " " -f 2 > hosts
```

Example output
```
cwiegand@kali:~$ python multiVrfy.py users hosts
[*] Running 91 Jobs.
[*] The results are in!
apache@10.100.0.1
bob@10.100.0.1
root@10.100.0.1
apache@10.100.0.2
root@10.100.0.2
[*] Execution took 34.1754479408 seconds.
```

The subprocess call starts vrfy.py whos skeleton originated from https://www.offensive-security.com.
