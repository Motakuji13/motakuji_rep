import urllib.request
url = "http://www.cbr.ru/scripts/XML_daily.asp"
webFile = urllib.request.urlopen(url)
data = webFile.read()
UrlSplit = url.split("/")[-1]
ExtSplit = UrlSplit.split(".")[1]
FileName = UrlSplit.replace(ExtSplit, "xml")
with open(FileName, "wb") as localFile:
    localFile.write(data)
webFile.close()

name = input("")