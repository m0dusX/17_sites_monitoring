# Sites Monitoring Utility

This script monitors all sites listed in a txt file by checking their status (online/offline) and registration expiration dates of their domain names and prints following information about each site in a txt to console:
1) Status: OK (ONLINE) / OFF (OFFLINE)
2) Information about domain name

# Quickstart

Place check_sites_health.py somewhere. Then run command line, go to folder in which you moved script and execute it with one parameter containing path to text file with sites.

Example of script launch on Linux, Python 3.5:

```#!bash

$ python check_sites_health.py <path to file>

```

Output data example:

```#!bash

1) https://google.com
Status: OK (ONLINE)
Domain name is paid for at least 1 month ahead

2) https://verisign.com
Status: OK (ONLINE)
Domain name is paid for at least 1 month ahead

3) https://aiiqoiqwdasdasd.com
Status: OFFLINE
Domain name was not found in registry
......

```


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
