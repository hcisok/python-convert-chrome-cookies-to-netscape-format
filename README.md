# Convert Chrome cookies to Netscape format

This script is ported from [dandv/convert-chrome-cookies-to-netscape-format](https://github.com/dandv/convert-chrome-cookies-to-netscape-format). It aims to work with yt-dlp and systems without Node.js installed.

This is a very simple Python script to convert the cookies you can copy/paste from Chrome's Application -> Storage -> Cookies, into the [Netscape cookies format](https://curl.haxx.se/docs/http-cookies.html) accepted by tools like `curl` and `yt-dlp`.

It's useful because you don't have to install any browser extension in order to save or convert the cookies. [Browser extensions are a known security risk.](https://www.howtogeek.com/188346/why-browser-extensions-can-be-dangerous-and-how-to-protect-yourself/)


## Requirements

* A terminal/command line window
* [Python](https://www.python.org/downloads/)


## Usage

1. Download convert-cookies.py (or clone this repo if you prefer)
2. In an editor, open a new blank file
2. In Chrome/Chromium, launch Developer Tools (F12)
3. Navigate to the site you need cookies from, e.g. YouTube, and log in.
4. Go to Application -> Storage -> Cookies
5. For each URL under Cookies (e.g. `https://www.youtube.com`), copy the table of cookies into the clipboard, then paste it at the end of the file you've opened in step 2. ![Chrome cookies](chrome-cookies.png)
6. Save the file with a name like `file-with-cookies-copy-pasted-from-Chrome.txt` 
7. Run the script:

       python convert-cookies.py file-with-cookies-copy-pasted-from-Chrome.txt > netscape-cookies.txt

Now, `netscape-cookies.txt` will contain cookies ready to be used by any application that reads cookies in Netscape format (e.g. `yt-dlp` or `curl`).


## Author

[hcisok](https://github.com/hcisok)
