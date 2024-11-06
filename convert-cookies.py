import sys
from datetime import datetime

filename = sys.argv[1] if len(sys.argv) > 1 else ''
if not filename:
    print("Usage: python convert-cookies.py <file-with-cookies-copy-pasted-from-Chrome.txt> > netscape-cookies.txt");
    print();
    print("Make sure to replace <file-with-cookies-copy-pasted-from-Chrome.txt> with the name of the file in which you copy/pasted the cookies from Chrome's Application -> Storage -> Cookies.");
    print("Then, pass the 'netscape-cookies.txt' file to 'curl' or 'yt-dlp' or any other tool that reads cookies in the Netscape cookies format.");
    sys.exit(1)

with open(filename, 'r', encoding='utf-8-sig') as f:
    cookies = f.read().splitlines()

print('# Netscape HTTP Cookie File')

for cookie in cookies:
    try:
        parts = cookie.split('\t')
        name = parts[0]
        value = parts[1]
        domain = parts[2]
        path = parts[3]
        expiration = parts[4]
        httpOnly = parts[6]
    except:
        continue
    if not domain.startswith('.'):
        domain = '.' + domain
    httpOnly = 'TRUE' if httpOnly == '✔' else 'FALSE'
    if expiration == 'Session':
        expiration = '0'
    else:
        expiration = str(int(datetime.strptime(expiration, "%Y-%m-%dT%H:%M:%S.%fZ").timestamp()))
    print('\t'.join([domain, 'TRUE', path, httpOnly, expiration, name, value]))
