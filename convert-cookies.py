import sys
from datetime import datetime, timedelta

if len(sys.argv) < 2:
    print("Usage: python convert_cookies.py <file-with-cookies-copy-pasted-from-Chrome.txt> > netscape-cookies.txt")
    print("\nMake sure to replace <file-with-cookies-copy-pasted-from-Chrome.txt> with the name of the")
    print("file in which you copy/pasted the cookies from Chrome's Application -> Storage -> Cookies.")
    print("\nThen, pass the 'netscape-cookies.txt' file to 'curl' or 'youtube-dl' or any other tool")
    print("that reads cookies in the Netscape cookies format.")
    sys.exit(1)

filename = sys.argv[1]
with open(filename, 'r', encoding='utf-8-sig') as f:
    cookies = f.read().splitlines()

print('# Netscape HTTP Cookie File')

for cookie in cookies:
    if not cookie:
        continue
    parts = cookie.split('\t')
    if len(parts) < 7:
        continue
    name = parts[0]
    value = parts[1]
    domain = parts[2]
    path = parts[3]
    expiration = parts[4]
    http_only = parts[6]
    if not name:
        continue
    if not domain.startswith('.'):
        domain = '.' + domain
    http_only = 'TRUE' if http_only == '✔' else 'FALSE'
    if expiration == 'Session':
        expiration = '2147483647' #format spec not specifying maximum value, assume it is 32-bit 
    else:
        expiration = str(int(datetime.strptime(expiration, "%Y-%m-%dT%H:%M:%S.%fZ").timestamp()))
    print(f"{domain}\tTRUE\t{path}\t{http_only}\t{expiration}\t{name}\t{value}")
