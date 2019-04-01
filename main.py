# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

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
        href_ar.append(href.encode())
        b = b+1
    return href_ar

def get_sequence(id):
    download = []
    author = ""
    b_idf = 0
    b_ide = 0
    b_idm = 0
    x = 0
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
        if "fb2" in href:
            temp_d.append(href)
            b_idf = href.replace("/b/", "")
            b_idf = b_idf.replace("/fb2", "")
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
        if "/a/" in href and author == "":
            author = i.text.encode("utf-8")
    result = []
    result.append(author)
    result.append(download)
    return result

def get_book(id):
    download = []
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
    return download

def get_author(id):
    url = "http://flibusta.is/a/"+id
    request = requests.get(url)

search_r = search("Тургенев")
#print(search_r)
print(get_sequence(21476))