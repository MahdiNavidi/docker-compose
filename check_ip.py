from urllib.request import urlopen
from urllib.error import URLError

try:
    with urlopen('https://api.ipify.org', timeout=30) as response:
        ip = response.read().decode('utf-8').strip()
        print("External IP:", ip)
        with open('ip.txt', 'w') as file:
            file.write(ip)
except URLError as e:
    print("Error fetching IP:", e)