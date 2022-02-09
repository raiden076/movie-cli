import requests
import json
import re
from bs4 import BeautifulSoup
import subprocess

# using beautifulsoup4, cause I'm lazy, and still not that good at regex
import urllib.parse

page_url = input("Enter the url: ")

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0",
}

response = requests.get(url=page_url, headers=headers)

XSRF_TOKEN = response.cookies["XSRF-TOKEN"]
laravel_session = response.cookies["laravel_session"]

soup = BeautifulSoup(response.text, "html.parser")
csrf = soup.find("meta", attrs={"name": "csrf-token"})["content"]
id_f = soup.find("span", attrs={"id": "fem"})["data"]

url_csrf = urllib.parse.quote_plus(csrf)
url_id_f = urllib.parse.quote_plus(id_f)

cookies = {
    "__atuvc": "1%7C6",
    "dom3ic8zudi28v8lr6fgphwffqoz0j6c": "39d958b5-4c51-411c-9885-e8f07116f003%3A3%3A1",
    "XSRF-TOKEN": XSRF_TOKEN,
    "laravel_session": laravel_session,
}

headers = {
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Accept-Language": "en-US,en;q=0.5",
    "Origin": "https://streamm4u.com/",
    "Referer": "https://streamm4u.com/watch/movie",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Te": "trailers",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0",
}

data = "_token=" + url_csrf + "&m4u=" + url_id_f

response = requests.post(
    "https://streamm4u.com/anhjax", headers=headers, cookies=cookies, data=data
)

# print(response.text)

soup2 = BeautifulSoup(response.text, "html.parser")

embeded_url = soup2.find("iframe")["src"]

embeded_id = re.split(r"/", embeded_url)[-1]


# embeded_url = input("input the page url: ")

# headers = {
#     'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0',
# }

# response = requests.get(url=embeded_url, headers=headers)
# print(response.cookies)

# embeded_url = "z7ek8ijkqwp33l8"
fuck_curl = "https://streamm4u.club/api/source/" + embeded_id

headers = {
    "Accept-Language": "en-US,en;q=0.5",
    "Origin": "https://streamm4u.club",
    "Referer": "https://streamm4u.club",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Te": "trailers",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0",
}

response = requests.post(url=fuck_curl, headers=headers, data="")


tokens_json = json.loads(response.text)
p_1080 = tokens_json["data"][2]["file"]
tok_1080 = re.split(r"\?token=", p_1080)[1]
# completely unnecessary regex, just a little show off :")
# will remove later.
print(tok_1080)


headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Referer": "https://streamm4u.club/",
    "Sec-Fetch-Dest": "iframe",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Te": "trailers",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0",
}

fuck_bash = "https://fvs.io/redirector?token=" + tok_1080

link_html = requests.head(url=fuck_bash, headers=headers)

stream_link = link_html.headers["Location"]

subprocess.Popen(["mpv", stream_link])

# print(link_html.headers)


# soup3 = BeautifulSoup(link_html.text, "html.parser")

# the .mp4 file is in the headers.
# I don't know why, but maybe this is a redirector, and python doesn't like it, or something?
# Anyway, I know you probably don't can fix this.
# nevermind, got it..

# https://streamm4u.com/watch/movie/interstellar-2014.21586.html
