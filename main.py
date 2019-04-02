# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import json
from http.server import BaseHTTPRequestHandler, HTTPServer


def search(search):
    b = 0
    href_ar = []
    request = requests.get("http://flibusta.is/booksearch?ask="+search)
    soup = BeautifulSoup(request.text)
    for i in soup.findAll("a", href=True):
        href = i['href']
        if "polka" in href:
            continue
        if "comment" in href:
            continue
        if "http" in href:
            continue
        if "https" in href:
            continue
        if "node" in href:
            continue
        if "booksearch" in href:
            continue
        if href == "/":
            continue
        if "user" in href:
            continue
        if "catalog" in href:
            continue
        if "daily" in href:
            continue
        if "sql" in href:
            continue
        if "dostup" in href:
            continue
        if "comp" in href:
            continue
        if "rec" in href:
            continue
        if "%" in href:
            continue
        if "new" in href:
            continue
        if "stat" in href:
            continue
        if "Other" in href:
            continue
        if "blog" in href:
            continue
        if "forum" in href:
            continue
        if "all" in href:
            continue
        if "tracker" in href:
            continue
        if len(href) <= 3:
            continue
        href_ar.append(href.encode("utf-8").decode())
        b = b+1
    return href_ar

def get_sequence(id):
    download = []
    author = ""
    b_idf = 0
    b_ide = 0
    b_idm = 0
    x = 0
    b_name = ""
    temp_d = []
    try:
        url = "http://flibusta.is/sequence/"+id
    except Exception:
        url = "http://flibusta.is/sequence/"+str(id)
    request = requests.get(url)
    soup = BeautifulSoup(request.text)
    for i in soup.findAll("a", href=True):
        href = str(i['href'])
        if "polka" in href:
            continue
        if "comment" in href:
            continue
        if "http" in href:
            continue
        if "https" in href:
            continue
        if "node" in href:
            continue
        if "booksearch" in href:
            continue
        if href == "/":
            continue
        if "user" in href:
            continue
        if "catalog" in href:
            continue
        if "daily" in href:
            continue
        if "sql" in href:
            continue
        if "dostup" in href:
            continue
        if "comp" in href:
            continue
        if "rec" in href:
            continue
        if "%" in href:
            continue
        if "new" in href:
            continue
        if "stat" in href:
            continue
        if "Other" in href:
            continue
        if "blog" in href:
            continue
        if "forum" in href:
            continue
        if "all" in href:
            continue
        if "tracker" in href:
            continue
        if len(href) <= 3:
            continue
        if "/b/" in href:
            b_name_now = i.text.encode("utf-8").decode()
            if b_name == "":
                temp_d.append(b_name_now)
                b_name = b_name_now
        if "fb2" in href:
            b_idf = href.replace("/b/", "")
            b_idf = b_idf.replace("/fb2", "")
            temp_d.append(href)
            x = x + 1
        if "epub" in href:
            temp_d.append(href)
            b_ide = href.replace("/b/", "")
            b_ide = b_ide.replace("/epub", "")
            x = x + 1
        if "mobi" in href:
            temp_d.append(href)
            b_idm = href.replace("/b/", "")
            b_idm = b_idm.replace("/mobi", "")
            x = x + 1
        if b_idf == b_idm and b_idf == b_ide and x == 3:
            download.append(temp_d)
            temp_d = []
            x = 0
            b_name = ""
        if "/a/" in href and author == "":
            author = i.text.encode("utf-8").decode()
    result = []
    result.append(author)
    result.append(download)
    return result

def get_book(id):
    download = []
    b_name = ""
    author = ""
    try:
        url = "http://flibusta.is/b/"+id
    except Exception:
        url = "http://flibusta.is/b/" + str(id)
    request = requests.get(url)
    soup = BeautifulSoup(request.text)
    for i in soup.findAll("a", href=True):
        href = str(i['href'])
        if "polka" in href:
            continue
        if "comment" in href:
            continue
        if "http" in href:
            continue
        if "https" in href:
            continue
        if "node" in href:
            continue
        if "booksearch" in href:
            continue
        if href == "/":
            continue
        if "user" in href:
            continue
        if "catalog" in href:
            continue
        if "daily" in href:
            continue
        if "sql" in href:
            continue
        if "dostup" in href:
            continue
        if "comp" in href:
            continue
        if "rec" in href:
            continue
        if "%" in href:
            continue
        if "new" in href:
            continue
        if "stat" in href:
            continue
        if "Other" in href:
            continue
        if "blog" in href:
            continue
        if "forum" in href:
            continue
        if "all" in href:
            continue
        if "tracker" in href:
            continue
        if len(href) <= 3:
            continue
        if "fb2" in href:
            download.append(href)
        if "epub" in href:
            download.append(href)
        if "mobi" in href:
            download.append(href)
        if "/a/" in href and author == "":
            author = i.text.encode("utf-8").decode()
    art = soup.findAll("img", src=True)
    cover = ""
    for i in art:
        if "i" in i['src']:
            cover = i['src']
    name = soup.find("h1", {"class": "title"}).text
    rem_array = ["(", ")", "fb2", "mobi", "epub"]
    for i in rem_array:
        name = name.replace(i, "")
    result = []
    result.append(author)
    result.append(name)
    result.append(cover)
    result.append(download)
    return result

def get_author(id):
    url = "http://flibusta.is/a/"+id
    request = requests.get(url)

search_r = search("Тургенев")
#print(search_r)
#print(get_sequence(21476))

def apicommands(path):
	try:
		parms = path.split("?")[1].split("&")
	except Exception:
		parms = {}
	if "search" in path:
		search_q = parms[0].split("=")[1]
		search_r = search(search_q)
		search_r = json.dumps(search_r)
		return search_r
	if "get_sequence" in path:
		id = parms[0].split("=")[1]
		links = get_sequence(id)
		links = json.dumps(links)
		return links
	if "get_book" in path:
		id = parms[0].split("=")[1]
		links = get_book(id)
		links = json.dumps(links)
		return links
	

port = 8900

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if('/api' in self.path):
            self.send_response(200)
            self.send_header("Content-type", "text/json")
            self.end_headers()
            self.wfile.write(apicommands(self.path).encode())

myServer = HTTPServer(('0.0.0.0', port), MyServer)

try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass

myServer.server_close()