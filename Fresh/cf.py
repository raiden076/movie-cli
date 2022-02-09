import requests
import re
from bs4 import BeautifulSoup
import urllib.parse

embeded_url = "https://streamm4u.com/watch/movie/interstellar-2014.21586.html"

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0",
}

response = requests.get(url=embeded_url, headers=headers)

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

print(response.text)
