import requests

try:
    res = requests.get('http://www.gutenberg.org/cache/epub/1113/pg1113.txt')
    res.raise_for_status()
except:
    print("There was a 404 error while trying to download your package")

playFile = open('RomeoAndJuliet2','wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)

playFile.close()

